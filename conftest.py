import json
from pathlib import Path

import allure
import pytest

from config.environments import Environment, environments, print_environment_info

# ============================================================
#   Настройка и отчетность
# ============================================================


def pytest_addoption(parser):
    """Добавление опций для выбора конфигурации запуска тестов"""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=[e.value for e in Environment],
        help="Окружение для запуска тестов",
    )


@pytest.fixture(scope="session", autouse=True)
def show_env_info(browser_name, request):
    """Вывод информации о тестовом окружении перед запуском"""
    env_name = request.config.getoption("--env")
    print_environment_info(env_name, browser_name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Создает скриншот в Allure при падении теста."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs["page"]
            allure.attach(
                page.screenshot(full_page=True),
                name=f"screenshot_{item.nodeid}",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")


# ============================================================
#   Базовые фикстуры фреймворка (Браузер и Приложение)
# ============================================================


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, env_config):
    """Настраивает контекст браузера, расширяя стандартную фикстуру плагина pytest-playwright."""
    return {
        **browser_context_args,
        "base_url": env_config.url,
        "ignore_https_errors": True,
        "viewport": {"width": 1920, "height": 1080},
    }


# ============================================================
#   Фикстуры конфигурации и данных
# ============================================================


@pytest.fixture(scope="session")
def env_config(request):
    """Предоставляет конфигурацию окружения"""
    env_name = request.config.getoption("--env")
    return environments[Environment(env_name)]


@pytest.fixture(scope="function")
def load_test_data(request):
    """Загружает тестовые данные окружения из test_data/{env}.json."""
    env = Environment(request.config.getoption("--env").lower())
    data_path = Path(__file__).parent / "test_data" / f"{env.value}.json"
    with data_path.open("r", encoding="utf-8") as data_file:
        return json.load(data_file)
