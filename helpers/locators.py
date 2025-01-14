from selenium.webdriver.common.by import By

class Locators:
    NAME_FOR_REGISTRATION = (By.XPATH,'(//input[@name="name"])[1]') #Поле для ввода имени на странице регистрации
    EMAIL_FOR_REGISTARTION = (By.XPATH,"(//input[@name='name'])[2]") #Поле для воода email на странице регистрации
    PASSWORD_FOR_REGISTRATION = (By.XPATH,"//input[@name='Пароль']") #Поле для ввода пароля на странице регистрации
    BUTTON_FOR_REGISTRATION = (By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка Зарегистрироваться
    EMAIL_FOR_LOGIN = (By.XPATH,"(//input[@class='text input__textfield text_type_main-default'])[1]") #Поле для воода email на странице входа
    PASSWORD_FOR_LOGIN = (By.XPATH,"(//input[@class='text input__textfield text_type_main-default'])[2]") #Поле для ввода пароля на странице входа
    ERROR_FOR_INCORRECT_PASSWORD = (By.XPATH,"//p[@class='input__error text_type_main-default']") #Ошибка, что пароль неккоретный
    TITLE_FOR_PAGE_LOGIN = (By.XPATH,"//*[text()='Вход']") #Заголовок на странице входа
    BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE = (By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")#Кнока Войти в аккаунт на главной странице
    BUTTON_LOGIN = (By.XPATH,"//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка войти на странице входа
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH,"(//p[@class='AppHeader_header__linkText__3q_va ml-2'])[3]") #Кнопка личный кабинет
    BUTTON_LOGIN_ON_PAGE_LOGIN = (By.XPATH,"(//a[@class='Auth_link__1fOlj'])") #Кнопка войти на странице регистрации