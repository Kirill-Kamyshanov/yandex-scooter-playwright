import json
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class Environment(StrEnum):
    DEV = "dev"
    STAGE = "stage"


@dataclass
class UserData:
    first_name: str
    last_name: str
    address: str
    metro_station: str
    phone_number: str


@dataclass
class EnvironmentConfig:
    url: str
    user_1: UserData
    user_2: UserData

    def __str__(self):
        return f"- URL: {self.url}"


def load_test_user(environment: Environment, number: str) -> UserData:
    """Подгружает из json-файлов тестовых юзеров"""
    filepath = Path(__file__).parent.parent / "test_data" / f"{environment.value}.json"
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        return UserData(**data["test users"][number])


environments = {
    Environment.DEV: EnvironmentConfig(url="https://qa-scooter.praktikum-services.ru/",
                                       user_1=load_test_user(Environment.DEV, "1"),
                                       user_2=load_test_user(Environment.DEV, "2")
                                       ),
    Environment.STAGE: EnvironmentConfig(url="https://qa-scooter.praktikum-services.ru/",
                                         user_1=load_test_user(Environment.STAGE, "1"),
                                         user_2=load_test_user(Environment.STAGE, "2")
                                         )
}


def print_environment_info(env_name, browser="Chrome"):
    """Выводит краткую сводку по тестовому окружению"""
    env = Environment(env_name)

    print()
    print(f"- Окружение: {env.value.upper()}")
    print(f"- Браузер: {browser}")
    print(f"- Юзер 1: {environments[env].user_1.first_name} {environments[env].user_1.last_name}")
    print(f"- Юзер 2: {environments[env].user_2.first_name} {environments[env].user_2.last_name}")
    print()
