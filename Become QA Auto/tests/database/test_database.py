import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db=Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0]=='Maydan Nezalezhnosti 1'
    assert user[0][1]=='Kyiv'
    assert user[0][2]=='3127'
    assert user[0][3]=='Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 35)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0]==35


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(3, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(3)

    assert water_qnt[0][0]==30

@pytest.mark.database_info
def test_get_info():
    db = Database()
    database=db.get_info_from_database()
    print (database)

@pytest.mark.database_info
def test_get_info_from_table():
    db = Database()
    table=db.get_info_from_table('products')
    print (table)

@pytest.mark.database_info
def test_get_info_from_column():
    db= Database()
    column=db.get_info_from_column('products')
    print(column)


