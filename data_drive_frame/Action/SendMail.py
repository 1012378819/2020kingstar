#encoding:utf-8
import time
from PageObject.SendMailPage import SendMailPage

def send_mail(driver,receiver,subject,content):

    time.sleep(3)
    send_page = SendMailPage(driver)

    #获取写信按钮并点击
    write_btn = send_page.write_btn()
    write_btn.click()

    main_frame = send_page.main_frame()
    driver.switch_to.frame(main_frame)
    time.sleep(1)
    receiver_box = send_page.receiver_box()
    subject_box = send_page.subject_box()

    receiver_box.send_keys(receiver)
    subject_box.send_keys(subject)

    sub_frame = send_page.sub_frame()
    driver.switch_to.frame(sub_frame)

    time.sleep(1)

    content_box = send_page.content_box()
    content_box.send_keys(content)

    driver.switch_to.parent_frame()

    send_btn = send_page.send_btn()
    send_btn.click()

    time.sleep(3)

    driver.refresh()


if __name__ == '__main__':
    from selenium import webdriver
    from Action.Login import login
    driver = webdriver.Chrome(executable_path="d://chromedriver.exe")
    login(driver,"286542822@qq.com","xxxxxxx")
    send_mail(driver,"286542822@qq.com","光荣之路测试开发培训","光荣之路")

