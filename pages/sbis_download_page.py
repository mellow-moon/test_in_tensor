import wget
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class SbisDownloadPage(BasePage):

    SBIS_PLUGIN_TAB = (By.XPATH, '//div[@name="TabButtons"]/div[2]')
    SBIS_DOWNLOAD_PLUGIN_LINK = (By.LINK_TEXT, 'Скачать (Exe 3.64 МБ)')

    def click_sbis_plugin_tab(self):
        sbis_plugin_tab = self.find(self.SBIS_PLUGIN_TAB)

        x_offset = 1
        y_offset = 1

        ac = ActionChains(self.driver)
        ac.move_to_element(sbis_plugin_tab).move_by_offset(x_offset, y_offset).click().perform()

    def download_sbis_plugin(self):
        url = self.get_url_by_locator(self.SBIS_DOWNLOAD_PLUGIN_LINK)
        path = os.getcwd()

        wget.download(url, out = path)
    
    def sbis_plugin_is_downloaded(self):
        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        return os.path.isfile(downloaded_file_path)

    def plugin_size_is_correct(self):
        current_dir = os.getcwd()

        downloaded_file_name = 'sbisplugin-setup-web.exe'
        downloaded_file_path = current_dir + '/' + downloaded_file_name

        true_file_size = 3.64

        downloaded_file_size = os.path.getsize(downloaded_file_path) / 1048576
        downloaded_file_size = round(downloaded_file_size, 2)

        return downloaded_file_size == true_file_size
