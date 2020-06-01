# 1. 自动化测试概述

## 1.1 软件测试六大模块

### 1.1.1 功能性测试

* ATM机取钱不扣款
* 日期格式不正确
* web页面超链接无法打来
* 手机听音乐时来电不提示
* 地铁公交车刷卡扣款不成功
* 手机app无法正常启动

### 1.1.2 可用性测试（用户体验）

隐性需求：

* 用户习惯
  
  * 针对不同的用户群体，使用习惯
* 行业规范

  - 电商，保险，医疗，金融
* 竞争对手

eg：

* 手机应用程序运行太慢

* 删除数据无二次确认

* 页面布局难看

* 网站经常出现广告

### 1.1.3 性能测试（高并发场景）

* 网页打开速度慢
* 应用程序运行太久占用内存很大
* 春运抢票系统崩溃

### 1.1.4 安全性测试（系统漏洞）

* wifi万能钥匙
* csdn用户数据泄露
* 手机联系人信息被窃取
* 网站被大量用户非法攻击

### 1.1.5 兼容性测试（客户端兼容性）

* 网页IE和Firefox显示效果不一致
* app手机在手机上无法安装
* 应用程序在win10上卡顿

###  1.1.6 可靠性测试（系统是否稳定，容错性，捕获异常能力）

测试流程：

* 计划

* 分析需求

* 设计用例

* 执行用例

* 测试报告

## 1.2 自动化测试价值

自动化测试是把以人为驱动的测试行为转化为机器执行的一种过程

### 1.2.1 自动化测试优势

* 提高测试执行效率，节约时间成本
* 解放人力去做更重要的事（分析需求，设计用例）
* 可重复利用，减少对人的依赖
* 提升客户满意度
* 提升测试团队水平
* 减少兼容性测试工作量
* 有些测试工作必须依赖自动化完成（高并发）

### 1.2.2 自动化测试不足

* 开发自动化测试脚本需要花费较长周期（手工用例2-3倍时间）
* 随着产品迭代，自动化测试脚本也需要更新，时间成本高
* 不同项目自动化脚本重用性低（接口测试）
* 短期项目实施自动化测试价值低
* 自动化测试无法代替手工测试找到产品bug
* 自动化测试开发过程对软件测试团队的技术要求高

## 1.3 手工测试 vs 自动化测试

| 寻找产品缺陷   | 手工测试 | 优于 | 自动化测试 |
| :------------- | -------- | ---- | ---------- |
| 纯技术要求     | 手工测试 | 低于 | 自动化测试 |
| 产品稳定性要求 | 手工测试 | 低于 | 自动化测试 |
| 测试用例高效性 | 手工测试 | 优于 | 自动化测试 |
| 测试人才需求   | 手工测试 | 同于 | 自动化测试 |
| 可替代性       | 手工测试 | 同于 | 自动化测试 |
| 测试项目价值   | 手工测试 | 同于 | 自动化测试 |

## 1.4 自动化测试能力要求

### 1.4.1 软件测试能力要求

* 掌握软件测试流程和方法

* 掌握软件测试用例设计思路

* 有1年软件测试项目经验

### 1.4.2 程序设计能力要求

* java或者python基础
* 数据库使用经验
* 软件系统三层结构及协议（客户端，服务端，数据库）

### 1.4.3 软件架构能力要求

* 理解系统前后端交互过程
* 理解操作系统（手机和电脑）基本原理
* 理解软件系统的三层结构及协议
* 理解项目核心技术架构
* 理解被测产品的需求和业务逻辑  

# 2.selenium环境搭建
## 2.1 selenium安装
```buildoutcfg
pip install selenuim
```
## 2.2 driver下载
```buildoutcfg
chrome下载:
http://npm.taobao.org/mirrors/chromedriver/

geck下载:
https://github.com/mozilla/geckodriver/releases

ie下载:
http://selenium-release.storage.googleapis.com/index.html
```
注意事项：

a. 浏览器驱动和浏览器相对应

b. 浏览器驱动版本和浏览器版本相对应

c. 将下载好的浏览器驱动放置在pyhon安装根目录下

# 3.selenium使用步骤

a. 导入selenium

b. 打开浏览器

c. 输入网址

d. 网址进行操作

e. 关闭浏览器

```python
from selenium import webdriver
import time

# 屏蔽'CHROME正受到组件控制'的提示
chrome_option_set = webdriver.ChromeOptions()
chrome_option_set.add_experimental_option("excludeSwitches", ['enable-automation']) 

prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
chrome_option_set.add_experimental_option("prefs", prefs) # 屏蔽'保存密码'提示框
# 打开浏览器
browser = webdriver.Chrome(options=chrome_option_set)
# 输入网址
browser.get("http://www.baidu.com")
# 操作地址
# 关闭浏览器
time.sleep(2)
browser.quit()
```

