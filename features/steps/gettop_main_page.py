from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open GetTop page')
def open_gettop(context):
    context.app.main_page.open_main_page()


@when('Hover over a product')
def hover_over_product(context):
    context.app.main_page.hover_image()


@when('Click on Quick View')
def quick_view(context):
    context.app.main_page.quick_view()


@when('Add product to cart')
def product_to_cart(context):
    context.app.main_page.add_to_cart()


@when('Click on a product')
def click_on_a_product(context):
    context.app.main_page.click_product()


@when('Click on left arrow {number} times')
def click_left_arrow(context, number):
    for i in range(int(number)):
        context.app.main_page.click_left_arrow()


@then('Click on right arrow {number} times')
def click_left_arrow(context, number):
    for i in range(int(number)):
        context.app.main_page.click_right_arrow()


@then('Close Quick View on the right side corner')
def close_quick_view(context):
    context.app.main_page.close_quick_view()


@then('verify product is in cart')
def verify_product_in_cart(context):
    context.app.main_page.verify_product_in_cart()

