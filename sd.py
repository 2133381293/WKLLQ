'''
cron:35 15 * * *
new Env('今日头条测试')
'''
import requests #line:6
import random ,sys ,json ,time #line:7
def file_token ():#line:9
    OOOOOO00OOOO0OOO0 =[]#line:10
    try :#line:11
        O00O00O0O0OO0000O =open ('/ql/config/env.sh','r')#line:12
        for OOOOO0OOO0O0OO000 in O00O00O0O0OO0000O .readlines ():#line:13
            if 'xtttoken'in OOOOO0OOO0O0OO000 :#line:15
                OOOOOO00OOOO0OOO0 +=[OOOOO0OOO0O0OO000 .replace ('export','').replace ('"','').replace ('\n','').replace ('xtttoken=','').strip ()]#line:17
        O00O00O0O0OO0000O .close ()#line:18
        return OOOOOO00OOOO0OOO0 #line:19
    except :#line:20
        print ('没有找到变量文件，或者token填写错误')#line:21
        sys .exit ()#line:22
def file_ck ():#line:24
    OO000OO0O0O0000O0 =[]#line:25
    try :#line:26
        O0OOOO0O0OO00O00O =open ('/ql/config/env.sh','r')#line:27
        for O0O00OOO00OOO0000 in O0OOOO0O0OO00O00O .readlines ():#line:28
            if 'wkcookie'in O0O00OOO00OOO0000 :#line:30
                OO000OO0O0O0000O0 +=[O0O00OOO00OOO0000 .replace ('export','').replace ('"','').replace ('\n','').replace ('wkcookie=','').strip ()]#line:31
        O0OOOO0O0OO00O00O .close ()#line:32
    except :#line:33
        print ('没有找到变量文件，或者cookies填写错误')#line:34
        sys .exit ()#line:35
    O00O0OOO0O0O00OO0 =[]#line:37
    try :#line:38
        for O0O00OOO00OOO0000 in range (len (OO000OO0O0O0000O0 )):#line:39
            if len (OO000OO0O0O0000O0 [O0O00OOO00OOO0000 ])<10 :#line:41
                continue #line:42
            if '&'in OO000OO0O0O0000O0 [O0O00OOO00OOO0000 ]:#line:44
                OO000O0OOO0000000 =OO000OO0O0O0000O0 [O0O00OOO00OOO0000 ].split ('&')#line:45
                for O0O0O000OO000OOO0 in OO000O0OOO0000000 :#line:46
                    O0OO0O0O00O0O00OO =O0O0O000OO000OOO0 .replace ('=','":"').replace (';','","')#line:47
                    O0OOO0OO000O00O00 ='{"'+O0OO0O0O00O0O00OO +'"}'#line:48
                    O00O0OOO0O0O00OO0 +=[O0OOO0OO000O00O00 ]#line:49
                break #line:50
            O0OO0O0O00O0O00OO =OO000OO0O0O0000O0 [O0O00OOO00OOO0000 ].replace ('=','":"').replace (';','","')#line:52
            O0OOO0OO000O00O00 ='{"'+O0OO0O0O00O0O00OO +'"}'#line:53
            O00O0OOO0O0O00OO0 +=[O0OOO0OO000O00O00 ]#line:54
        return O00O0OOO0O0O00OO0 #line:55
    except :#line:56
        print ('cookie信息填写错误请检查')#line:57
        sys .exit ()#line:58
