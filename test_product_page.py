from pages.product_page import ProductPage
import pytest


#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.solve_quiz_and_get_code()


def test_name_position(browser):
    page = ProductPage(browser, link)
    page.open()
    name = page.get_product_name()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    assert page.get_name_from_basket() == name, "Name before add to basket and name after unmatch"


def test_price_match(browser):
    page = ProductPage(browser, link)
    page.open()
    price_before = page.get_price_before()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    price_after = page.get_price_after()
    assert price_after == price_before, "Price before add to basket and name after unmatch"
    