# wechat-robot
## 简介
wechat-robot是一个可以给微信推送消息的项目，使用该项目可以自己搭建一个微信机器人，实现日程提醒、每日天气、自动聊天等功能。本项目的博客介绍[从零搭建微信机器人](https://blog.csdn.net/weixin_44387339/article/details/117346190)

## 运行方式
开发时所用python版本 3.6.13

建议使用conda创建python虚拟环境，conda使用方式可以参考博客[miniconda安装与使用](https://blog.csdn.net/weixin_44387339/article/details/109171325)
```
git clone https://github.com/hanfangyuan4396/wechat-robot.git
cd wechat-robot
conda create --name wechat_robot python=3.6
conda activate wechat_robot
pip install -r requirements.txt
nohup python wechat_robot.py &
```