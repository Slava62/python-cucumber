from features.browser import Browser
from features.pages.main_page import MainPage

#Cucumber+Behave+Python+Allure reports
#cd proj root
#behave -f allure_behave.formatter:AllureFormatter -o my_report
#allure serve my_report
#behave --tags="@search_em" -f allure_behave.formatter:AllureFormatter -c -o my_report

def before_all(context):
    context.browser = Browser()
    context.main_page=MainPage()

def after_all(context):
    context.browser.close()
