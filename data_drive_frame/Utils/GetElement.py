#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#获取页面元素
def get_element(driver,locate_type,locate_expression):
    try:
        element = WebDriverWait(driver,60,0.2).until(
            lambda x : x.find_element(by = locate_type,value=locate_expression))
        return  element
    except Exception as e:
        raise  e




