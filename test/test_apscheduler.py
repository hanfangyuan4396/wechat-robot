from apscheduler.schedulers.blocking import BlockingScheduler

# 需要定时触发的任务函数
def print_text(text1, text2):
    print(text1, text2)

# 创建scheduler，timezone时区信息可以不设置，默认为系统时区
scheduler = BlockingScheduler(timezone="Asia/Shanghai")
# cron 触发器
# 每天七点半执行
scheduler.add_job(print_text, 'cron', ('cron:', 'good morning'), hour=7, minute=30)
# 整分钟时执行
scheduler.add_job(print_text, 'cron', ('cron:', 'hello world'), minute='*/1')
# interval 触发器
# 每隔一分钟执行一次，从程序开始运行时算起
scheduler.add_job(print_text, 'interval', ('interval:', 'hello world'), minutes=1)
# 开始scheduler start()后面如果还有代码不会被执行，程序在start被阻塞住
scheduler.start()
