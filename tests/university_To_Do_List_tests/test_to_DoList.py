import allure
import pytest

from pages.university_To_Do_List.todolist import ToDoList


@pytest.mark.usefixtures("setup")
class TestToDoList:

    @allure.title("check default to do list")
    @allure.description("To do list is displayed")
    def test_todo_list(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        assert (todolist.add_do_list_displayed())

    @allure.title("Click on plus Icon")
    @allure.description("check add do list is not displayed ")
    def test_todo_list(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        assert todolist.add_do_list_notDisplayed() is False

    @allure.title("Click on to do list of element")
    @allure.description("text becomes strikethrough for every element by clicking on them")
    def test_text_strikethrough(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        todolist.text_strikethrough()

    @allure.title("mouse hover on to do list of element")
    @allure.description("Verify that the delete icon appears when hovering it")
    def test_delete_icon_appears(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        todolist.delete_icon()

    @allure.title(" delete the Go to potion class from the list")
    @allure.description("verify that Go to potion class element isn't displayed in the list")
    def test_delete_icon_appears(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        todolist.delete_List_option()

    @allure.title("Add a new class to do list")
    @allure.description("verify that created a new to do list element is displayed at the end of the list")
    def test_add_newList(self):
        todolist = ToDoList(self.driver)
        todolist.open()
        todolist.title("WebDriver | To Do List")
        todolist.add_new_class_in_TodoList("buy new car")
