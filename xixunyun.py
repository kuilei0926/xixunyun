# coding:utf-8
from urllib import request
from urllib import parse
import json
import time
import sys
import os
import base64
import rsa

sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
print(longitude)
print(latitude)
# 关于如何获取坐标
# 例如[0.123456,0.123456]，先经度后纬度，可以去 https://lbs.amap.com/console/show/picker 高德取坐标，直接把结果复制到[]里即可
# 每家坐标拾取器标准不同，本脚本采用XY轴坐标格式。例如北京[116.000000,40.000000]
class HandleSign:
    # 定义服务器公钥, 往往可以存放在公钥文件中
    server_pub = """
        -----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
        O3F7gs+7bzrgPsMl29LemonPYvIG8C604CprLittlenJpnhWu2lGirlWZyLq6sBr
        tuPorOc42+gInFfyhJAwdZB6Sqlove7bW+jNe5youDtU7very6Gx+muchGo8Dg+S
        kKlZFc8Br7SHtbL2tQIDAQAB
        -----END PUBLIC KEY-----
        """

    @classmethod
    def to_encrypt(cls, msg, pub_key=None):
        """
        非对称加密
        :param msg: 待加密字符串或者字节
        :param pub_key: 公钥
        :return: base64密文字符串
        """
        if isinstance(msg, str):            # 如果msg为字符串, 则转化为字节类型
            msg = msg.encode('utf-8')
        elif isinstance(msg, bytes):        # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('msg必须为字符串或者字节类型!')

        if not pub_key:                     # 如果pub_key为空, 则使用全局公钥
            pub_key = cls.server_pub.encode("utf-8")
        elif isinstance(pub_key, str):      # 如果pub_key为字符串, 则转化为字节类型
            pub_key = pub_key.encode('utf-8')
        elif isinstance(pub_key, bytes):    # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('pub_key必须为None、字符串或者字节类型!')

        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象

        cryto_msg = rsa.encrypt(msg, public_key_obj)  # 生成加密文本
        cipher_base64 = base64.b64encode(cryto_msg)   # 将加密文本转化为 base64 编码

        return cipher_base64.decode()   # 将字节类型的 base64 编码转化为字符串类型

if __name__ == '__main__':
    # 调用to_encrypt类方法来进行加密
    longitudersa = HandleSign.to_encrypt(longitude)
    latitudersa = HandleSign.to_encrypt(latitude)
    print(longitudersa)
    print(latitudersa)
# 配置开始
user = os.environ["USER"]
account = user.split( )[0] # 账号1
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID

if account=="" or account=="" or school_id=="" or sign_gps=="":
    msg += '诶呀？好像你还没有配置好账号信息和签到设置呢！(>_<)\n'
    exit(1)
    
# 关于学校ID
# 可以前往 https://api.xixunyun.com/login/schoolmap 查询，比如茂名职业技术学院ID为924（截止20201213）
remark_name = "假期" # 签到类型（现已只需填写汉字类型）
# 关于签到类型
# 请注意此类型可能会变更
# 0：上班 1：外出 2：假期 3：请假 4：轮岗 5：回校 6：外宿 7：在家 8：下班 9：学习 10：毕业设计 11：补签
comment = "" # 签到说明（如需换行请使用\\n，如需输入"\"斜杠请使用"\\"，以上仅为猜测，作者没用过）
no_wait = 0 # 是否不等待直接完成（将取消获取真实位置信息功能，习训云会报告“位置区域”），0：等待，1：不等待
set = os.environ["SET"]
if len(set) == 0:
    system = "11" # 模拟Android版本号
    app_version = "4.4.7" # 模拟App版本号
    uuid = "00:00:00:00:00:00" # 模拟UUID
else:
    system = set.split( )[0] # 模拟Android版本号
    app_version = set.split( )[2] # 模拟App版本号
    uuid =set.split( )[3] # 模拟UUID

model = os.environ["MODEL"]
if len(model) == 0:
    model = "Xiaomi 10" # 模拟机型
# 配置结束



