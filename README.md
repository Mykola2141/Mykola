Фреймворк називається "Become QA Auto"
Фреймворк створений для автоматизації тестування веб-додатків, API та баз даних.
Цей фреймворк призначений для спрощення процесу автоматизації тестування веб-додатків, включаючи UI, API та бази даних. 
Він побудований з використанням таких потужних інструментів, як Selenium, pytest та інші, що дозволяє створювати надійні та ефективні тести. 
Фреймворк підтримує Page Object Model для UI-тестів, що сприяє кращій організації та підтримці тестового коду.

Основні характеристики
*   Автоматизація UI-тестів з використанням Page Object Model (POM),  розробленого для браузера Chrome.Версія 131.0.6778.205(інші браузери в планах)
*   Тестування API, включаючи специфічні тести для GitHub API.
*   Тестування баз даних.
*   Модульна структура, що полегшує розширення та підтримку.
*   Гнучка конфігурація.
*   Використання pytest для запуску та організації тестів.

Для запуску тестів використовуйте команду:

Bash
pytest -m (marker_name)

Структура проєкту

config/: Файли конфігурації.

modules/: Основні модулі фреймворку.

api_clients/: Клієнти для API.

common/: Загальні утиліти.

database.py: Робота з базою даних.

ui_page_objects/: Page objects для UI-тестів.

tests/: Тестові скрипти.

api/: API-тести.

database/: Тести бази даних.

ui/: UI-тести.

become_qa_auto.db: Файл бази даних SQLite.

conftest.py: Файл з фікстурами pytest, що використовуються в тестах.

pytest.ini: Файл конфігурації pytest, що містить визначення маркерів для тестів.

requirements.txt: Файл в якому перелічені залежності,які використовуються в проекті.

Подальший розвиток

Планую надалі розвивати цей фреймворк з часом, додавати підтримку нових браузерів, або інтеграцію з іншими інструментами.

Для клонування репозиторію скористайтесь наступними посиланнями:

HTTPS:https://github.com/Mykola2141/Mykola.git
SSH:git@github.com:Mykola2141/Mykola.git

Для встановлення та використання фреймворку необхідно мати:

*   Python 3.8 або новішої версії.
*   Встановлений веб-браузер Google Chrome.


The framework is called "Become QA Auto" The framework is designed to automate the testing of web applications, APIs, and databases. This framework is designed to accelerate the process of automating the testing of web applications, including UI, APIs, and databases. It is built using powerful tools such as Selenium, pytest, and others, which allows you to create reliable and efficient tests. The framework supports the Page Object Model for UI tests, contributing to better organization and maintenance of test code.

Key features

Automate UI tests using the Page Object Model (POM) developed for the Chrome browser. Version 131.0.6778.205 (other browsers are planned)
API testing, including special tests for GitHub API.
Database testing.
Modular structure, making it easy to extend and maintain.
Flexible configuration.
Use pytest to run and organize tests.
To run the tests, use the command:

Bash pytest -m (marker_name)

Project structure

config/: Configuration files. modules/: Core framework modules. api_clients/: API clients. general/: General utilities. database.py: Database operations. ui_page_objects/: Page objects for UI tests. tests/: Test scripts. api/: API tests. database/: Database tests. ui/: UI tests. become_qa_auto.db: SQLite database file. conftest.py: File with pytest fixtures used in tests. pytest.ini: Pytest configuration file containing marker definitions for tests. requirements.txt: File listing relationships used in the project.

Additional development plan to further develop this framework over time, adding support for new browsers or integration with other tools.

To install and use the framework, you must have:

Python 3.8 or later.
The Google Chrome web browser is installed.
