import time

import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class LoginPage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    @allure.step("Open login page")
    def get_login_page(self):
        self.logger.info("Open login page")
        self.browser.get(self.base_url + 'identity/account/login')
        WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/div/section/form/div[5]/button')))

    @allure.step("Login")
    def login(self):
        self.logger.info("Login")

        username_input = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "Email")))
        username_input.send_keys(config.username)

        pass_input = self.browser.find_element(By.ID, "Password")
        pass_input.send_keys(config.password)

        submit_buttton = self.browser.find_element(By.XPATH, '/html/body/div/div/div/div/section/form/div[5]/button')
        submit_buttton.click()

    @allure.step("Check enter")
    def get_vendor_list_selector(self):
        self.logger.info('Get vendor list')

        self.browser.get(self.base_url)
        enter_menu_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="navbar"]/ul[2]/li[2]/a')))
        enter_menu_button.click()

        vendor_list_selector = WebDriverWait(self.browser, 60).until(expected_conditions.presence_of_element_located(
            (By.ID, "modal-title")))

        return vendor_list_selector
