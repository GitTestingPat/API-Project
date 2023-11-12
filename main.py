from selenium.webdriver.common.by import By
from selenium import webdriver

class ShadyMeadowsPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores para reservación
        self.book_room_button_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div/div[3]/button"
        self.firstname_input_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div[2]/div[3]/div[1]/input"
        self.lastname_input_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div[2]/div[3]/div[2]/input"
        self.email_input_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div[2]/div[3]/div[3]/input"
        self.phone_input_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div[2]/div[3]/div[4]/input"
        self.book_button_xpath = "//*[@id='root']/div[2]/div/div[4]/div/div[2]/div[3]/button[2]"

        # Localizadores para solicitud de información
        self.name_input_id = "name"
        self.email_input_id = "email"
        self.phone_input_id = "phone"
        self.subject_input_id = "subject"
        self.message_input_id = "description"
        self.submit_button_id = "submitContact"

    def open(self):
        self.driver.get(BASE_URL)

    def make_reservation(self, firstname, lastname, email, phone):
        self.driver.find_element(By.XPATH, self.book_room_button_xpath).click()
        self.driver.find_element(By.XPATH, self.firstname_input_xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH, self.lastname_input_xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.phone_input_xpath).send_keys(phone)
        self.driver.find_element(By.XPATH, self.book_button_xpath).click()

    def make_request(self, name, email, phone, subject, message):
        self.driver.find_element(By.ID, self.name_input_id).send_keys(name)
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)
        self.driver.find_element(By.ID, self.phone_input_id).send_keys(phone)
        self.driver.find_element(By.ID, self.subject_input_id).send_keys(subject)
        self.driver.find_element(By.ID, self.message_input_id).send_keys(message)
        self.driver.find_element(By.ID, self.submit_button_id).click()
