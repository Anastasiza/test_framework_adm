from ui_tests.page_objects.powerstation_registry_page import PowerstationRegistry


def test_powerstation_registy_label(browser, base_url):
    label = PowerstationRegistry(browser, base_url).get_powerstation_registry()
    assert label


def test_powerstation_id(browser, base_url):
    powerstation_id = PowerstationRegistry(browser, base_url).get_powerstation_id()
    assert powerstation_id
