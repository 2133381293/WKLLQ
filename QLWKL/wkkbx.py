'''
cron:0 */11 5-23 * * ?
new Env('悟空开宝箱 ')
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
#开宝箱
def kbx(cookie,token):
    api = 'https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/done?device_platform=android&os=android&ssmix=a&_rticket=1650004532873&_rticket=1650004532878&cdid=bfc4886f-da7c-4cd4-a911-dac0069da3e6&channel=dy_wk26_zdh_zonghe_13088&aid=6589&app_name=gold_browser&version_code=1136&version_name=1.3.6&manifest_version_code=11360&update_version_code=113607&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C3931834%2C3525279%2C3577942%2C3718419%2C3765027%2C3836344%2C3842788%2C3932103%2C3949606%2C3967014%2C3977520%2C3990734%2C4002641%2C4006715&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=dy_wk26_zdh_zonghe_13088&recommend_switch=true&isTTWebView=1&session_id=32c7c283-e3f3-431a-8b40-e2b67766151b&host_abi=armeabi-v7a&is_db=0&rom_version=miui_v125_21.4.22&iid=1095549026578008&device_id=2400977487399848&luckydog_base=vXpYUvapItEkt5wB8fhvafGOmBuGVZczMob5c6PGstlhY-ZNm-Wa29uKh5hUw3yLkT42uGPlo9MCaJeIeGxgISID3476bv5SJK2yYI0RFE5T4k9m-5t2hybrr_bvpVkMl2J1bM3vmB8qLfmFSnb3Y3KQZZ8TLYG7994rSvYYFxw&luckydog_data=b0IG2Xt2cCG9KEc3XneBkCOzEpZBOxdaDjfrKtawtnjO38JUpechnrdfobU0eyXAcE9da3Yb5uvB_xh_lmoVJlqYulQUjFKDPkFi3266a6c&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.17&luckycat_version_code=501017&status_bar_height=26 h2'
    header1 = {
        'accept': 'application/json', 'x-ss-req-ticket': '1650004532881', 'sdk-version': '2', 'x-tt-token': token,
        'passport-sdk-version': '30442',
        'x-tt-dt': 'AAATVB3XKGQHUUPOAVCF6VLHX62VVTQRVKMZXLM3N3FEWVACFI2BBC6X3RE2REQ6LXGFD7J6WZGFY7A5PIUIACJDSQWGYOK4TL4S5EPSOSOUOVNOEXP2MVV3NIWX7YNTPHLUFBCZUAS3SIILWEUNNVA',
        'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json;encoding=utf-8',
        'x-ss-stub': '99914B932BD37A50B983C5E7C90AE93B', 'x-tt-request-tag': 's=1;p=0', 'x-ss-dp': '6589',
        'x-tt-trace-id': '00-2bef201d0d887ad22400ba806a7e19bd-2bef201d0d887ad2-01',
        'user-agent': 'com.cat.readall/11360 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion',
        'accept-encoding': 'gzip, deflate',
        'x-argus': 'cHw9A9G/bfGwN0MKXZ94wx23Yw4/hjlM6yWM31FFCQ9hJ1tX3jBwH3Hyy7Qckdh7QeI4OtC6SqWW+XNxKqRAG32fA3S4XPXNPAEc4cGvOGhRlj+XOtKZ9+oVoAd1Ki5l1TKXOUt0FqvxL/x3BUpd4oWM2bmeXljb1a1sgKCha675WhWgzIFAi1hGRd7jixabE7LYBLpZRotklLF2yFbC6iE82HHf1v/cG9i4MhP67/mmzw1KK35s+r4kf4hRwh8XTf50Z5jWKtxYpNiitayd95R5',
        'x-gorgon': '040420a80000f12a62c424ceb02a75025b904b67d089f001bcfe', 'x-khronos': '1650004532',
        'x-ladon': 'uabdLxbMyTHWP134Xgsj3v6v4nhBRIxXemzJvKjOsIilYMWs'
    }
    #开宝箱数据
    data={
        }
    re = requests.post(url=api, headers=header1, json=data, cookies=cookie)
    try:
        print(re.json()["data"]["score_amount"])





    except:
        print('开宝箱失败')
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

    for ck in range(len(a_len)):
            a = random.randint(30, 60)
            print(f'随机等待{a}秒')
            time.sleep(a)
            print(f'⚠️第{ck+1}账号开宝箱获得金币',end=' ')
            kbx(json.loads(a_len[ck]),t_token[0])