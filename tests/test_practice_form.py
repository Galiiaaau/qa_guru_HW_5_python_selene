from selene import browser, have, be, by
import os


def test_fill_out_the_form():

    browser.open("/automation-practice-form")

    # Filling out the form
    browser.element("#firstName").should(be.blank).type("Galiia")
    browser.element("#lastName").should(be.blank).type("Uzbekova")
    browser.element("#userEmail").should(be.blank).type("galiiauzbekova@gmail.com")
    browser.element("#gender-radio-2").double_click()
    browser.element("#userNumber").should(be.blank).type("8937365074")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").click().element(by.text("1994")).click()
    browser.element(".react-datepicker__day--018").click()
    browser.element("#subjectsInput").type("English").press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("pics/this-is-fine.png"))
    browser.element("#currentAddress").should(be.blank).type("Moscow")
    browser.element("#react-select-3-input").should(be.blank).type("NCR").press_enter()
    browser.element("#react-select-4-input").should(be.blank).type("Delhi").press_enter()
    browser.element("#submit").double_click()

    # Check if the form was submitted
    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    # Check if the results are correct
    browser.element('.table').should(have.text("Galiia Uzbekova"))
    browser.element('.table').should(have.text("galiiauzbekova@gmail.com"))
    browser.element('.table').should(have.text("Female"))
    browser.element('.table').should(have.text("8937365074"))
    browser.element('.table').should(have.text("18 February,1994"))
    browser.element('.table').should(have.text("English"))
    browser.element('.table').should(have.text("Reading"))
    browser.element('.table').should(have.text("this-is-fine.png"))
    browser.element('.table').should(have.text("Moscow"))
    browser.element('.table').should(have.text("NCR Delhi"))
