## 1 常用函数(https://blog.csdn.net/qingdiao/article/details/81096052)(https://www.cnblogs.com/wxinyu/p/7691225.html)
### 1.1 __setProperty函数
```buildoutcfg
${__setProperty(property name,property value,True/False)}
```
给jmeter属性设置值，默认返回值为空字符串，函数在任何地方调用都有效

property name: 要设置的属性名称，必要属性

property value: 要设置的属性的值，必要属性

True/False: 原值是否要返回，非必要属性，设置为true，返回原始值

作用域：跨线程调用，可以在任何地方调用

注：该函数的参数无需使用双引号引用

### 1.2 JSON Extarctor
json提取器,常用来提取当前请求响应里的值，如登录token
作用域：当前线程组

### 1.3 __P函数
```buildoutcfg
${__P(property name,default value)}
```
为用户在命令行使用属性

不像__property函数那样有可以存值的变量，并且如果没有提供默认值，侧假定默认给1，原因是它对常见的测试变量(如循环、线程数、ramp up等)有效

Property Name：要检索的属性名，必要属性

Default Value：默认值，不填的话会默认设置1，非必要属性

作用域：可跨线程使用


### 1.4 vars函数
```buildoutcfg
vars.put(var, value)
```
设置属性值

var: 变量名称，string类型

value: 变量值，string类型

作用域：当前线程组，必须在beanshell使用

```buildoutcfg
vars.get(var)
```
获取属性值

var: 变量名称，需要使用双引号引用变量名，即`vars.get(“var”)`

value: 变量值，ffstring类型

作用域：当前线程组，必须在beanshell使用

### 1.5 props函数
```buildoutcfg
props.put(var, value)
```
设置属性值

var: 变量名称，string类型

value: 变量值，string类型

作用域：跨线程组调用，必须在beanshell使用

```buildoutcfg
props.get(var)
```
获取属性值

var: 变量名称，需要使用双引号引用变量名，即`props.get(“var”)`

value: 变量值，string类型

作用域：跨线程组调用，必须在beanshell使用

```buildoutcfg
props.remove(var)
```
移除属性值

var: 变量名称，需要使用双引号引用变量名，即`props.remove(“var”)`

value: 变量值，string类型

作用域：跨线程组调用，必须在beanshell使用

### 1.6 _char函数

```buildoutcfg
__char(num1, num2....)
```
把一组数字转换为Unicode
![image](https://img-blog.csdn.net/20180718121601861?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

num: Unicode字符编码（十进制数或者十六进制数）

作用域：当前java请求范围内

### 1.7 __counter函数
```buildoutcfg
__counter(true, output)
```
计数器，支持多线程（可以理解为多用户）

每次调用计数器函数都会产生一个新值，从1开始每次加1

计数器既可以被配置成针对每个虚拟用户是独立的，也可以被配置成所有虚拟用户公用的

如果每个虚拟用户的计数器是独立增长的，那么通常被用于记录测试计划运行了多少遍

全局计数器通常被用于记录发送了多少次请求

计数器使用一个整数值来记录，允许的最大值为2,147,483,647


线程组设置为2个用户，循环两次${__counter(true,output)}，线程分别计数，互不干扰

![image](https://img-blog.csdn.net/20180718121954918?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

线程组设置为2个用户，循环两次${__counter(false,output)}，线程合并起来一起计数

![image](https://img-blog.csdn.net/20180718122232421?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

true：线程之间互不干扰(每个虚拟用户的计数器保持独立)

false: 合并计数(全局计数器)

output: 重用计数器函数创建值的引用名

作用域: 可全局可线程组内

### 1.8 __CSVRead函数

从文件中读取指定列的值

当对某个文件进行第一次读取时，文件将被打开并读取到一个内部数组中

如果在读取过程中找到了空行，函数就认为到达文件末尾了，即允许拖尾注释

每一个线程都有独立的内部指针指向文件数组中的当前行

当某个线程第一次引用文件时，函数会为线程在数组中分配下一个空闲

任何一个线程访问的文件行，都与其他线程不同（除非线程数大于数组包含的行数）

默认情况下，函数会在遇到的每一个逗号处断行

如果希望在输入的列中使用逗号，那么需要换一个分隔符（通过设置属性csvread.delimiter来实现），且该符号没有在CSV文件的任何列中出现

a.读取固定值，无论循环多少次，值是不变的(${__CSVRead(C:\Users\wzd\Desktop\test.txt,0)})

![image](https://img-blog.csdn.net/20180718122800380?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

b.读取动态值, ${__CSVRead(C:\Users\wzd\Desktop\test.txt,next)}(读取不成功)

![image](https://img-blog.csdn.net/20180718123021229?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

c.文件取别名(${__CSVRead(C:\Users\29446\Desktop\test.txt,*file)})(${__CSVRead(*file,0)})

![image](https://img-blog.csdn.net/20180718123313834?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 1.9 __FileToString函数

用来读取整个文件, 每次对该函数的调用，都会读取整个文件

如果在打开或者读取文件时发生错误，那么函数就会返回字符串"**ERR**"

![image](https://img-blog.csdn.net/20180718123917837?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

```buildoutcfg
__FileToString(文件名, 文件编码方式, 变量名)
```
文件名: 包含路径的文件名（路径可以是相对于JMeter启动目录的相对路径）

文件编码方式: 如果不采用平台默认的编码方式, 读取文件需要用到的文件编码方式

如果没有指明就使用平台默认的编码方式

变量名: 引用名（refName）用于重用函数创建的值

### 1.10 __Random函数

返回指定最大值和最小值之间的随机数

![image](https://img-blog.csdn.net/20180718124214455?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpbmdkaWFv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

```buildoutcfg
__Random(最小值, 最大值, 变量名)
```

最小值: 最小数值

最大值: 最大数值

变量名: 重用函数计算值的引用名
