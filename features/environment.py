from features.browser import Browser
from features.pages.main_page import MainPage

def before_all(context):
    context.browser = Browser()
    context.main_page=MainPage()

def after_all(context):
    context.browser.close()
