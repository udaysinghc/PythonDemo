import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.webdriver.support.wait import WebDriverWait

from base.page_base import PageBase
from locators.locators import FileUpload


class UploadFile(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify that the notification You need to select a file to upload!")
    def verify_notification_to_file_upload(self):
        self.driver.find_element(*FileUpload.submit_button).send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print("Alert Text:", alert_text)
        assert alert_text == "You need to select a file to upload!"
        alert.accept()

    @allure.step("verify that the notification Your file has now been uploaded")
    def upload_file(self):
        file_path = os.path.abspath("test.csv")
        self.driver.find_element(*FileUpload.file_type).send_keys(file_path)
        self.driver.find_element(*FileUpload.submit_button).send_keys(Keys.ENTER)
        time.sleep(0.6)
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == "Your file has now been uploaded!", f"Error: File not uploaded!"
        alert.accept()
        time.sleep(0.6)

    @allure.step("Verify file name")
    def Verify_file_name(self):
        file_path = os.path.abspath("test.csv")
        file_input = self.driver.find_element(*FileUpload.file_type)
        file_input.send_keys(file_path)
        time.sleep(0.6)
        uploaded_file_name = os.path.basename(file_path)
        time.sleep(0.6)
        expected_file_name = "test.csv"
        time.sleep(0.6)
        assert uploaded_file_name == expected_file_name, f"Error: Upload file name {uploaded_file_name} is not match with {expected_file_name}"