if __name__ == '__main__':
    # 待加密字符串或者字节
    # 调用to_encrypt类方法来进行加密
    cryto_info = HandleSign.to_encrypt(longitude)
    print(longitude)
    
def isset(v): 
    try : 
        type (eval(v)) 
    except : 
        return  0 
    else : 
        return  1
def get_remark(var):
    return {
        0: "上班",
        1: "外出",
        2: "假期",
        3: "请假",
        4: "轮岗",
        5: "回校",
        6: "外宿",
        7: "在家",
        8: "下班",
        9: "学习",
        10: "毕业设计",
        11: "补签",
    }.get(var,"未知类型")
msg = ""
msg += '我来看一下~\n'
if no_wait==0:
    for i in range(1,100):
        try:
            # 获取位置信息
            req = request.Request("https://restapi.amap.com/v3/geocode/regeo?key=8325164e247e15eea68b59e89200988b&location="+longitude+","+latitude+"&radius=2800")  # GET方法
            regeopage = request.urlopen(req, timeout=10).read()
            regeopage = regeopage.decode('utf-8')
            regeopage = json.loads(regeopage)
            # print(regeopage["regeocode"]["formatted_address"])
            # exit()
            break
        except Exception as e:
            msg += '出现异常-->'+str(e) +'\n'
    msg += '你将会用你的账号在' + regeopage["regeocode"]["formatted_address"] + '（经度：' + longitude + '，纬度' + latitude+'）以' + remark_name + '进行签到。(｀・ω・´)\n'
    msg += '请确认一下哦~\n'
else:
    regeopage = {"status":"1","info":"OK","infocode":"10000","regeocode":{"formatted_address":[],"addressComponent":{"country":[],"province":[],"city":[],"citycode":[],"district":[],"adcode":[],"township":[],"towncode":[],"streetNumber":{"street":[],"number":[],"location":"0,0","direction":[],"distance":[]}}}}
    msg += '你将会用账号' + account + '在经度：' + longitude + '，纬度' + latitude + '以' + remark_name + '进行签到。(｀・ω・´)\n'
msg += '我们来登录吧！\n'
headers = {
    # 'User-Agent':'FuckXixunyun'
}
for i in range(1,100):
    try:
        # 登录
        loginurl = "https://api.xixunyun.com/login/api?from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0"
        logindata = {"registration_id":"1104a8979285e976298","platform":2,"system":system,"model":model,"app_version":app_version,"account":account,"app_id":"cn.vanber.xixunyun.saas","uuid":uuid,"password":password,"key":"","request_source":"3","school_id":school_id}
        logindata = parse.urlencode(logindata).encode('utf-8')
        req = request.Request(loginurl, headers=headers, data=logindata)  #POST方法
        accountpage = request.urlopen(req, timeout=10).read()
        accountpage = accountpage.decode('utf-8')
        accountpage = json.loads(accountpage)
        # print(accountpage)
        break
    except Exception as e:
        msg += '出现异常-->' + str(e) + '\n'
