import time
import os
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button_css = ".btn-add-to-basket"


def input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


@pytest.mark.incremental
class TestAddToBasketButton:

    def test_find_button_add_to_basket(self, browser):
        browser.get(link)
        button = len(browser.find_elements_by_css_selector(button_css))
        assert button > 0, "Can't find button 'Add to basket':C"

    def test_button_add_to_basket_language(self, browser, language):
        fr = "Ajouter au panier"
        es = "Añadir al carrito"
        ru = "Добавить в корзину"
        gb = "Add to basket"
        browser.get(link)
        # time.sleep(30)
        button_name = browser.find_element_by_css_selector(button_css)
        print(language)
        if language == "fr":
            input_text(fr, button_name.text)
        elif language == "es":
            input_text(es, button_name.text)
        elif language == "gb":
            input_text(gb, button_name.text)
        elif language == "ru":
            input_text(ru, button_name.text)
        else:
            assert "your_expected_result" == button_name.text, f"You entered language '{language}', but in settings only fr,es,ru,gb. Use languages from settins!"
