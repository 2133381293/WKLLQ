'''
cron:0 1 0 * * ?
new Env('今日头条2签到.')
'''
#jrtoken   jrcookie变量名 签到
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
    api = 'https://api5-normal-lf.toutiaoapi.com/luckycat/lite/v1/sign_in/action?manifest_version_code=8750&_rticket=1649812091621&sa_enable=0&act_token=CbKKB2kKaYifAocl6r_qSJsPlM90YahQz2D4Lhnc-xxC7Ws9DiFXMVqQbeHaXtCHaEZGoomXPJ3eiPg_OZN3zA&iid=3382530259551581&channel=lite_xiaomi_64&isTTWebView=1&use_ecpm=0&device_type=MI+CC+9e&language=zh&host_abi=arm64-v8a&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&resolution=720*1475&cookie_base=WCilq_0e2W-djHKxuMgfck0jZ6qpCgtEronl1r0f1NdjjoFmNE_kKKapK18JpyoEtI6DIvOwfgF-kDvpP0Wbs0XR0MhqTONZy040k7SdCBw&is_pad=0&update_version_code=87507&dq_param=2&status_bar_height=26&cdid=6b68202d-3da9-4ee1-909e-8ebe5337dd3d&ab_group=z2&os_api=29&abflag=3&rit=coin&dpi=320&ab_feature=z1&cookie_data=KWD6GOF-mlEWW7t0kHhC2g&ac=wifi&act_hash=4823f2b8e1306558044de925bb4ec496&device_id=2400977487399848&os=android&pass_through=default&os_version=10&version_code=875&session_id=c026ecfc-5c2f-4f16-afe2-961dac6b2a18&tma_jssdk_version=2.8.0.16&app_name=news_article_lite&ab_version=668905%2C3937366%2C668904%2C3937345%2C668906%2C3937374%2C668903%2C3937392%2C1859937%2C668908%2C3937402%2C668907%2C3937398%2C3801463%2C2220242%2C3520490%2C3596061%2C3936294%2C3958946&version_name=8.7.5&device_brand=Xiaomi&ssmix=a&plugin_state=139681997156381&device_platform=android&polaris_version=1.0.5&aid=35&rom_version=miui_v125_21.4.22&luckydog_base=WyxIFYW3v6lWtQzUNYpnswSGhDsj5LNxi9WHIes_Lk_pEBc3MEJt0H0SwyQmncuserSNxC2Q_bU_toMECP3MT5oCCEoMLxw4Bux8sE1XNNwnSZrujTOgcgTV1jgpapD1Q5T2kTt4UomT_UYIyCcJ6HiKePWxxHoRNa6q0y9y-8M&luckydog_data=LcTRkETRI9xqIpSJ6aAD9lPviR7BjjMGkaP0EDeu_jD2SdwRno9UgCtflOPPhko763D8tBiPoxjH-mhRaWSZH_dV9gzHWubAwz0zV56Lurs&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.20&luckycat_version_code=501020'
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
    data = {
        "use_ecpm": 0, "rit": "coin"
    }
    re = requests.post(url=api, headers=header, data=json.dumps(data), cookies=cookie)

    print(re.text)
def ygg(cookie,token):
    api = 'https://minigame3-normal-lf.zijieapi.com/ttgame/game_orchard/fortune_tree/shake?os_version=10&version_code=875&device_id=2400977487399848&iid=3382530259551581&app_name=news_article_lite&device_platform=android&device_type=MI+CC+9e&channel=lite_xiaomi_64&aid=35&version_name=8.7.5&update_version_code=87507'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; MI CC 9e Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 NewsArticle/8.7.5.0 ToutiaoMicroApp/2.31.1.1 PluginVersion/874011',
        'content-type': 'application/json', 'sdk-version': '2',
        'x-tt-token': token,
        'passport-sdk-version': '30442', 'x-tt-request-tag': 's=-1;p=1', 'x-ss-dp': '35',
        'x-tt-trace-id': '00-279910ea010627b9bbc1890747960023-279910ea010627b9-01', 'referer': 'https',
        'x-argus': 'CU53UAz8Me8Ju6Nf81mHfUrhFijIYacb4jY1N7ZMc5rUmDymn3rb3TAal20Y0uzMneuEdDtL0KyF4vpY6zPbJDHTxw7kyr0B+oTrsf66AzT/ceqjjxUfflduhKovTtq/90CXobYkoKIWMRn+cW6q8xJbpNdtuAXs9JFS65dsbXif7SdvCtWuShew4euoag/xfvAwFvrftgdlrQEMmmVavqyp',
        'x-gorgon': '84044044000062cdfbff4e6341194f470060032e73367a6b42cf', 'x-khronos': '1649931781',
        'x-ladon': 'tBJyeYKPbRsyYyZ9roy+nmpLF2RBgfakncQIgU2l/2Lai1Fr'}
    try:
        re = requests.get(url=api, headers=headers, cookies=cookie)
        print(re.json())
    except:
        print('领取失败')
        print(re.text)

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
    #######################开始做任务
    for ck in range(len(a_len)):
            print(f'⚠️第{ck+1}账号开始签到')
            kbx(json.loads(a_len[ck]), t_token[0])
            print('尝试摇金币一次')
            time.sleep(10)
            ygg(json.loads(a_len[ck]), t_token[0])
            time.sleep(6)