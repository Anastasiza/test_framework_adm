import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class Powerstation:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    @allure.step("Get powerstation")
    def get_powerstation(self):
        self.logger.info("Get powerstation")
        powerstation_id = WebDriverWait(self.browser, 30).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                               '/html/body/app-root/app-top-menu/screens-container/ng-component/div/sdk-table-container/div/div/sdk-table-list/div/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[3]/div/span')))
        powerstation_id.click()
        time.sleep(5)
        powerstation_label = WebDriverWait(self.browser, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[1]/about-island/island-title/h2")))
        return powerstation_label

    @allure.step("Get name")
    def get_powerstation_name(self):
        self.logger.info("Get name")
        name = self.browser.find_element(By.XPATH, "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[1]/about-island/section/div[2]/property[1]/div[2]")
        return name

    @allure.step("Get SN")
    def get_powerstation_sn(self):
        self.logger.info("Get SN")
        sn = self.browser.find_element(By.XPATH,
                                         "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[1]/about-island/section/div[2]/property[3]/div[2]")
        return sn

    @allure.step("Get city")
    def get_powerstation_city(self):
        self.logger.info("Get city")
        city = self.browser.find_element(By.XPATH,
                                       "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[2]/div/location-island/section/div[1]/property[3]/div[2]")
        return city

    @allure.step("Get provider id")
    def get_powerstation_prov_id(self):
        self.logger.info("provider id")
        provider_id = self.browser.find_element(By.XPATH,
                                         "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[1]/provider-island/section/div[2]/property/div[2]")
        return provider_id


    @allure.step("Get vendor")
    def get_powerstation_vendor(self):
        self.logger.info("provider vendor")
        vendor = self.browser.find_element(By.XPATH,
                                         "/html/body/app-root/app-top-menu/screens-container/ng-component/div[2]/div[1]/business-island/div/property[6]/div[2]/span")
        return vendor
