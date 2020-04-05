#encoding:utf-8
from PageObject.LoginPage import LoginPage
import time
def login(driver,username,password):
    url = "https://mail.qq.com"
    driver.get(url)
    #
    login_page = LoginPage(driver)
    login_frame = login_page.frame()
    driver.switch_to.frame(login_frame)

    time.sleep(2)

    btn_login_username_passowrd = login_page.btn_with_username_passwd()
    btn_login_username_passowrd.click()

    username_box = login_page.username()
    password_box = login_page.password()

    username_box.send_keys(username)
    password_box.send_keys(password)

    logint_btn = login_page.btn_login()
    logint_btn.click()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="d://chromedriver.exe")
    login(driver,"286542822@qq.com","xxxxxx")



