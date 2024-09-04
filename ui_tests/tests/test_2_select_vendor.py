from ui_tests.page_objects.vendor_selector_page import VendorSelector


def test_select_vendor(browser, base_url):
    select_vendor_dialog = VendorSelector(browser, base_url)
    select_vendor_dialog.selecting_all_vendors()
    select_vendor_dialog.selecting_place()
    select_vendor_dialog.selecting_general_vendor()
    select_vendor_dialog.save_vendor_setup()
    assert select_vendor_dialog.get_account_title()
