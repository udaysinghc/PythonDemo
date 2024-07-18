from selenium.webdriver.common.by import By


class        ToDoListLocator:
    addNewTodoList = (By.CSS_SELECTOR, "input[type='text']")
    plusButton = (By.ID, "plus-icon")
    addNewTodoHidden = (By.CSS_SELECTOR, "input[type='text'][placeholder='Add new todo'][style*='display: none']")
    listOption = (By.CSS_SELECTOR, "ul li")
    listOptionSpan = (By.XPATH, "//div[@id='container']//ul//li//text()")
    strikeList = (By.CSS_SELECTOR, "li[class*='completed']")
    trashButton = (By.CSS_SELECTOR, "[class*='fa fa-trash']")


class ContactUsLocator:
    firstName_input = (By.NAME, "first_name")
    lastName_input = (By.NAME, "last_name")
    email_input = (By.NAME, "email")
    comment_input = (By.NAME, "message")
    restButton = (By.CSS_SELECTOR, "[value='RESET']")
    submitButton = (By.CSS_SELECTOR, "[value='SUBMIT']")
    errorTextForAllFiled = (By.XPATH, "(//*[contains(.,'all')])[2]")
    TileForInvalidEmail = (By.XPATH, "//body[contains(.,'Error')]")
    ThankYouText = (By.CSS_SELECTOR,"div h1")
    ResetButton = (By.XPATH,"//input[@value='RESET']")


class FileUpload:
    file_type = (By.XPATH,"//input[@type='file']")
    submit_button = (By.ID,"submit-button")
