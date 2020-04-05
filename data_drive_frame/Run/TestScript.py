#encoding:utf-8
from selenium import  webdriver
from Action.Login import login
from Action.SendMail import send_mail
from Utils.ParseExcel import ParseExcel

def main():
    driver = webdriver.Chrome(executable_path="d://chromedriver.exe")
    pe = ParseExcel(r"E:\test\data_drive_frame\TestData\测试数据.xlsx")
    #先获取所有的登录数据
    login_rows = pe.get_all_rows()
    for row in login_rows[1:]:
        username = row[1].value
        password = row[2].value
        data_sheet = row[3].value
        is_execute = row[4].value
        print(username,password,data_sheet)
        if is_execute.lower() == "y":
            login(driver,username,password)
            pe.set_sheet_by_name(data_sheet)
            #取发邮件数据
            data_rows = pe.get_all_rows()
            for data_row in data_rows[1:]:
                receiver = data_row[1].value
                subject = data_row[2].value
                content = data_row[3].value
                print(receiver,subject,content)
                send_mail(driver,receiver,subject,content)

    driver.quit()


if __name__ == '__main__':
    main()

