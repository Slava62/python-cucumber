#from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MainPageElements(object):
    MENU_SANDWICH_BUTTON='.header__menu--menu'
    MENU_ITEMS='div.menu__items'
    MENU_CONTENT='div.menu__content'
    MENU_ALL_ITEMS='a.menu__item'
    PAGE_NEWS_TITLE='main h2'
    ITEM_PAGE_TITLE='main h1'

    SEARCH_BUTTON='.header__menu--search'
    SEARCH_FIELD='form input'
    SEARCH_FORM_BUTTON='button'
    SEARCH_RESULT='.search-result'
    SEARCH_RESULT_ITEMS='a h2'
    SEARCH_RESULT_MESSAGE='main h1'

    TIME_TO_WAIT=1000

class MainPage(Browser):
    #Main page actions
    #Wait the element with locator as string
    def drv_wait (self, locator):
        return WebDriverWait(
             self.driver,MainPageElements.TIME_TO_WAIT).until(
                 EC.visibility_of(self.driver.find_element(
                     By.CSS_SELECTOR,locator)))

    #first step for all test
    def navigate_to_main_page(self):
        self.driver.get('http://www.rmpts.ru')
        news_block=self.drv_wait(MainPageElements.PAGE_NEWS_TITLE)
        return news_block.text=='Новости'
    
    #*************steps for menu test common
    #Open menu
    def click_menu_sandwich_button(self):
        self.drv_wait(MainPageElements.MENU_SANDWICH_BUTTON).click()

    #Get the menu blocks count
    def get_menu_blocks_count(self):
        items = self.drv_wait(MainPageElements.MENU_CONTENT).find_elements(By.CSS_SELECTOR,MainPageElements.MENU_ITEMS)
        i=0
        for el in items:
            i=i+1
        return i

    #Catch a glance to menu blocks
    def get_menu_content(self):
        return self.drv_wait(MainPageElements.MENU_CONTENT)

    #*************steps for menu blocks test 
    def select_menu_item(self,index):
        index=int(index) - 1
        WebDriverWait(self.driver,MainPageElements.TIME_TO_WAIT).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
        MainPageElements.MENU_ALL_ITEMS)))[index].click()
    
    #Look through the title of opened page
    def get_item_page_title(self):
        title=self.drv_wait(MainPageElements.ITEM_PAGE_TITLE)
        return title.text

    #*************steps for search test
    def click_search_button(self):
        self.drv_wait(MainPageElements.SEARCH_BUTTON).click()

    #Type text to search in search field
    def set_text_for_search(self,text):
        if text=='History' :
            text='История'
        self.drv_wait(MainPageElements.SEARCH_FIELD).send_keys(text)

    #Click search button in search form
    def click_form_search_button(self):
        self.drv_wait(MainPageElements.SEARCH_FORM_BUTTON).click()

    #Get the items of search result
    def get_search_result(self):
        return self.drv_wait(MainPageElements.SEARCH_RESULT).find_elements_by_css_selector(MainPageElements.SEARCH_RESULT_ITEMS)
    
    #Get the message of search result
    def get_search_result_message(self):
        return self.drv_wait(MainPageElements.SEARCH_RESULT_MESSAGE).text

    #Get the error popup message
    def get_popup_message(self):
        alert=self.driver.switch_to.active_element
        return alert.text#'Заполните это поле.'

     

   