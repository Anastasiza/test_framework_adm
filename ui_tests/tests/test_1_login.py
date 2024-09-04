from ui_tests.page_objects.login_page import LoginPage


def test_auth(browser, base_url):
    adm = LoginPage(browser, base_url)
    adm.get_login_page()
    adm.login()
    assert adm.get_vendor_list_selector()
