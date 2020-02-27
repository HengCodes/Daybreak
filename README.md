## 项目背景

>目前大多数公司存在线上业务监控的需求，现在越来越多前后端分离项目，在产品上线的时候，经常因为api错误导致前台无法正常运行或者服务无法提供给他人导致测试进度延误或者已经上线的api的突然挂掉而无法得知，等到用户反馈的时候，才立马去进行修改。而破晓项目希望可以实现接口线上监控，并且可以在线增加接口，编辑接口，勾选被监控的接口，配置监控的环境信息，执行评率，并且已图表的形式展现出来。

## 主要功能

* 支持常见的http请求，如get，post，put，delete等常见restful api请求方式支持
* 监控任务的创建（如选择那些api需要被监控，执行频率等）
* 通知告警服务（邮件）


## 技术栈

本次练手项目为正式项目的补充，所以统一使用前后端开发模式，采用python+django+vue的技术框架

* 后端开发语 Python 3.8
* web框架 Django 3.x
* Restful 框架：Django restful framework
* 后端管理框架：Django-simpleUI
* 前台开发框架Vue3.x+iview-admin


## UI框架
#### 后台admin界面
![a302aa36c36d90161ee7ce45347aeddd.png](en-resource://database/509:0)

### 前台展示页面

![3d94c500556e68e76947ccc243094883.png](en-resource://database/511:0)
