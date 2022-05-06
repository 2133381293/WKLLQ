'''
cron:0 */12 * * * ?
new Env('今日头条2开宝箱')
'''
#jrtoken   jrcookie变量名 开宝箱
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
            if 'jrtoken' in i:
                token += [
                    i.replace('export', '').replace('"', '').replace('\n', '').replace('jrtoken=', '').strip()]
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
            # 读取jrcookie  cookie
            if 'jrcookie' in i:
                cookie_file += [i.replace('export', '').replace('"', '').replace('\n', '').replace('jrcookie=','').strip()]
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
##########################################################################
def kbx(cookie,token):
    header = {
        'X-SS-STUB': '9229AEBE1549800C042EF9422DD4A208',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI CC 9e Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 cpdaily/9.0.12 wisedu/9.0.12',
        # 抓包数据X-Tt-Token
        'X-Tt-Token': token,
        'X-SS-REQ-TICKET': '1649577581972',
        'x-tt-dt': 'AAAQWMQYPGJ3OIQ3KKQ72D4MOT7KTC5M2OO5GGYTYLJBLAAMGI4HFDLE6QVUX7O36GMNUAXVF7DQIBL55Y2R4ISCURHWNPBQBVAXXVNUXKPNUEMA5VJHX6W3Y5Z5CSAVO3BNOSX26OEW7FGJ5EKAUCI',
        'x-vc-bdturing-sdk-version': '2.2.1.cn',
        'passport-sdk-version': '30442',
        'X-Ladon': '+5exW76hR5HgeSKw4FvCks1MA4OJz0gJ+/qljxMkdLUg3RoI',
        'X-Gorgon': '0404c0d740016927207137e7a8e2afc2c43df0fc31c8b3d7f562',
        'X-Khronos': '1649577581',
        'X-Argus': 'fIZHS0l0FNY4P2SPplYZ581wpvnrjz3DkoQxsnCD1svIWEkd0Il8hza+3l4wmNqs7K3Uz5y+UI6Pc3TA+RGPICvs791HLdGwNE11Se5hZOGqs0M2TsAufX/O6qS7Rou1+B3YgrRdkdkCyx2MDwajuyD4tO5AZUHAXordseJQY5W0fTb60KXHKH714eOiZRiwqzraJizrYhHa1nvk9Bal1jsxcTmPECgc7YzbFLuJZvnZq8E7vNp6sdXsXwe3KYWWMVPmC55N7tVlPrzm83xjMu6y',
        'Content-Type': 'application/json'}
    url = 'https://api5-normal-hl.toutiaoapi.com/score_task/v1/task/open_treasure_box/?os_api=25&device_type=LENOVO+L79031&ssmix=a&manifest_version_code=8750&dpi=240&abflag=3&pass_through=default&cookie_data=Us_Pln3yqyFFb1LzrDW1BA&use_ecpm=0&act_hash=4823f2b8e1306558044de925bb4ec496&rom_version=25&rit=coin&isTTWebView=0&app_name=news_article_lite&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&version_name=8.7.5&ab_version=668903%2C3937392%2C1859937%2C668908%2C3937402%2C668907%2C3858187%2C3937398%2C668905%2C3937366%2C668906%2C3937374%2C668904%2C3937345%2C3801462%2C3856300%2C3520489%2C3540011%2C3596061%2C3700363%2C3707270&plugin_state=139681997156381&session_id=c95b2ffa-03de-4a99-9419-add27ec656e4&sa_enable=0&ac=wifi&host_abi=armeabi-v7a&update_version_code=87507&channel=lite_baidu_zr&_rticket=1649589691358&status_bar_height=24&cookie_base=aDmsYzoCdx1Mk78M6UI3JhlTbMTkli4VUH6_C_EAq4kalYu8sTXaqtM_hvHvb-l4zT5U0rbC1T7Gsolpo9b4hRrY9kFxLokkYGcbfzqHB1o&dq_param=1&device_platform=android&iid=1500168077710142&version_code=875&polaris_version=1.0.5&tma_jssdk_version=2.8.0.14&cdid=f7e4eb3b-f87f-465b-afa0-3995f30e661f&os=android&is_pad=1&device_id=3298947584760952&resolution=720*1280&act_token=HLKSeQ21-TLVUUM8HNRZtcygeOsBVUuDpKnXljvB17-CvryAIxub4cTkPU7J_HJyJ8-F0N8_uEq3qsYxHDqWfg&os_version=7.1.2&language=zh&device_brand=LENOVO&aid=35&ab_feature=z1&luckydog_base=gOPAhxYQIyPWo0my7INrZCDVCvkKObtHZ6JHvPBGIZkSx3i2fuHnTjPrIoDESSnejvcVYv5XuCoPxy_bvxCdFgq7LGj9Oyf4PS53G6b57VUQL3ys6NUYarqp9mvBQ0uCjwHPkX9FF7VC0BZcQ98a7qGajjBMFoheo4DP_J2OlHY&luckydog_data=HFCZw__eI6ZI6WJwX5CazG6_w3T0PJjjOyezXLyMvUKXCCzoInwE7J8Cvpl--vnTFy_Ty4r8aS1FIbnQIMTvvAvBgvHekjDOwC_cf5qmsEo&luckydog_token=o5s2PibOgpATyYds1rbBSeqb2-TLDgA92JwedpPumF258MT0BoZeGbay7NjE2Xgw&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.20&luckycat_version_code=501020'
    data = {
        "use_ecpm": 0, "rit": "coin", "open_treasure_box_enter_from": "", "from": "task_page",
        "enable_preload_exciting_video": 0
    }
    q = requests.post(url=url, headers=header, cookies=cookie, json=data)
    try:
        jb = q.json()["data"]["score_amount"]
        print(f'开宝箱获得金币{jb}')
    except:
        print('开宝箱失败')
if __name__=="__main__":
    # 开始检测ck
    a_len = file_ck()
    if len(a_len) == 0:
        print('一个ck也没有,请检查账号信息')
        sys.exit()
    print(f'🔔🔔🔔今开宝箱共检测到{len(a_len)}个ck🔔🔔🔔')
    # 开始检测token
    t_token = file_token()
    if len(t_token) == 0:
        print('请设置环境变量 token ')
        sys.exit()
    #######################开始做任务
    for ck in range(len(a_len)):
            print(f'⚠️第{ck+1}账号开始做任务')
            kbx(json.loads(a_len[ck]), t_token[0])
            time.sleep(6)