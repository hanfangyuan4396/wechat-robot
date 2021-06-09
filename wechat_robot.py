from apscheduler.schedulers.blocking import BlockingScheduler
from wechat_api import wechat_api # 导入是实例化的微信消息接口对象

# 早安消息
def good_morning():
    title = '早安问候'
    text = '早上起床，拥抱太阳，满满的正能量！'
    wechat_api.send_text_message(title, text)

if __name__ == '__main__':
    # 创建scheduler，timezone时区信息可以不设置，默认为系统时区
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # 每天七点半发送问候消息
    scheduler.add_job(good_morning, 'cron', hour=22, minute=34)
    # 开启scheduler
    print('开启任务......')
    scheduler.start()
