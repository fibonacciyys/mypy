# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:59:32 2019

@author: ReoNa
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AutoSign(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.mode_list = [By.LINK_TEXT,By.ID,By.CLASS_NAME,By.XPATH,By.PARTIAL_LINK_TEXT]
        self.url_list = []
        
    def openUrl(self,url):
        self.driver.get(url)
        
    def press_enter(self,element):
        element.sent_key(Keys.RETURN)
        
    def getBy_click(self,mode,string,is_click=1):
        '''
        mode:0,link_text;1,ID;2,class;3,xpath;4,partial_link_text
        '''
        try:
            element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((self.mode_list[mode],string))
                        )
            if is_click:
                element.click()
        except:
            print('ERROR!')
#            self.driver.minimize_window()
        
    def update_old_handle(self):
        self.old_handle = self.driver.window_handles
        
    def change2blank(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle not in self.old_handle:
                self.driver.switch_to.window(handle)
        self.update_old_handle()
    
    def sw2frame(self):
        try:
            new_frame = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID,'ptlogin_iframe'))
                        )
            self.driver.switch_to.frame(new_frame)
        except:
            print('ERROR!')
            self.driver.minimize_window()
            
    def back2memberPage(self):
        self.driver.close()
        self.driver.switch_to.window(self.member_page)
    
    def unitSign(self):
#        self.driver.refresh()
        time.sleep(5)
        self.getBy_click(4,'签到')
#        self.driver.find_element_by_partial_link_text('签到').click()
        
    def running(self):
        self.openUrl('https://weibo.com/login.php')
#        self.small_size = self.driver.get_window_size()
        self.driver.maximize_window()
        self.update_old_handle()
        self.getBy_click(0,'登录')
        self.getBy_click(0,'使用QQ直接登录')
        self.change2blank()
        self.sw2frame()
        self.getBy_click(2,'face')
        self.getBy_click(2,'ficon_setup')
        self.change2blank()
        self.getBy_click(3,'//ul[@class="lev2_list"]/li[3]/a')
        self.driver.refresh()  # 去除iframe的影响呱
        self.getBy_click(2,'member_ul',0)
        self.member_page = self.driver.current_window_handle
#        for handle in self.driver.window_handles:
#            try:
#                self.driver.switch_to.window.handle
#                ul = self.driver.find_element_by_class_name('member_ul')
#                self.member_page = self.driver.current_window_handle
#                break
#            except:
#                print('NOT IT')
        ul = self.driver.find_element_by_class_name('member_ul')
        members = ul.find_elements_by_class_name('S_txt1')
        for el in members:
            self.url_list.append(el.get_attribute('href'))
#        print(self.url_list)
        self.url_list = list(filter(None,self.url_list))
        self.driver.execute_script('window.open("https://www.baidu.com");')
        self.change2blank()
        for i in self.url_list:
            self.driver.get(i)
            self.unitSign()
#            self.back2memberPage()
#        self.driver.set_window_size(self.small_size.width,self.small_size.height)
        print('Finish!')

def getBy_click(driver,mode,string,is_click=1):
    '''
    mode:1,link_text;2,ID;3,class;4,xpath;
    '''
    mode_list = [By.LINK_TEXT,By.ID,By.CLASS_NAME,By.XPATH]
    try:
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((mode_list[mode],string))
                    )
        if is_click:
            element.click()
    except:
        print('ERROR!')

def print_handles(driver):
    print('current:',driver.current_window_handle)
    print(driver.window_handles)

def test():
    driver = webdriver.Chrome()
#    temp = quote('新浪微博超话')
#    driver.get('https://www.baidu.com/s?wd=' + temp)
    driver.get('http://weibo.com/login.php')
    driver.maximize_window()
#    log_windows = driver.current_window_handle
#    log_in = driver.find_element_by_link_text('登录')
#    log_in.click()
    getBy_click(driver,0,'登录')
#    qq_log = driver.find_element_by_link_text('使用QQ直接登录')
#    qq_log.click()
    print('wb_click')
    print_handles(driver)
    getBy_click(driver,0,'使用QQ直接登录')
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[-1])
    print_handles(driver)
    driver.switch_to.frame(driver.find_element_by_id('ptlogin_iframe'))
#    new_window = driver.current_window_handle
#    my_img = driver.find_element_by_class_name('face')
#    my_img.click()
    print('qq_click')
    print_handles(driver)
    getBy_click(driver,2,'face')
    print_handles(driver)
    print('ficon_click')
    print_handles(driver)
    getBy_click(driver,2,'ficon_setup')
    all_handles = driver.window_handles
    driver.switch_to.window(all_handles[-1])
    print_handles(driver)
    print('focus_click')
    print_handles(driver)
    getBy_click(driver,3,'//ul[@class="lev2_list"]/li[3]/a')
    print_handles(driver)
    print('refresh')
    print_handles(driver)
    driver.refresh()
    print_handles(driver)
    getBy_click(driver,2,'member_ul',0)
#    members = driver.find_elements_by_class_name('member_ul')
    
    
    
if __name__ == '__main__':
    sign = AutoSign()
    sign.running()
#    test()
    
    
    
    
    
    
    
    
    