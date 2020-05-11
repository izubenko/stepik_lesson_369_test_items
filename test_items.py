import time
#pytest -v --tb=line --reruns 1 --browser_name=chrome test_items.py

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(30)
    browser.find_element_by_css_selector('.btn-add-to-basket')