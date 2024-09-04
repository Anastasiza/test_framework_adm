from ui_tests.page_objects.powerstation_page import Powerstation
import time


def test_powerstation_registy_label(browser, base_url):
    label = Powerstation(browser, base_url).get_powerstation()
    assert label


def test_get_powerstation_name(browser, base_url):
    name = Powerstation(browser, base_url).get_powerstation_name()
    assert name


def test_get_powerstation_sn(browser, base_url):
    sn = Powerstation(browser, base_url).get_powerstation_sn
    assert sn


def test_get_powerstation_city(browser, base_url):
    city = Powerstation(browser, base_url).get_powerstation_city
    assert city


def test_get_powerstation_provider_id(browser, base_url):
    provider_id = Powerstation(browser, base_url).get_powerstation_prov_id
    assert provider_id


def test_get_powerstation_vendor(browser, base_url):
    vendor = Powerstation(browser, base_url).get_powerstation_vendor
    assert vendor

