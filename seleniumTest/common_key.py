from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains #ActionChains模块支持，右键，鼠标悬停，拖拽，双击等动作
driver=webdriver.Chrome()

driver.find_element_by_xpath("").is_selected() #判断单选复选框下拉框是否被选中
print(driver.find_element_by_id('su').size) #打印出页面元素的大小，结果：{'width': 100.0, 'height': 36.0}
a=driver.find_element_by_name('su').text #获取元素上面的文字
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')# 可以通过这个方法，输入任何一个键盘上支持的字符或者快捷键。比如：组合键-全选文字ctrl+a
# 直接清空文字（1）
driver.find_element_by_name('su').clear()
# 全选后退格键删除文字（2）
driver.find_element_by_name('su').send_keys(Keys.CONTROL+'a')
driver.find_element_by_name('su').send_keys(Keys.BACKSPACE)

element=driver.find_element_by_xpath("//*[@id='lg']/img")
actionChains=ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

driver.execute_script("window.alert('这是一个alert弹框');") #执行js

driver.find_element_by_xpath("//*[@href]").get_attribute('href') #获取元素的属性

#进入frame
driver.switch_to.frame('frame1')
# 截图
driver.get_screenshot_as_file("C:\\Users\\pei.lu\\Desktop\\baidu.png") #会在桌面保存一张百度首页的截图，图片后缀是png。
driver.save_screenshot("G://test/01.png")
# 处理网页Alert弹窗,点击弹出页面的确定按钮
driver.switch_to.alert.accept()  #新方法
driver.switch_to_alert().accept()#旧方法废弃

#切换窗口
news_link=driver.find_element_by_xpath("//*[@id='pane_news']/div/ul/li/a")
news_link.click()#点击新链接会出现新窗口
handles=driver.window_handles
for handle in handles:
    if handle!=driver.current_window_handle:
        print('switch to second window',handle)
        driver.close() #关闭第一个窗口，可选操作
        driver.switch_to.window(handle)