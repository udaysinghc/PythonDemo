import time

import pytest
import allure

from pages.university_file_upload.upload_file import UploadFile


@pytest.mark.usefixtures("setup")
class TestUploadFile:

    @allure.title("Upload file")
    @allure.description("Verify that the notification You need to select a file to upload!")
    def test_upload_file(self):
        uploadfile = UploadFile(self.driver)
        uploadfile.open()
        uploadfile.title("File Upload")
        uploadfile.verify_notification_to_file_upload()

    @allure.title("Upload file")
    @allure.description("verify that the notification Your file has now been uploaded")
    def test_submit_button(self):
        uploadfile = UploadFile(self.driver)
        uploadfile.open()
        uploadfile.title("File Upload")
        uploadfile.upload_file()

    @allure.title("File name ")
    @allure.description("Verify uploaded file name")
    def test_file_name(self):
        uploadfile = UploadFile(self.driver)
        uploadfile.open()
        uploadfile.title("File Upload")
        uploadfile.Verify_file_name()
