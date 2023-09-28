from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage


class TensorHomePage(BasePage):

    PEOPLE_STRENGTH_TITLE = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]/p[1]')
    TENSOR_ABOUT_LINK = (By.XPATH, '//a[@href="/about" and contains(@class, "tensor_ru-link")]')

    def people_strength_block_is_presented(self):
        title = 'Сила в людях'

        block_is_presented = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.PEOPLE_STRENGTH_TITLE, title)
        )

        return block_is_presented

    def go_to_tensor_about(self):
        url = self.get_url_by_locator(self.TENSOR_ABOUT_LINK)
        self.go_to_url(url)

        return TensorAboutPage(self.driver)
