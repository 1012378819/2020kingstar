#encoding:utf-8
from Utils.GetElement import get_element

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver

    #获取登录页面frame元素对象
    def frame(self):
        element = get_element(self.driver,"id","login_frame")
        return  element

    def btn_with_username_passwd(self):
        element = get_element(self.driver,'id',"switcher_plogin")
        return  element

    def username(self):
        element = get_element(self.driver,"id","u")
        return  element

    def password(self):
        element = get_element(self.driver,"id","p")
        return  element

    def btn_login(self):
        element = get_element(self.driver,"id","login_button")
        return  element



