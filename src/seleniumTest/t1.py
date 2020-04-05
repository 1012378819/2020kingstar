# coding=utf-8
from    selenium    import  webdriver
from    selenium.common.exceptions  import  TimeoutException
from    selenium.webdriver.support.wait import  WebDriverWait
from    selenium.webdriver  import  ActionChains
import   time

#页面交互
def pageInteraction():
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    # 隐示等待，为了等待充分加载好网址
    driver.implicitly_wait(5)
    write = driver.find_element_by_id("kw")
    write.send_keys("Selenium")
    # 点击
    driver.find_element_by_id('su').click()
    try:
        # 显示等待，其中5的解释：5秒内每隔0.5毫秒扫描1次页面变化，直到指定的元素
        wait = WebDriverWait(driver,5)
        wait.until(lambda   driver: driver.find_element_by_id("content_left"))
        # 打印源代码
        print(driver.page_source)

    except  TimeoutException:
        print("查询元素超时")
    finally:
        time.sleep(3)
        driver.close()

#页面元素拖拽
def elementDragging():
    try:
        driver = webdriver.Firefox()
        url ="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
        driver.get(url)
        driver.implicitly_wait(5)
        # 切换到元素所在的frame
        driver.switch_to.frame("iframeResult")
        # 起点
        start = driver.find_element_by_id("draggable")
        # 终点
        end = driver.find_element_by_id("droppable")

        actions = ActionChains(driver)
        actions.drag_and_drop(start, end)
        # 执行
        actions.perform()
    except Exception:
        print("exception")
    finally:
        driver.close()

#页面切换
def pageSwitching():
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    #获取当前百度界面的窗口句柄
    BD_windows = driver.current_window_handle
    #打印
    print(BD_windows)
    # 隐示等待，为了等待充分加载好网址
    driver.implicitly_wait(5)

    write = driver.find_element_by_id("kw")
    write.send_keys("CSDN")
    # 点击
    driver.find_element_by_id('su').click()
    try:
        #打开一个网页
        driver.find_element_by_link_text(u'CSDN-专业IT技术社区').click()
        # 隐示等待，为了等待充分加载好网址
        driver.implicitly_wait(5)
        #打印所有的窗口
        print(driver.window_handles)
        # 隐示等待，为了等待充分加载好网址
        driver.implicitly_wait(5)
        #窗口切换到第二个网页
        driver.switch_to_window(driver.window_handles[1])
        #点击第二个网页的"写博客"按钮
        driver.find_element_by_link_text(u'写博客').click()
        time.sleep(5)
    except  Exception:
        print("exception")
    finally:
        driver.quit()
if  __name__ == '__main__':
    pageInteraction()
    #pageSwitching()
    #elementDragging()

