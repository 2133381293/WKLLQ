'''
cron:0 */40 6-23 * * ?
new Env('悟空阅读and小说 ')
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
def readnove_id(cookie,token):#获取参数——时间戳
    api='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/detail?device_platform=android&os=android&ssmix=a&_rticket=1650962272586&_rticket=1650962272600&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&channel=xiaomi_6589_64&aid=6589&app_name=gold_browser&version_code=1138&version_name=1.3.8&manifest_version_code=11380&update_version_code=113805&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4031501%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C3990734%2C4002641%2C4012767%2C4023316%2C4054291%2C4064419%2C4070289&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=default&recommend_switch=true&isTTWebView=1&session_id=8c058eee-280e-4760-8fa0-64a7b6c1314b&host_abi=arm64-v8a&is_db=0&rom_version=miui_v125_21.4.22&iid=2027938897208093&device_id=2400977487399848&luckydog_base=Yn-R8NF_utRHu4f9Xz9DpwzDqLDUpixik68eh5UdTSY7k05tTe0RatiEAgJvWcaQmcPHqc99rdlYFzil_nxaety-RpQo8QYihxfSre6oC6WCPNW1qFGphPIsslHLc5oD_tZMS1iufr17p6IlNO7iuVAlHf6CER9bczp3smhCMaE&luckydog_data=vznI0crtLv-MPkr5QQ_YMbOafjCYz0R3y0RDpMy1KpRTIbfTE2p0yCJJOnQ5LchoBg_msZO33ihrlUC9Q5cBYj7hq4et4ZnIe869Q1tlVD4&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.24&luckycat_version_code=501024&status_bar_height=26'
    headers={'Host': 'api5-normal-lf.toutiaoapi.com', 'accept': 'application/json', 'content-type': 'application/json;encoding=utf-8', 'x-ss-req-ticket': '1650962272604', 'sdk-version': '2', 'x-tt-token':token , 'passport-sdk-version': '30442', 'x-tt-dt': 'AAAXYB3XH4EEGQKJOONTRZKQNONYNOZQ2VXJ2PKYGYJRCED4I62RUU2NJAFKS6PMJ2LD6FXD4WRK7Y67LL6ZYBLDA5JY2TRRSJ2G2THDIXEBPC3B7K2DFS5GRQNSVLVSQ2AQIN6MM6H6RGSMK72R3LQ', 'x-vc-bdturing-sdk-version': '2.2.0.cn', 'x-tt-request-tag': 's=1;p=0', 'x-ss-dp': '6589', 'x-tt-trace-id': '00-650512ea0d887ad22400ba8db0c319bd-650512ea0d887ad2-01', 'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion', 'accept-encoding': 'gzip, deflate', 'x-argus': 'SbfLPHfC16xtBrzwl/Fe4GAtlRYEc654mlAXRUkWzw3Gnv6ddM3fXcGToWQaGmEcxF78vlKQa9ADnPxG2CdhT5FxWpojjKSoIde8uwUjyk3WmdqwhSV7PWMgLcyTgJNFpBbNoO4X4lRIse6HaBGhIGUsRw4/aFQvIynJy87txaw2Y47GzIky/3xzJ4R+7o7NmLHxZZPytmM7uZ3k5xLZ7/IroT3Xwyr+H4POk3ZwYA/81CJKVWIW0qXUMZ1vwh/flmiAxYDF9fJTVErZ5nhnhquA', 'x-gorgon': '840480f50000096fc03618adaf2707ada7a64fece3515cab30fc', 'x-khronos': '1650962269', 'x-ladon': 'SyR9MpqUIQyiofcA4c//bAAGO/o+5KZNhRYy3rVcKK9uwSX7'}
    re=requests.get(url=api,headers=headers,cookies=cookie)
    try:
        nove_id = re.json()['data']['treasure_task']['next_treasure_time']
        return nove_id
    except:
        print('获取nove——ts错误')
        sys.exit()

def readnove(cookie,token):#金币累计满领取金币
    api='https://api5-normal-lf.toutiaoapi.com/luckycat/sj/v1/container/balance_transfer_hangup?_rticket=1650962270724&manifest_version_code=11380&iid=2027938897208093&channel=xiaomi_6589_64&isTTWebView=1&device_type=MI%20CC%209e&language=zh&host_abi=arm64-v8a&resolution=720*1475&is_db=0&update_version_code=113805&dq_param=2&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&os_api=29&dpi=320&ab_feature=94563%2C102749&ac=mobile&os=android&device_id=2400977487399848&os_version=10&pass_through=default&version_code=1138&session_id=8c058eee-280e-4760-8fa0-64a7b6c1314b&app_name=gold_browser&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4031501%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C3990734%2C4002641%2C4012767%2C4023316%2C4054291%2C4064419%2C4070289&homepage_version=1&version_name=1.3.8&plugin=0&device_brand=Xiaomi&ssmix=a&recommend_switch=true&device_platform=android&aid=6589&rom_version=miui_v125_21.4.22'
    headers_1={'Host': 'api5-normal-lf.toutiaoapi.com', 'content-length': '54', 'x-ss-req-ticket': '1650962270726', 'sdk-version': '2', 'x-tt-token': token, 'passport-sdk-version': '30442', 'x-tt-dt': 'AAAXYB3XH4EEGQKJOONTRZKQNONYNOZQ2VXJ2PKYGYJRCED4I62RUU2NJAFKS6PMJ2LD6FXD4WRK7Y67LL6ZYBLDA5JY2TRRSJ2G2THDIXEBPC3B7K2DFS5GRQNSVLVSQ2AQIN6MM6H6RGSMK72R3LQ', 'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json; charset=UTF-8', 'x-ss-stub': '24C9F7F02745615C82DE5CA82DD61874', 'x-tt-request-tag': 's=1;p=0', 'x-ss-dp': '6589', 'x-tt-trace-id': '00-65050b990d887ad22400ba85188b19bd-65050b990d887ad2-01', 'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion', 'accept-encoding': 'gzip, deflate', 'x-argus': 'J52K9hZPNlalbcz7hVV9VZ/mdNbkkDjkFSiLgL3Hmnsj4rQu1zmujH6+JxYOhQTOHmkgTKywgXq6gAGsM+bJm3n48Ip8ECa+UfZHRgSXDLHVzeyPjosSliEfhzjcYO+PAvIK7NjzlnLNtVfkCnYXfJQQleU83NgATYPV9aC23MgWAbMyzu5ogviDx0+i93xWBCbWheC32WhVfYV0TVPaWoToHF0Ifg6cn5ddaPxEY2C0+os9mg/PtAuGhSA7YXxTgXNhMjZpZxpngXhH4p1I71tR', 'x-gorgon': '8404005c00004b2e4a18acd10ea63042447c07b0e4ec13b8eee9', 'x-khronos': '1650962267', 'x-ladon': 'F4wfD7IITFaCO2Rb3gqKuMbrXnFWhvNfWCVxR8d7JNU2h5MZ'}
    data={"c_amount":300,"ts":f"{readnove_id(cookie,token)}","scene_key":"Novel"}
    time.sleep(3)
    re_2 = requests.post(url=api, headers=headers_1, cookies=cookie, json=data)
    try:
        jb=re_2.json()["data"]["c_amount"]
        print(f'看小说获得{jb}金币')

    except:
        print('看小说失败')
        print(re_2.text)
        sys.exit()
def raenl(cookie,token):#获取金币，此处该首次运行
    api_3='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/whole_scene/done?device_platform=android&os=android&ssmix=a&_rticket=1650973544691&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&channel=xiaomi_6589_64&aid=6589&app_name=gold_browser&version_code=1138&version_name=1.3.8&manifest_version_code=11380&update_version_code=113805&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4031498%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C3990734%2C4002641%2C4012767%2C4023316%2C4054291%2C4064419%2C4070289&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI%20CC%209e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=default&recommend_switch=true&isTTWebView=1&session_id=31a0b8db-fe6d-49fa-a2b2-16f47ffeb135&host_abi=arm64-v8a&is_db=0&rom_version=miui_v125_21.4.22&iid=2027938897208093&device_id=2400977487399848&luckydog_base=KnORt_Wpo6bXoub7kPWiolb5WRd9Sdb9rlB_u-lC3MRe84GQbF1iPjQcYXxHOkpBAnpMMT_YybbXXlBVrruarSL2MaQUrgsh8BsACdHwTfRacv04erc-nrLo_80NDt9RCzObATmSeel-8Iu4F_YvA6KrdvPcGIdEpB7eGRG7G78&luckydog_data=JSLGRZ9ArmqN7oJg1NaJ1wx6YGo-QzIMpU5LbwPd-xKuczdwShoZh2kGJqk-nH7E-nJlI3OoF3cMeBVpukczzgptqGp_gzqHKQDpPO6NKYQ&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.24&luckycat_version_code=501024&status_bar_height=26'
    headers_3={'Host': 'api5-normal-lf.toutiaoapi.com', 'content-length': '35', 'x-ss-req-ticket': '1650973544702', 'sdk-version': '2', 'x-tt-token': token, 'passport-sdk-version': '30442', 'x-tt-dt': 'AAAXYB3XH4EEGQKJOONTRZKQNONYNOZQ2VXJ2PKYGYJRCED4I62RUU2NJAFKS6PMJ2LD6FXD4WRK7Y67LL6ZYBLDA5JY2TRRSJ2G2THDIXEBPC3B7K2DFS5GRQNSVLVSQ2AQIN6MM6H6RGSMK72R3LQ', 'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json; charset=utf-8', 'x-ss-stub': 'B500145AC8E04BFD373CE94F9D55F819', 'x-tt-request-tag': 's=-1;p=0', 'x-ss-dp': '6589', 'x-tt-trace-id': '00-65b112930d887ad22400ba8bcf5b19bd-65b112930d887ad2-01', 'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion', 'accept-encoding': 'gzip, deflate', 'x-argus': 'RPnTzF8kN6PBOhCrtPV8GWaRMeAXOHvB8gcu+py6vgbjVOiTTiYWO54FUIAgxiEmqdcTFY8vSAjvYOfR38ckdI3htpHeOQK4QC7szoa6drDiRCV8h+ql/iJMaD6inaEZSloLr1WStAgU/sau8lqrBjcqLY51SDCC2PtyhVmg+T7k6tqoo9jMzIty+dK70y0I6viiaiNTDUuye9VSvUbd1lyM5JhB0jzjAOD3wENMXIQBr1YbngKbi0Bb/X0/+aJqa/r0v8JqkCRS8LtdtEq0lmOp', 'x-gorgon': '8404805d0000b9f3fefd6e1a2c3132d7d2e86974d2d4e8840786', 'x-khronos': '1650973543', 'x-ladon': 'kCYSWt3ige+qwJSaZ2b2yAXQca5UfF/qhUS48TzdcZ26SYex'}
    data_3={"group_id":"","scene_key":"Novel"}
    r_3=requests.post(url=api_3,headers=headers_3,cookies=cookie,json=data_3)
    if '成功' not in r_3.text:
        print(r_3.text)
        time.sleep(30)

#开始检测ck
a_len=file_ck()
if len(a_len)==0:
    print('一个ck也没有,请检查ck信息')
    sys.exit()
print(f'#### 共检测到{len(a_len)}个账号 ####')
#开始检测token
t_token=file_token()
if len(t_token) == 0:
    print('请设置环境变量 token ')
    sys.exit()

#检测到ck，token开始阅读小说
for ck in range(len(a_len)):
    # 总共循环次数
    print(f'第{ck+1}个账号开始运行  阅读文章5次.....')
    for x in range(5):

        # 首先运行发送金币累计金币
        f = random.randint(5, 10)
        for i in range(f):
            t = random.randint(20, 40)
            time.sleep(t)
            ############################
            raenl(json.loads(a_len[ck]),t_token[0])
        # 此处运行点击领取金币事件
        time.sleep(3)
        readnove(json.loads(a_len[ck]),t_token[0])