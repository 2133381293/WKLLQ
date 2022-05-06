#悟空浏览器任务
#自己抓取cookies 和  x-tt-token两个数据
#定时规则建议一天运行一次
# 0 0 1 * * ? #每天凌晨 1 点执行一次
#            ——————————————适用青龙脚本

import requests
import random,sys,json,time
#读取tooken函数
def file_token():
    token = []
    try:
        file = open('/ql/config/env.sh', 'r')
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
        file = open('/ql/config/env.sh', 'r')
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
###############################################################、
#领取天气补贴每天一次
def weter_wk(cookie,token):
    api_wt='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/weather/done?_rticket=1651734304465&manifest_version_code=11380&iid=2027938897208093&channel=xiaomi_6589_64&isTTWebView=1&device_type=MI+CC+9e&language=zh&host_abi=arm64-v8a&resolution=720*1475&is_db=0&update_version_code=113805&dq_param=2&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&os_api=29&dpi=320&ab_feature=94563%2C102749&ac=wifi&os=android&device_id=2400977487399848&os_version=10&pass_through=default&version_code=1138&session_id=dc6e04ff-21f0-4d24-aaa5-c1d8494b9390&app_name=gold_browser&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C4002641%2C4012767%2C4023316%2C4054291%2C4055170%2C4057887%2C4064419%2C4079374&homepage_version=1&version_name=1.3.8&plugin=0&device_brand=Xiaomi&ssmix=a&recommend_switch=true&device_platform=android&aid=6589&rom_version=miui_v125_21.4.22'
    header={'x-ss-req-ticket': '1651734304479', 'sdk-version': '2', 'x-tt-token': token, 'passport-sdk-version': '30442', 'x-tt-dt': 'AAAVTXZAUUXUGUDXVORIKIQHPVB7QIPAGR7LR5Y66H5Y2FOMXX7XPUZ42OUMSR4DOR2X6EBROPRB3RGPC57NB7ZVBEAWA35PPABCZUNUBCQEDFVQDYEDEOV7DC6UD2Y5FF33KX3OSQU4KUWDTSDNQJQ', 'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json; charset=UTF-8', 'x-ss-stub': '99914B932BD37A50B983C5E7C90AE93B', 'x-tt-request-tag': 's=1;p=0', 'x-ss-dp': '6589', 'x-tt-trace-id': '00-9309587a0d887ad22400ba863f4419bd-9309587a0d887ad2-01', 'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion', 'accept-encoding': 'gzip, deflate', 'x-argus': 'HTWRIySW9SKZji8Swd+kct4fBt4R/YT9UShPi8bK2Cfy2D8tSNKBrudTpo2omMGtN72DjgyIbQ7DZMYtiwDR1VvO6eAUhy+JOJvF3nIJrOfVizAVA50NUepjgt432SWDjoiXcanMHQNcpqWmlXNz13FBRyGmdDGYrYFIJCTS7vTkFR54xF966RdDnByWd1R/3dRDRF4NbFRF5KgAgAQioWwOvC2f7OmfEjEqbhVPgcV/vSZGw8o6DrBCqyz9eoK4hXEReafSB+Nr7CL4LtXTnDrx', 'x-gorgon': '8404c0760000ca8880c8c5c47f54e7a2b19cc420b6e1a5beb144', 'x-khronos': '1651734302', 'x-ladon': '1DJxJwBJYl7177cQg8nCqNd2nWIMh/Smo1ZzBvsZT0qMGNUr'}
    data_wk={}
    re_wk=requests.post(url=api_wt,headers=header,cookies=cookie,json=data_wk)
    print('领取天气补贴获得金币',end=' ')
    print(re_wk.text)

#搜索赚金币
def sos_wk(cookie,token):
    quer=['新闻直播','凤凰网','中国梦','社会','成都','热搜']
    for i in quer:
        api_s = 'https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/search/done?_rticket=1651677385782&manifest_version_code=11380&iid=2027938897208093&channel=xiaomi_6589_64&isTTWebView=1&device_type=MI+CC+9e&language=zh&host_abi=arm64-v8a&resolution=720*1475&is_db=0&update_version_code=113805&dq_param=2&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&os_api=29&dpi=320&ab_feature=94563%2C102749&ac=mobile&os=android&device_id=2400977487399848&os_version=10&pass_through=default&version_code=1138&session_id=e63e4cde-a846-488d-9bd9-53d9cae8ac25&app_name=gold_browser&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C4002641%2C4012767%2C4023316%2C4054291%2C4055170%2C4057887%2C4064419%2C4079374&homepage_version=1&version_name=1.3.8&plugin=0&device_brand=Xiaomi&ssmix=a&recommend_switch=true&device_platform=android&aid=6589&rom_version=miui_v125_21.4.22'
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

        data_s = {"query": i, "source": "search_bar_inner"}
        re_wk = requests.post(url=api_s, headers=header, cookies=cookie, json=data_s)
        try:
            jb = re_wk.json()["data"]["reward"]
            print(f'搜索文章获得{jb}金币')

        except:
            print('领取失败')
            print(re_wk.text)
        time.sleep(20)
