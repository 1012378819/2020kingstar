from appium import webdriver
import time

#1、安卓设备信息
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '810EBM42YU9V'
desired_caps['appPackage'] = 'com.lemon.lemonban'
desired_caps['appActivity'] = 'com.lemon.lemonban.WelcomeActivity'

#2、启动appium
#3、与appiume服务器连接上。告诉appium要操作哪个设备上的哪个应用程序
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.implicitly_wait(30)

#点击全程班链接
qcb_ele = driver.find_element_by_xpath('//android.widget.TextView[@text=\"全程班\"]')
qcb_ele.click()

#打印当前的上下文
time.sleep(5)
contexts = driver.contexts
print(contexts)

#切换到webview
view_context = 'WEBVIEW_com.lemon.lemonban'
driver.switch_to.context(view_context)
time.sleep(5)
print(driver.current_context)

#点击收藏按钮
fav_button_id = "js-bottom-fav"
driver.find_element_by_id(fav_button_id).click()






