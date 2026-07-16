import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class FaqComponent(BaseComponent):
    """Раздел 'Вопросы о важном'"""

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Клик на часто задаваемый вопрос по индексу:'{index}'")
    def click_faq_question_button(self, index: str):
        self.page.locator(f"#accordion__heading-{index}").nth(0).click()

    @allure.step("Проверка ожидаемого текста часто задаваемого вопроса по индексу:'{index}'")
    def check_faq_question_text(self, index: str, expected_text: str):
        expect(self.page.locator(f"#accordion__panel-{index}").nth(0)).to_have_text(expected_text)