# #看长广告
# def gg(cookie):
#    api='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/cooperate/exciad/done?device_platform=android&os=android&ssmix=a&_rticket=1651718232878&_rticket=1651718232883&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&channel=xiaomi_6589_64&aid=6589&app_name=gold_browser&version_code=1138&version_name=1.3.8&manifest_version_code=11380&update_version_code=113805&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C4002641%2C4012767%2C4023316%2C4054291%2C4055170%2C4057887%2C4064419%2C4079374&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=default&recommend_switch=true&isTTWebView=1&session_id=c5393a27-521d-4105-a21b-3605ae257325&host_abi=arm64-v8a&is_db=0&rom_version=miui_v125_21.4.22&iid=2027938897208093&device_id=2400977487399848&luckydog_base=ovVs9qDe_hzZUV6YPf2uN5do4F0VL6dUuMtYukREQdz1SoEu6GHcHpRFbuV6_bx8O4bMp4nk3Z7zIyp3r8tYexF-lXty5GMsGPTxznQwVVrlUh5bfubWsDcYoE5LKkWhXof8DXTWe-qRT1OpzboNVcBmdYsNduhnVNZE5hsUzWI&luckydog_data=Vdx0a8MWswBLORCydYZlFes6t-6EQ51P1zzuvH2Q9Nfuv2SPpmpM3_AfRDmQFnr_N3j00TW4uyzVK-B4h0QYHQ&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.24&luckycat_version_code=501024&status_bar_height=26'
#    header ={'x-ss-req-ticket': '1651718232886', 'sdk-version': '2', 'x-tt-token': '00e7c316e45f36e6d27298efba196235ad04abf574e0d44e93bcc45a2fec3f9e8614bb4a79a839de34200b32795ca04879837849bfb876179d5562519deb76686bf335a06e97d074a95439513d3a14119f52ba2ed7a369ae0bca891e60fca93905e27-1.0.1', 'passport-sdk-version': '30442', 'x-tt-dt': 'AAAVTXZAUUXUGUDXVORIKIQHPVB7QIPAGR7LR5Y66H5Y2FOMXX7XPUZ42OUMSR4DOR2X6EBROPRB3RGPC57NB7ZVBEAWA35PPABCZUNUBCQEDFVQDYEDEOV7DC6UD2Y5FF33KX3OSQU4KUWDTSDNQJQ', 'x-vc-bdturing-sdk-version': '2.2.0.cn', 'content-type': 'application/json; charset=utf-8', 'x-ss-stub': '8294EBF3B442715224E74B814F02D299', 'x-tt-request-tag': 's=-1;p=0', 'x-ss-dp': '6589', 'x-tt-trace-id': '00-92141cd00d887ad22400ba81b27f19bd-92141cd00d887ad2-01', 'user-agent': 'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion', 'accept-encoding': 'gzip, deflate', 'x-argus': 'X0ih+Vt8nZPLDV8HDUTgYTFagJwFF8kKBnNaJExkHZn/1ZMabvXaHQ3DDknn2hZKnBz1KCg62A3bUgFghxTIEVA7kQg8Pl1M5R474egqtv7OV46BBZQEqlkCaOsNtr09Lp/TNOLtLGY9Fpj81NJ5JaebucFlFWgJTuTtzNhgXnoiy87P2XGv5Ldm4k8DNBaVOqpCAiljK5aKU7EvKZ2C73kky6DCwljNzaUrxMtzJnbyOJaeC6mBHLTJ8oehW4gIVyC6tH7Cmzco0XKdcpW5T1mk', 'x-gorgon': '8404a041000040a2910e7840b7f95ffeda26bbbb21d49f63399e', 'x-khronos': '1651718231', 'x-ladon': 'jEo0X70YxCwz47SOSQUEYUkzWAAoSHqPAVWDtDTQ+g9IwRZR'}
#
#    data_wk = {"task_id":3012,"ad_type":0,"ad_id":12,"exci_extra":{"amount":300,"reward_times":0,"inner_reward_times":0}}
#    re_wk = requests.post(url=api, headers=header, cookies=cookie, json=data_wk)
#    print('看长广告获得金币', end=' ')
#    print(re_wk.text)


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
        print(f'🥇第{ck + 1}账号开始做任务...')
        #领取天气补贴
        weter_wk(json.loads(a_len[ck]), t_token[0])
        time.sleep(5)
        #搜索文章jibi
        sos_wk(json.loads(a_len[ck]), t_token[0])
        time.sleep(5)
        #
