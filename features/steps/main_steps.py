from behave import *
from nose.tools import assert_true
from nose.tools import assert_equal

@given('user navigates to main page')
def step_impl(context):
    assert_true(context.main_page.navigate_to_main_page())
    
@when('user clicks main menu sandwich button')
def step_impl(context):
    context.main_page.click_menu_sandwich_button()

@then('the user sees the menu blocks')
def step_impl(context):
    assert_true(context.main_page.get_menu_content().is_displayed)
    
@step('the blocks count is "{number}"')
def step_impl(context, number):
    items_count=context.main_page.get_menu_blocks_count()
    assert_equal(items_count, int(number))

@step('the user selects the menu item with index "{item_index}"')
def step_impl(context,item_index):
    print("Item index :" + item_index)
    context.main_page.select_menu_item(item_index)
    
@then('the page "{item_page}" is opened')
def step_impl(context,item_page):
    text=context.main_page.get_item_page_title()
    print("Expected result (cucumber table): " + "--" + item_page + "--")
    print("Actual result (page title): " + "--" + text + "--")
    assert_true(text==item_page)

    