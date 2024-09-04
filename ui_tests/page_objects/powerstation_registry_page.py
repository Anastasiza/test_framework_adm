import time

import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class PowerstationRegistry:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    @allure.step("Get powerstation registry")
    def get_powerstation_registry(self):
        self.logger.info("Get powerstation registry")
        self.browser.get(self.base_url + 'admin/#/powerstation')
        powerstation_registry_label = WebDriverWait(self.browser, 60).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/app-top-menu/screens-container/ng-component/div/sdk-table-container/sdk-table-toolbar/mat-toolbar/mat-toolbar-row/div[1]')))
        return powerstation_registry_label.text

    @allure.step("Get powerstation Id")
    def get_powerstation_id(self):
        self.logger.info('Get powerstation Id')
        powerstation_id = WebDriverWait(self.browser, 30).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/app-root/app-top-menu/screens-container/ng-component/div/sdk-table-container/div/div/sdk-table-list/div/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[3]/div/span')))
        return powerstation_id
