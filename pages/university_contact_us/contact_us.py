import allure
from faker import Faker
from selenium.common import StaleElementReferenceException

from base.page_base import PageBase
from locators.locators import ContactUsLocator


class ContactUs(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify that First Name, Last Name, Email Address and Comments are empty")
    def contactus_from_empty(self):
        # Find the input fields
        first_name_input = self.driver.find_element(*ContactUsLocator.firstName_input)
        last_name_input = self.driver.find_element(*ContactUsLocator.lastName_input)
        email_input = self.driver.find_element(*ContactUsLocator.email_input)
        comment_input = self.driver.find_element(*ContactUsLocator.comment_input)

        # Get the values from the input fields
        first_name_value = first_name_input.get_attribute('value')
        last_name_value = last_name_input.get_attribute('value')
        email_value = email_input.get_attribute('value')
        comment_value = comment_input.get_attribute('value')
        assert first_name_value == '', f"First Name field is not empty. Value: {first_name_value}"
        assert last_name_value == '', f"Last Name field is not empty. Value: {last_name_value}"
        assert email_value == '', f"Email Address field is not empty. Value: {email_value}"
        assert comment_value == '', f"Comments field is not empty. Value: {comment_value}"

    @allure.step("Verify that the Submit button is active and click on it")
    def check_submit_button(self):
        try:
            submit_button = self.driver.find_element(*ContactUsLocator.submitButton)
            assert submit_button.is_enabled(), "Submit button is not enabled"
            submit_button.click()
        except StaleElementReferenceException:
            pass
        assert ("Contact form handler".title())

    @allure.step("Verify that error message")
    def check_errorMessage(self, errorMessage):
        errorMessageForAllFiled = self.driver.find_element(*ContactUsLocator.errorTextForAllFiled)
        assert errorMessageForAllFiled.text == errorMessage, f"Error message for all fields is not as expected: '{errorMessage}', Actual: '{errorMessageForAllFiled.text}'"

    @allure.step("Fill in the First Name, Last Name and Comments fields using the faker library")
    def fill_contact_form(self, email):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        comments = fake.paragraph()
        first_name_field = self.driver.find_element(*ContactUsLocator.firstName_input)
        last_name_field = self.driver.find_element(*ContactUsLocator.lastName_input)
        comments_field = self.driver.find_element(*ContactUsLocator.comment_input)
        email_filed = self.driver.find_element(*ContactUsLocator.email_input)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_filed.send_keys(email)
        comments_field.send_keys(comments)

    @allure.step("Verify  text for Error: Invalid email address")
    def get_error_message_for_invalid_email(self, errorText):
        assert ("Contact form handler".title())
        errorTile = self.driver.find_element(*ContactUsLocator.TileForInvalidEmail)
        assert errorTile.text == errorText, f"Error message for invalid email: '{errorText}', Actual: '{errorTile.text}'"

    @allure.step("Verify that the text Thank You for your Message!")
    def thank_you_message(self):
        message = self.driver.find_element(*ContactUsLocator.ThankYouText)
        assert message.text == "Thank You for your Message!" ,f"Message should display: 'Thank You for your Message!', Actual: '{message.text}' "

    @allure.step("Verify that values for all fields are pre-filled")
    def verify_pre_filled_values(self):
        fields = {
            "first_name": ContactUsLocator.firstName_input,
            "last_name": ContactUsLocator.lastName_input,
            "comments": ContactUsLocator.comment_input,
            "email": ContactUsLocator.email_input
        }
        initial_values = {}
        final_values = {}

        for field_name, locator in fields.items():
            field_element = self.driver.find_element(*locator)
            initial_values[field_name] = field_element.get_attribute("value")

        self.check_submit_button()
        self.driver.back()

        for field_name, locator in fields.items():
            field_element = self.driver.find_element(*locator)
            final_values[field_name] = field_element.get_attribute("value")

        for field_name in fields.keys():
            assert initial_values[field_name] == final_values[field_name], f"{field_name} value is not matching"


    @allure.step("Verify that the Reset button is active and click on it")
    def reset_button(self):
        self.driver.back()
        self.driver.find_element(*ContactUsLocator.ResetButton).click()


    @allure.step("Verify that First Name, Last Name, Email Address and Comments are empty")
    def verify_fields_after_reset(self):

        LOCATORS = {
            "first_name": ContactUsLocator.firstName_input,
            "last_name": ContactUsLocator.lastName_input,
            "comments": ContactUsLocator.comment_input,
            "email": ContactUsLocator.email_input
        }

        for field_name, locator in LOCATORS.items():
            field_element = self.driver.find_element(*locator)
            field_value = field_element.get_attribute("value")
            assert not field_value, f"The {field_name} field is not empty after reset."


