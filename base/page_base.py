import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    @allure.step("Verify page title")
    def title(self, title):
        titleValue = self.driver.title
        assert titleValue == title, f"Error:'{titleValue}' is not matched with '{title}'"