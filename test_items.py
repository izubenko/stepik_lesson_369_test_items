
#pytest -v --tb=line --reruns 1 --browser_name=chrome test_items.py

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_basket(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector('#add_to_basket_form > button')
    #correct_text = browser.find_element_by_class_name('smart-hints__hint').text # считываем текст и записываем его в переменную
    #assert "Correct!" == correct_text, f"Got: '{correct_text}', but should be 'Correct!'"