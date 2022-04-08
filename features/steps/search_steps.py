from email import message
from behave import *
from nose.tools import assert_true
from nose.tools import assert_equal

@when('user clicks search button')
def step_impl(context):
    context.main_page.click_search_button()
    
@step('the user types "{text}" in a search field')
def step_impl(context, text):
    context.main_page.set_text_for_search(text)

@step('the user presses the search button')
def step_impl(context):
    context.main_page.click_form_search_button()

@then('the second link follows to history block')
def step_impl(context):
    search_result=context.main_page.get_search_result()
    i=0
    for el in search_result:
        if i==1 :
            assert_true(el.text=='История')
        i=i+1    
    assert_true(i==4)

@then('the user should see the message "{text}"')
def step_impl(context,text):
    search_result_message=context.main_page.get_search_result_message()
    if text=='The text is not found':
        text='Найдено 0 результатов.'
    assert_equal(text,search_result_message)

@then('the user should see the popup "{popup_message}"')
def step_impl(context,popup_message):
    msg=context.main_page.get_popup_message()
    assert_equal(popup_message,msg)