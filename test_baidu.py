"""
关闭浏览器通知提示
"""
# from selenium import webdriver
# import time
#
# chrome_option_set = webdriver.ChromeOptions()
# chrome_option_set.add_experimental_option("excludeSwitches", ['enable-automation']) # 屏蔽'CHROME正受到组件控制'的提示
#
# prefs = {"":""}
# prefs["credentials_enable_service"] = False
# prefs["profile.password_manager_enabled"] = False
# chrome_option_set.add_experimental_option("prefs", prefs) # 屏蔽'保存密码'提示框
# # 打开浏览器
# browser = webdriver.Chrome(options=chrome_option_set)
# # 输入网址
# browser.get("http://www.baidu.com")
# # 操作地址
# # 关闭浏览器
# time.sleep(2)
# browser.quit()

