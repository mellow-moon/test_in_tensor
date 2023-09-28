from pages.sbis_home_page import SbisHomePage


def test_first_scenario(driver):

    sbis_home_page = SbisHomePage(driver)
    
    sbis_contacts_page = sbis_home_page.go_to_contacts_page()

    tensor_home_page = sbis_contacts_page.click_tensor_banner()
    assert tensor_home_page.people_strength_block_is_presented()

    tensor_about_page = tensor_home_page.go_to_tensor_about()
    assert tensor_about_page.url_is_valid()
    assert tensor_about_page.all_photos_are_the_same_size()
