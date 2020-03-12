import time
import os
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#def test_input_text(expected_result, actual_result):
#    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
 
def test_button_add_to_basket_language(browser):
    browser.get(link)
    time.sleep(30)
    e = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert "Ajouter au panier" == e.text,f"expected Ajouter au panier, got {e.text}"
    