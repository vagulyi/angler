import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_guest_should_see_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    cart_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    #cart_button.click()
    assert cart_button, "Should be a basket button"
