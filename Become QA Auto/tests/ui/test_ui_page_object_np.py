from modules.ui.page_objects.np_search import NPSearch
import pytest


@pytest.mark.ui_np
def test_check_find_office_address():
    #створення об'єкту сторінки
    np_search=NPSearch()

    #відкриваємо сторінку 'https://novaposhta.ua'
    np_search.go_to()

    #виконуємо спробу увійти в систему Github
    np_search.try_find_cargo("59001227272105")

    #первіряємо, що назва сторінки така,яку ми очікуємо
    assert np_search.check_title("Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН")
    
    #закриваємо браузер
    np_search.close()