def et (O00O00OOO0OOOO000 ,OOOOOO0OOOO00OO00 ):#line:61
    OOO00O0000OOOOOO0 ='https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/eat/done?_request_from=web&scm_build_version=1.0.0.76&device_platform=android&os=android&ssmix=a&_rticket=1651642326315&_rticket=1651642326320&cdid=7dd3e0aa-d898-4f1e-8c40-793215a88972&channel=xiaomi_6589_64&aid=6589&app_name=gold_browser&version_code=1138&version_name=1.3.8&manifest_version_code=11380&update_version_code=113805&ab_version=3109096%2C3330432%2C3330612%2C3669867%2C3698801%2C3835809%2C4057700%2C3525279%2C3718419%2C3765027%2C3836344%2C3932103%2C3949606%2C3958727%2C3978800%2C4002641%2C4004664%2C4012767%2C4023316%2C4054291%2C4055170%2C4057887%2C4064419%2C4079374&ab_feature=94563%2C102749&resolution=720*1475&dpi=320&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&ac=mobile&homepage_version=1&dq_param=2&plugin=0&pass_through=default&recommend_switch=true&isTTWebView=1&session_id=dd038e89-566b-47a2-a631-b6da6fc552ca&host_abi=arm64-v8a&is_db=0&rom_version=miui_v125_21.4.22&iid=2027938897208093&device_id=2400977487399848&luckydog_base=g14lyWliXe8MTKYLvfWOnEWIXz6hFqQ9IdTKcjS1WsOQ7JA0K2zIatL5MejeAtm3qAQcSBNWk6dKFy4StCr29MO9A_KgYF9FA6qyjoZcHRYuiwZWmElVyGQzkTrQAqeNmK1iN6IBDmOQgxDgCT3cE1wHXPlwTQas4pjlGx218uY&luckydog_data=u9jvYPXk5SqG2C5flAUt2lusHs5yEy8geNWgTE0zWPDGpN7367fs-tFDZsU3nL7ExwigI-G3k_HVcv4cW_5JTxjB7SUhHe5o77x9ORSVo8k&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.24&luckycat_version_code=501024&status_bar_height=26'#line:62
    O00OOO0O0OOO0O00O ={'x-ss-req-ticket':'1651734304479','sdk-version':'2','x-tt-token':OOOOOO0OOOO00OO00 ,'passport-sdk-version':'30442','x-tt-dt':'AAAVTXZAUUXUGUDXVORIKIQHPVB7QIPAGR7LR5Y66H5Y2FOMXX7XPUZ42OUMSR4DOR2X6EBROPRB3RGPC57NB7ZVBEAWA35PPABCZUNUBCQEDFVQDYEDEOV7DC6UD2Y5FF33KX3OSQU4KUWDTSDNQJQ','x-vc-bdturing-sdk-version':'2.2.0.cn','content-type':'application/json; charset=UTF-8','x-ss-stub':'99914B932BD37A50B983C5E7C90AE93B','x-tt-request-tag':'s=1;p=0','x-ss-dp':'6589','x-tt-trace-id':'00-9309587a0d887ad22400ba863f4419bd-9309587a0d887ad2-01','user-agent':'com.cat.readall/11380 (Linux; U; Android 10; zh_CN; MI CC 9e; Build/QKQ1.190910.002; Cronet/TTNetVersion','accept-encoding':'gzip, deflate','x-argus':'HTWRIySW9SKZji8Swd+kct4fBt4R/YT9UShPi8bK2Cfy2D8tSNKBrudTpo2omMGtN72DjgyIbQ7DZMYtiwDR1VvO6eAUhy+JOJvF3nIJrOfVizAVA50NUepjgt432SWDjoiXcanMHQNcpqWmlXNz13FBRyGmdDGYrYFIJCTS7vTkFR54xF966RdDnByWd1R/3dRDRF4NbFRF5KgAgAQioWwOvC2f7OmfEjEqbhVPgcV/vSZGw8o6DrBCqyz9eoK4hXEReafSB+Nr7CL4LtXTnDrx','x-gorgon':'8404c0760000ca8880c8c5c47f54e7a2b19cc420b6e1a5beb144','x-khronos':'1651734302','x-ladon':'1DJxJwBJYl7177cQg8nCqNd2nWIMh/Smo1ZzBvsZT0qMGNUr'}#line:73
    OOO0000O0O0000000 ={"enable_preload_exciting_video":0 }#line:74
    OOOO0O00O00O0O0O0 =requests .post (url =OOO00O0000OOOOOO0 ,headers =O00OOO0O0OOO0O00O ,cookies =O00O00OOO0OOOO000 ,json =OOO0000O0O0000000 )#line:75
    try :#line:76
        O00000O00OO00O00O =OOOO0O00O00O0O0O0 .json ()['data']["score_amount"]#line:77
        print (f'领取吃饭补贴获得金币{O00000O00OO00O00O}')#line:78
    except :#line:79
        print (OOOO0O00O00O0O0O0 .text )#line:80
        sys .exit ()#line:81
if __name__ =="__main__":#line:86
    a_len =file_ck ()#line:88
    if len (a_len )==0 :#line:89
        print ('一个ck也没有,请检查账号信息')#line:90
        sys .exit ()#line:91
    print (f'🔔🔔🔔共检测到{len(a_len)}个ck🔔🔔🔔')#line:92
    t_token =file_token ()#line:94
    if len (t_token )==0 :#line:95
        print ('请设置环境变量 token ')#line:96
        sys .exit ()#line:97
    for ck in range (len (a_len )):#line:99
            print (f'⚠️第{ck+1}账号开始做任务')#line:100
            et (json .loads (a_len [ck ]),t_token [0 ])#line:101
            time .sleep (5 )