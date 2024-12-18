from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NPSearch(BasePage):
    URL='https://novaposhta.ua'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(NPSearch.URL)

    def try_find_cargo(self, searching_cargo_number):
        #Знаходимо поле для пошуку накладної на вантаж
        find_cargo=self.driver.find_element(By.ID, "cargo_number")

        #вводимо номер накладної в поле пошуку "1234567891011"
        find_cargo.send_keys(searching_cargo_number)

        #знаходимо кнопку "відстежити"
        btn_element=self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div/div[2]/form/input[2]")

        #емулюємо клік лівою кнопкою мишки
        btn_element.click()

    #перевіряємо очікуваний заголовок сторінки "novaposhta.ua"
    def check_title(self, expected_title):
        return self.driver.title==expected_title