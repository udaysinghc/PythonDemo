import time

import allure
from selenium.webdriver import ActionChains, Keys

from base.page_base import PageBase
from locators.locators import ToDoListLocator


class ToDoList(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("verify add new todo is displayed by default")
    def add_do_list_displayed(self):
        return self.driver.find_element(*ToDoListLocator.addNewTodoList).is_displayed()

    @allure.step("verify click on plus button then Add new todo is not displayed")
    def add_do_list_notDisplayed(self):
        self.driver.find_element(*ToDoListLocator.plusButton).click()
        time.sleep(0.5)
        return self.driver.find_element(*ToDoListLocator.addNewTodoHidden).is_displayed()

    @allure.step("Verify text becomes strikethrough for every element by clicking on them")
    def text_strikethrough(self):
        elements = self.driver.find_elements(*ToDoListLocator.listOption)
        for element in elements:
            element.click()
            time.sleep(0.3)
        strikeCompleted = self.driver.find_elements(*ToDoListLocator.strikeList)
        for element in strikeCompleted:
            assert (element.is_displayed())

    @allure.step("Verify that the delete icon appears when hovering to Go to potion class the list")
    def delete_icon(self):
        elements = self.driver.find_elements(*ToDoListLocator.listOption)
        for element in elements:
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(0.3)
            self.driver.find_element(*ToDoListLocator.trashButton).is_displayed()

    @allure.step("Click on the delete icon and verify Go to potion class isn't displayed in the list")
    def delete_List_option(self):
        elements = self.driver.find_elements(*ToDoListLocator.listOption)
        for element in elements:
            ActionChains(self.driver).move_to_element(element).perform()
            element_text = element.text
            if element_text == "Go to potion class":
                print("textlist" + element_text)
                self.driver.find_element(*ToDoListLocator.trashButton).click()
                time.sleep(1)
                assert element_text != " Go to potion class"

    @allure.step("Click on the delete icon and verify Go to potion class isn't displayed in the list")
    def add_new_class_in_TodoList(self, nameOfList):
        self.driver.find_element(*ToDoListLocator.addNewTodoList).send_keys()
        input_field = self.driver.find_element(*ToDoListLocator.addNewTodoList)
        input_field.send_keys(nameOfList)
        input_field.send_keys(Keys.ENTER)
        elements = self.driver.find_elements(*ToDoListLocator.listOption)
        for element in elements:
            ActionChains(self.driver).move_to_element(element).perform()
            element_text = element.text
            if element_text == nameOfList:
                assert element_text == nameOfList
