#encoding:utf-8
from Utils.GetElement import get_element

class SendMailPage(object):

    def __init__(self,driver):
        self.driver = driver

    def write_btn(self):
        element = get_element(self.driver,"id","composebtn")
        return element

    def main_frame(self):
        element = get_element(self.driver,"id","mainFrame")
        return element

    def receiver_box(self):
        element = get_element(self.driver,"xpath",'//input[@class="js_input" and @tabindex="1"]')
        return element

    def subject_box(self):
        element = get_element(self.driver,"id","subject")
        return element

    def sub_frame(self):
        element = get_element(self.driver,"xpath",'//div[@id="QMEditorArea"]//iframe[@class="qmEditorIfrmEditArea"]')
        return element

    def content_box(self):
        element = get_element(self.driver,"xpath","//body")
        return  element


    def send_btn(self):
        element = get_element(self.driver,"xpath",'//a[@name="sendbtn" and @tabindex="5"]')
        return element


