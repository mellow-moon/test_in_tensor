from pages.sbis_home_page import SbisHomePage


def test_second_scenario(driver):
    
    sbis_home_page = SbisHomePage(driver)

    sbis_contacts_page = sbis_home_page.go_to_contacts_page()
    assert sbis_contacts_page.region_defined_correct()
    assert sbis_contacts_page.partners_list_presented_and_visible()
    sbis_contacts_page.change_region()
    assert sbis_contacts_page.region_changed_successfully()
    assert sbis_contacts_page.partners_list_changed_successfully()
    assert sbis_contacts_page.url_is_correct()
    assert sbis_contacts_page.title_is_correct()
