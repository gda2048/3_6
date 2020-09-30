import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_ability_to_add_product_to_the_cart(browser):
    browser.get(link)
    # time.sleep(30)
    buttons = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(buttons) == 1, 'No such element or selector is ambiguous'
