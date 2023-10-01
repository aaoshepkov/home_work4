import os

from selene import be, have
from selene.support.shared import browser


def test_demoqa():
    browser.open("https://demoqa.com/automation-practice-form")

    browser.element('#firstName').type('Alex')

    browser.element('#lastName').type('Osh')

    browser.element('#userEmail').type('aaoshepkov@gmail.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('79659944488')

    browser.element('#dateOfBirthInput').click()

    browser.element('.react-datepicker__year-select').type('1979')

    browser.element('.react-datepicker__month-select').type('January')

    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()

    browser.element('#subjectsInput').type('computer science').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('files/jenkins.png'))

    browser.element('#currentAddress').type('Planet Earth')

    browser.element('#react-select-3-input').type('NCR').press_enter()

    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()


def test_google_search_negative():
    # Открытие Google
    browser.open("https://www.google.com")

    # Поиск по запросу "yashaka/selene"
    browser.element('#APjFqb').should(be.blank).type('nvdjsnvkhsbdlkewjfoiahsdukfb').press_enter()

    # Проверка наличия текста на странице
    browser.element('#result-stats').should(have.text("Результатов: примерно 0"))
