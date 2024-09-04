import time

from selenium.webdriver import Keys

import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import logging
import allure


class VendorSelector:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    @allure.step("Selecting all vendors")
    def selecting_all_vendors(self):
        self.logger.info('Selecting all vendors')
        select_all_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "body > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div.modal-body.ng-scope > div.text-right > button:nth-child(1)")))
        select_all_button.click()

    @allure.step("Selecting place")
    def selecting_place(self):
        self.logger.info('Selecting place')
        select_place = Select(self.browser.find_element(By.ID, 'placeSelect'))
        select_place.select_by_value(config.target_place_id)
        time.sleep(2)

    @allure.step("Selecting general vendor")
    def selecting_general_vendor(self):
        self.logger.info('Selecting general vendor')

        select_general_vendor = Select(self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/select'))
        select_general_vendor.select_by_value(config.general_vendor)
        time.sleep(2)


    @allure.step("Save vendor setup")
    def save_vendor_setup(self):
        self.logger.info('Save vendor setup')
        save_button = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button")
        save_button.click()
        time.sleep(4)

    @allure.step("Get account title")
    def get_account_title(self):
        self.logger.info('Get account title')
        account_title = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="navbar"]/ul[3]/li[2]/ul[1]/span[2]')))
        return account_title
