import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler

# 企业id、key
CORP_ID = 'xxx' # 更换为你的企业id
CORP_SECRET = 'xxx' # 更换为你的应用secret
AGENT_ID = 1000002 #更换为你的应用id，注意是数字类型，不是字符串

# 获取token
def get_token():
    token_api = (
                    'https://qyapi.weixin.qq.com/cgi-bin/gettoken?' +
                    f'corpid={CORP_ID}&corpsecret={CORP_SECRET}' 
                )
    response = requests.get(token_api)
    print(response.json())
    return response.json()['access_token']

# 发送文本消息
def send_text_message(content, touser):
    data = json.dumps({
        "touser" : touser,
        "msgtype" : "text",
        "agentid" : AGENT_ID,
        "text" : {
            "content" : content
        },
        "safe":0
    })
    send_api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?' + f'access_token={get_token()}'
    res = requests.post(send_api, data=data).json()
    print(res)

if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # 整分钟时刻发送消息
    scheduler.add_job(send_text_message, 'cron', ('hello world', '@all'), minute="*/1")
    scheduler.start()
