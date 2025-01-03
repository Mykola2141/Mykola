import pytest



@pytest.mark.ui_np
def test_check_find_office_address(page_object):
    #відкриваємо сторінку 'https://novaposhta.ua'
    page_object.go_to()

    #шукаємо поле пошуку і вводимо номер накладної
    page_object.try_find_cargo("59001227272105")

    #первіряємо, що назва сторінки така,яку ми очікуємо
    assert page_object.check_title("Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН")