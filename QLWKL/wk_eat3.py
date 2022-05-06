'''
cron:0 1 8,13,18,22 * * ?
new Env('悟空吃饭补贴')
'''
import requests
import random,sys,json,time
import os
###########################################检测环境和处理变量######################################
#获取变量文件路径
def path_e():
    #获取当前运行文件目录
    path_w=os.getcwd()
    if 'ql' not in path_w:
        print('当前运行脚本不在青龙,请把脚本放在青龙目录下！')
        sys.exit()
    #提取目录
    file_path = ''
    for i in path_w.split('/'):
        if i == 'ql':
            break
        file_path += i + '/'
    file_path_last = file_path + 'ql/config/env.sh'
    return file_path_last.strip()
#读取tooken函数
def file_token():
    token = []
    try:
        file = open(path_e(), 'r')
        for i in file.readlines():
            # 读取token
            if 'xtttoken' in i:
                token += [
                    i.replace('export', '').replace('"', '').replace('\n', '').replace('xtttoken=', '').strip()]
        file.close()
        return token
    except:
        print('没有找到变量文件，或者token填写错误')
        sys.exit()
#读取cookie函数
def file_ck():
    cookie_file = []
    try:
        file = open(path_e(), 'r')
        for i in file.readlines():
            # 读取wkkcookie  cookie
            if 'wkcookie' in i:
                cookie_file += [i.replace('export', '').replace('"', '').replace('\n', '').replace('wkcookie=','').strip()]
        file.close()
    except:
        print('没有找到变量文件，或者cookies填写错误')
        sys.exit()
    #开始处理cookie格式
    cookies=[]
    try:
        for i in range(len(cookie_file)):
            # 判断不符合的cookie信息
            if len(cookie_file[i]) < 10:
                continue
            # 判断是否有多个变量
            if '&' in cookie_file[i]:
                cc = cookie_file[i].split('&')
                for x in cc:
                    a = x.replace('=', '":"').replace(';', '","')
                    ck = '{"' + a + '"}'
                    cookies += [ck]
                break
            # 只有一个cookie变量
            a = cookie_file[i].replace('=', '":"').replace(';', '","')
            ck = '{"' + a + '"}'
            cookies += [ck]
        return cookies
    except:
        print('cookie信息填写错误请检查')
        sys.exit()
##################################做任务部分##########################################
#吃饭补贴
def et(cookie,token):
    api='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/eat/done?_request_from=web&scm_build_version=1.0.0.76&device_platform=android&os=android&ssmix=a&_rticket=1651642326315&_rticket=1651642326320&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&channel=xiaomi_6589_64&aid=6589&app_name=gold_browser&version_code=1138&version_name=1.3.8&manifest_version_code=11380&update_version_code=113805&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C4002641%2C4004664%2C4012767%2C4023316%2C4054291%2C4055170%2C4057887%2C4064419%2C4079374&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=default&recommend_switch=true&isTTWebView=1&session_id=dd038e89-566b-47a2-a631-b6da6fc552ca&host_abi=arm64-v8a&is_db=0&rom_version=miui_v125_21.4.22&iid=2027938897208093&device_id=2400977487399848&luckydog_base=g14lyWliXe8MTKYLvfWOnEWIXz6hFqQ9IdTKcjS1WsOQ7JA0K2zIatL5MejeAtm3qAQcSBNWk6dKFy4StCr29MO9A_KgYF9FA6qyjoZcHRYuiwZWmElVyGQzkTrQAqeNmK1iN6IBDmOQgxDgCT3cE1wHXPlwTQas4pjlGx218uY&luckydog_data=u9jvYPXk5SqG2C5flAUt2lusHs5yEy8geNWgTE0zWPDGpN7367fs-tFDZsU3nL7ExwigI-G3k_HVcv4cW_5JTxjB7SUhHe5o77x9ORSVo8k&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.24&luckycat_version_code=501024&status_bar_height=26'
    header = {'x-ss-req-ticket': '1651734304479', 'sdk-version': '2', 'x-tt-token': token,
              'passport-sdk-version': '30442',
              'x-tt-dt': 'AAAVTXZAUUXUGUDXVORIKIQHPVB7QIPAGR7LR5Y66H5Y2FOMXX7XPUZ42OUMSR4DOR2X6EBROPRB3RGPC57NB7ZVBEAWA35PPABCZUNUBCQEDFVQDYEDEOV7DC6UD2Y5FF33KX3OSQU4KUWDTSDNQJQ',
              'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json; charset=UTF-8',
              'x-ss-stub': '99914B932BD37A50B983C5E7C90AE93B', 'x-tt-request-tag': 's=1;p=0', 'x-ss-dp': '6589',
              'x-tt-trace-id': '00-9309587a0d887ad22400ba863f4419bd-9309587a0d887ad2-01',
              'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion',
              'accept-encoding': 'gzip, deflate',
              'x-argus': 'HTWRIySW9SKZji8Swd+kct4fBt4R/YT9UShPi8bK2Cfy2D8tSNKBrudTpo2omMGtN72DjgyIbQ7DZMYtiwDR1VvO6eAUhy+JOJvF3nIJrOfVizAVA50NUepjgt432SWDjoiXcanMHQNcpqWmlXNz13FBRyGmdDGYrYFIJCTS7vTkFR54xF966RdDnByWd1R/3dRDRF4NbFRF5KgAgAQioWwOvC2f7OmfEjEqbhVPgcV/vSZGw8o6DrBCqyz9eoK4hXEReafSB+Nr7CL4LtXTnDrx',
              'x-gorgon': '8404c0760000ca8880c8c5c47f54e7a2b19cc420b6e1a5beb144', 'x-khronos': '1651734302',
              'x-ladon': '1DJxJwBJYl7177cQg8nCqNd2nWIMh/Smo1ZzBvsZT0qMGNUr'}
    data_wk = {"enable_preload_exciting_video":0}
    re_wk = requests.post(url=api, headers=header, cookies=cookie, json=data_wk)
    try:
        a=re_wk.json()['data']["score_amount"]
        print(f'领取吃饭补贴获得金币{a}')
    except:
        print(re_wk.text)
        sys.exit()

if __name__=="__main__":
    # 开始检测ck
    a_len = file_ck()
    if len(a_len) == 0:
        print('一个ck也没有,请检查账号信息')
        sys.exit()
    print(f'🔔🔔🔔共检测到{len(a_len)}个ck🔔🔔🔔')
    # 开始检测token
    t_token = file_token()
    if len(t_token) == 0:
        print('请设置环境变量 token ')
        sys.exit()
    #######################
    for ck in range(len(a_len)):
            print(f'⚠️第{ck+1}账号开始做任务')
            et(json.loads(a_len[ck]), t_token[0])
            time.sleep(5)