msg += '登录状态码：' + str(accountpage["code"]) + '\n'
msg += '登录状态：' + accountpage["message"] + '\n'
msg += '服务器返回响应时间：' + accountpage["run_execute_time"] + '\n'
if accountpage["code"]==20000: # 成功
    msg += '内部账户编号：' + str(accountpage["data"]["user_id"]) + '\n'
    msg += '你好' + accountpage["data"]["user_name"] + '！(/・ω・)/\n'
    msg += '目前你的积分为' + str(accountpage["data"]["point"]) + '分，全校排名第' + str(accountpage["data"]["point_rank"]) + '位\n'
    msg += '姓名：' + accountpage["data"]["user_name"] + '\n'
    msg += '班级：' + accountpage["data"]["class_name"] + '\n'
    msg += '入学年份：' + accountpage["data"]["entrance_year"] + '\n'
    msg += '绑定手机号：' + accountpage["data"]["bind_phone"] + '\n'
    msg += '登录令牌：' + accountpage["data"]["token"] + ']\n'
    if no_wait==0:
        msg += '请确认账户没错哦~\n'
    
    msg += '正在进入签到页面~\n'
    for i in range(1,100):
        try:
            # 获取签到信息(原始信息：month_date=2018-12)
            req = request.Request("https://api.xixunyun.com/signin40/homepage?month_date=&token="+accountpage["data"]["token"]+"&from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0")  # GET方法
            signhomepage = request.urlopen(req, timeout=10).read()
            signhomepage = signhomepage.decode('utf-8')
            signhomepage = json.loads(signhomepage)
            break
        except Exception as e:
            msg += '出现异常-->' + str(e) + '\n'
    msg += '进入签到页面状态码：' + str(signhomepage["code"]) + '\n'
    msg += '进入签到页面状态：' + signhomepage["message"] + '\n'
    msg += '服务器返回响应时间：' + signhomepage["run_execute_time"] + '\n'
    if signhomepage["code"]==20000: # 成功
        # print(signhomepage["data"])
        msg += '连续签到次数：' + signhomepage["data"]["continuous_sign_in"] + '\n'
        msg += '服务器返回签到类型数据：' + str(signhomepage["data"]["mark_list"]) + '\n'
        msg += '开始匹配签到类型数据\n'
        for i in signhomepage["data"]["mark_list"]:
            # print(i)
            # if i["value"] == remark_name:
            if i["value"] == remark_name:
                msg += '找到对应数据了！类型名称' + str(i["value"]) + '对应Key为' + str(i["key"]) + '\n'
                remark = i["key"]
                break
        if(isset('remark')==0):
            msg += '没有找到类型数据，请确认是否配置正确（可以参考输出日志中的“服务器返回签到类型数据”部分）\n'
            print(msg)
            exit()
        print (regeopage["regeocode"]["addressComponent"]["province"])
        signactdata_origin = {"change_sign_resource":"0","longitude":longitude,"latitude":latitude,"comment":"","remark":remark,"address":regeopage["regeocode"]["formatted_address"],"address_name":(regeopage["regeocode"]["addressComponent"]["province"]+regeopage["regeocode"]["addressComponent"]["city"]+regeopage["regeocode"]["addressComponent"]["district"])}
        print("开始组合数据包：",signactdata_origin)
        if no_wait==0:
            msg += '数据包没错哦~（其实只是让开发者确认啦）\n'
            
        msg += 'Biu~那么我们就开始吧！\n'
        
        print(msg)
        exit()
        
        for i in range(1,100):
            try:
                # 签到
                signacturl = "https://api.xixunyun.com/signin_rsa?token="+accountpage["data"]["token"]+"&from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0"
                signactdata = signactdata_origin
                signactdata = parse.urlencode(signactdata).encode('utf-8')
                req = request.Request(signacturl, headers=headers, data=signactdata)  #POST方法
                signactpage = request.urlopen(req, timeout=10).read()
                signactpage = signactpage.decode('utf-8')
                signactpage = json.loads(signactpage)
                # print(signactpage)
                """ 
                数据样例（20181215）
                {
                    "code": 20000,
                    "message": "成功",
                    "run_execute_time": "0.0689s",
                    "data": {
                        "point": 2,
                        "continuous": 4,
                        "message_string": "太棒了！+2积分，您已签到4天。"
                }
                """
                break
            except Exception as e:
                msg += '出现异常-->' + str(e) + '\n'
        # print("原始信息：",signactpage)
        msg += '签到状态码：' + str(signactpage["code"]) + '\n'
        msg += '签到状态：' + signactpage["message"] + '\n'
        msg += '服务器返回响应时间：' + signactpage["run_execute_time"] + '\n'
        if signactpage["code"]==20000: # 成功
            msg += '\r\n\r\n' + signactpage["data"]["message_string"] + '\n'
        else:
            msg += '\r\n\r\n好像签到失败了QAQ\n'
            msg += '原因：'+  str(signactpage["message"]) + '\n'
            print(msg)
            exit()
    else:
        msg += '\r\n\r\n好像正在进入签到页面失败了QAQ\n'
        print(msg)
        exit()
else:
    msg += '\r\n\r\n好像登录失败了QAQ\n'
    print(msg)
    exit()
