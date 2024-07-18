import time

import allure
import pytest

from pages.university_contact_us.contact_us import ContactUs


@pytest.mark.usefixtures("setup")
class TestContactUs:

    @allure.title("check contactus form filed")
    @allure.description("Verify that contactus form default are empty")
    def test_contactus_empty_filed(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.contactus_from_empty()

    @allure.title("check submit button")
    @allure.description("Verify that submit button is active and clickable")
    def test_empty_filed_validation(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.check_submit_button()
        contact_us.check_errorMessage("Error: all fields are required\nError: Invalid email address")

    @allure.title("test Error: Invalid email address")
    @allure.description("Verify that the text Error: Invalid email address is displayed on the page")
    def test_fill_form_invalid_email(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.fill_contact_form("test.com")
        contact_us.check_submit_button()
        contact_us.get_error_message_for_invalid_email("Error: Invalid email address")

    @allure.title("Fill in the Email Address field with a valid email")
    @allure.description("Verify that contact-form-thank-you.html is displayed")
    def test_fill_form_valid_email(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.fill_contact_form("test.com@gmail.com")
        contact_us.check_submit_button()
        contact_us.thank_you_message()

    @allure.title("The text Thank You for your Message! ")
    @allure.description("Verify that the text Thank You for your Message! is displayed")
    def test_thank_you_message(self):
        self.test_fill_form_valid_email()
        contact_us = ContactUs(self.driver)
        contact_us.thank_you_message()

    @allure.title("values for all fields are pre-filled")
    @allure.description("Verify that values for all fields are pre-filled")
    def test_fields_are_prefilled(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.fill_contact_form("test.com@gmail.com")
        contact_us.verify_pre_filled_values()


    @allure.title("Reset button is active")
    @allure.description("Verify that the Reset button is active and click on it")
    def test_reset_button(self):
        contact_us = ContactUs(self.driver)
        contact_us.open()
        contact_us.title("WebDriver | Contact Us")
        contact_us.fill_contact_form("test.com@gmail.com")
        contact_us.check_submit_button()
        contact_us.reset_button()

    @allure.title("After Reset field are empty")
    @allure.description("Verify that First Name, Last Name, Email Address and Comments are empty")
    def test_field_are_empty(self):
        self.test_reset_button()
        contact_us = ContactUs(self.driver)
        contact_us.verify_fields_after_reset()


