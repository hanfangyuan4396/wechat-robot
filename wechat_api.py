import requests
import json

# 企业id、key
CORP_ID = 'xxx' # 更换为你的企业id
CORP_SECRET = 'xxx' # 更换为你的应用secret
AGENT_ID = 1000002 #更换为你的应用id，注意是数字类型，不是字符串

# 微信消息接口类
class WeChatAPI():
    # 接口类的构造函数，需要企业id以及应用的secret
    def __init__(self, corp_id, corp_secret):
        self.corp_id = corp_id
        self.corp_secret = corp_secret
        self.update_token()

    # token请求函数，根据企业id以及应用secret请求token
    def get_token(self):
        # token获取的api
        token_api = (
                        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?' +
                        f'corpid={self.corp_id}&corpsecret={self.corp_secret}'
                    )
        # 设置10s的超时限制，无响应则打印错误信息
        try:
            response = requests.get(token_api, timeout=10)
        except:
            print('请求超时，无法获取access_token')
            return 'error'
        return response.json()['access_token']

    # token更新函数，返回的token其实是有有效期的，在token过期后要更新token，
    # 我们在得到token后要及时保存，避免频繁重复请求token，微信对token的请求频率也是有限制的
    def update_token(self):
        self.access_token = self.get_token()
        # 获取新的token后，放入消息发送的api中
        self.send_api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?' + f'access_token={self.access_token}'
    
    # 文本消息发送函数，传入要发送的文本消息标题，正文; 应用id以及推送的用户有默认值，需要时可以传入参数
    def send_text_message(self, title, text, agent_id=AGENT_ID, touser="@all"):
        # 消息体字典转换为json字符串
        data = json.dumps({
            "touser" : touser,
            "msgtype" : "text",
            "agentid" : agent_id,
            "text" : {
                # 文本消息可以设置一个标题还有正文，这样阅读更清晰
                "content" : title + '\n\n' + text
            },
            "safe":0
        })
        # 设置10s的超时限制，无响应则打印错误信息
        try:
            response = requests.post(self.send_api, data=data, timeout=10).json()
        except:
            print('请求超时，无法发送消息')
            return
        # 企业微信文档中介绍了42001，40014这两个错误代码都跟token有关，需要更新token，再次发送消息
        # 更新token，重新发送消息
        if response['errcode']==42001 or response['errcode']==40014:
            self.update_token()
            self.send_text_message(title, text, agent_id=agent_id, touser=touser)
        # 发送成功
        elif response['errcode'] == 0:
            print(title, '发送成功')
        # 其他错误
        else:
            print('发送失败')
            print('data: ', data)
            print('response: ', response)
            print('token: ', self.access_token)

# 实例化微信消息接口对象，供其他模块直接使用
wechat_api = WeChatAPI(CORP_ID, CORP_SECRET)
