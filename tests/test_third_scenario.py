from pages.sbis_home_page import SbisHomePage


def test_third_scenario(driver):

    sbis_home_page = SbisHomePage(driver)

    sbis_download_page = sbis_home_page.go_to_download_sbis()
    sbis_download_page.click_sbis_plugin_tab()
    sbis_download_page.download_sbis_plugin()
    assert sbis_download_page.sbis_plugin_is_downloaded()
    assert sbis_download_page.plugin_size_is_correct()
