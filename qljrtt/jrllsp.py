'''
cron:0 0 6,7,8,9,10,11,13,15,18,21 * * ?
new Env('今日头条2浏览商品和看广告,认真阅读')
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
    api_data = 'https://api5-normal-lf.toutiaoapi.com/luckycat/lite/v1/ecommerce/done_task?pass_through=default&is_pad=0&act_token=kd_q6VVcPtcoVSmG6MEHoJ5vjH9SkhQupROwpKqQN-KjQoqLkFEfqt56Q1zOFe9MhQ6SCdU_NKWJIRgB4CR3HA&act_hash=4823f2b8e1306558044de925bb4ec496&cookie_base=47pel193Jpjuq-LHeqpC12RYoJA3rp9Tg5HhlC3l9uKZQ383khdntBeI9eyJqwSIBvBwXW_betaiERpNmPwdhg&cookie_data=QUTD9qyNAnn3Q58373NepQ&iid=4438069513032238&device_id=2400977487399848&ac=4g&channel=lite2_tengxun_64&aid=35&app_name=news_article_lite&version_code=878&version_name=8.7.8&device_platform=android&os=android&ab_version=668908%2C4061161%2C668907%2C4061157%2C668905%2C4061123%2C668906%2C4061131%2C668904%2C4061108%2C668903%2C4061151%2C1859937%2C4006186%2C2220242%2C3596061%2C4021758&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=z1&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&manifest_version_code=8780&resolution=720*1475&dpi=320&update_version_code=87809&_rticket=1651559332803&sa_enable=0&dq_param=2&plugin_state=139681997156381&isTTWebView=1&session_id=b6795be1-828b-4d98-b63f-9eda5272fde3&host_abi=arm64-v8a&tma_jssdk_version=2.8.0.16&rom_version=miui_v125_21.4.22&cdid=04499bcb-4f19-4ea3-ba61-3e74477f1c17&polaris_version=1.0.5&status_bar_height=26&luckydog_base=pdSHqY_uSNxlpanTlTXkPCoxA59bPsQjVOfHDEXUCVRas5TkGH2rui0vXth5O-ByfaSDjREINx9xR8Wcv9cb4FZtyQpx0byVxhPQpPZm9HJRYDuERccmhRV4GPyk4CIZ7067ZiQLYOHfr_5Suj7fJjskyLPav2nT6Mmt45W0q0UQrr4UmJ3malMC4PhWjqcHRL6MrR6OLFVM9n0S25s10i_lwPo-rADZ9zAYpIjx4FE&luckydog_data=s7uHEQJmFgOEL79oLAjY9S6_mDPpOKTa8HVZIJsuYg8GAAIT7dvRIB1AxhOXANHAHlCeCg0zS8Je6FnIPvrahFHpWrs-5xyOt0Kt-4zpzJo&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.26&luckycat_version_code=501026'
    header = {'Host': 'api5-normal-lf.toutiaoapi.com', 'content-length': '2', 'x-ss-req-ticket': '1651559332809',
              'x-vc-bdturing-sdk-version': '2.2.1.cn',
              'x-tt-dt': 'AAAXTL5IBRDJCZRJ4JQHFAZ2ZJLQ4ZO6P47W7HSJGSSDZWNDSRHN2NNZJFI7UH2YZWT4JCQ76TG7PGHINJNO5QQORQMKBOJXWSQ5447MPPMDVY6UTL4TZBMTJ75JQ6DRMXML5W757ABIHMT7NSRXZSA',
              'sdk-version': '2',
              'x-tt-token': token,
              'passport-sdk-version': '30442',
              'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 10; MI CC 9e MIUI/21.4.22) NewsArticle/8.7.8 cronet/TTNetVersion',
              'content-type': 'application/json', 'x-ss-stub': '99914B932BD37A50B983C5E7C90AE93B',
              'x-tt-store-region': 'cn-cq', 'x-tt-store-region-src': 'did', 'x-tt-request-tag': 's=1;p=0',
              'x-ss-dp': '35', 'x-tt-trace-id': '00-889b7d580d887ad22400ba8dd01b0023-889b7d580d887ad2-01',
              'accept-encoding': 'gzip, deflate, br',
              'x-argus': 'ytnIx2uNODjcjH5q2fedDJBPyhESbg1qOfPLddjn5dLBtSSZX/oV7MMeFfKWIW9NjV1jdoLkoviscE95VJ2o1kQrdNDkG+XGLkHiln9HsKc9xOXpaOc/Pi/kA7N5Osb+XA+Y/HkIwg6cEnHiFQ1oSS53PLInzgy94JhCNT5xj3EYn5W5vpwj79dAyuRyL8PrmoXW9LBKRkvV/If/6gFak8+QY/MH9xk0S3qGdmIo3ZxnUuBbvop1x2Yu3349ZCQMlq7kmBo+4ZE7NiRt2HoCTisb',
              'x-gorgon': '8404203100000ee4522115c7a7e14c40d905f014f3e73736f82a', 'x-khronos': '1651559331',
              'x-ladon': 'i3PCWpmhbsxHpKqPlElHBXWB4zat5Atn4HGghMhZN3lhYYeH'}
    data = {}
    re_json = requests.post(url=api_data, headers=header, cookies=cookie, json=data)
    try:
        jb = re_json.json()['data']['score_amount']
        print(f'浏览商品获得{jb}金币')
    except:
        print('获得金币失败')
        print(re_json.text)
#看广告
def gg(cookie,token):
    url = 'https://api5-normal-lf.toutiaoapi.com/luckycat/lite/v1/task/done/excitation_ad?pass_through=default&is_pad=0&act_token=CbKKB2kKaYifAocl6r_qSJsPlM90YahQz2D4Lhnc-xxC7Ws9DiFXMVqQbeHaXtCHaEZGoomXPJ3eiPg_OZN3zA&act_hash=4823f2b8e1306558044de925bb4ec496&cookie_base=WCilq_0e2W-djHKxuMgfck0jZ6qpCgtEronl1r0f1NdjjoFmNE_kKKapK18JpyoEtI6DIvOwfgF-kDvpP0Wbs0XR0MhqTONZy040k7SdCBw&cookie_data=KWD6GOF-mlEWW7t0kHhC2g&iid=3382530259551581&device_id=2400977487399848&ac=wifi&channel=lite_xiaomi_64&aid=35&app_name=news_article_lite&version_code=875&version_name=8.7.5&device_platform=android&os=android&ab_version=668905%2C3937366%2C668904%2C3937345%2C668906%2C3937374%2C668903%2C3937392%2C1859937%2C668908%2C3937402%2C668907%2C3937398%2C3801463%2C2220242%2C3520490%2C3596061%2C3936294%2C3958946&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=z2&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&manifest_version_code=8750&resolution=720*1475&dpi=320&update_version_code=87507&_rticket=1649812583577&sa_enable=0&dq_param=2&plugin_state=139681997156381&isTTWebView=1&session_id=b34c9a6a-f03c-4601-9164-13f2676d9a3d&host_abi=arm64-v8a&tma_jssdk_version=2.8.0.16&rom_version=miui_v125_21.4.22&cdid=6b68202d-3da9-4ee1-909e-8ebe5337dd3d&polaris_version=1.0.5&status_bar_height=26&luckydog_base=WyxIFYW3v6lWtQzUNYpnswSGhDsj5LNxi9WHIes_Lk_pEBc3MEJt0H0SwyQmncuserSNxC2Q_bU_toMECP3MT5oCCEoMLxw4Bux8sE1XNNwnSZrujTOgcgTV1jgpapD1Q5T2kTt4UomT_UYIyCcJ6HiKePWxxHoRNa6q0y9y-8M&luckydog_data=LcTRkETRI9xqIpSJ6aAD9lPviR7BjjMGkaP0EDeu_jD2SdwRno9UgCtflOPPhko763D8tBiPoxjH-mhRaWSZH_dV9gzHWubAwz0zV56Lurs&luckydog_token=Khh2F_xwYp-MqVYQlwV5oyXSW_JLoQWp9nd_fr6OyLQlbhT0oFEUEwsoqa6vQ3RX&luckydog_sdk_version=5.0.1-rc.11&luckydog_settings_version=15&luckycat_version_name=5.0.1-rc.20&luckycat_version_code=501020'
    header = {'Host': 'api5-normal-lf.toutiaoapi.com', 'content-length': '2', 'x-ss-req-ticket': '1651559332809',
              'x-vc-bdturing-sdk-version': '2.2.1.cn',
              'x-tt-dt': 'AAAXTL5IBRDJCZRJ4JQHFAZ2ZJLQ4ZO6P47W7HSJGSSDZWNDSRHN2NNZJFI7UH2YZWT4JCQ76TG7PGHINJNO5QQORQMKBOJXWSQ5447MPPMDVY6UTL4TZBMTJ75JQ6DRMXML5W757ABIHMT7NSRXZSA',
              'sdk-version': '2',
              'x-tt-token': token,
              'passport-sdk-version': '30442',
              'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 10; MI CC 9e MIUI/21.4.22) NewsArticle/8.7.8 cronet/TTNetVersion',
              'content-type': 'application/json', 'x-ss-stub': '99914B932BD37A50B983C5E7C90AE93B',
              'x-tt-store-region': 'cn-cq', 'x-tt-store-region-src': 'did', 'x-tt-request-tag': 's=1;p=0',
              'x-ss-dp': '35', 'x-tt-trace-id': '00-889b7d580d887ad22400ba8dd01b0023-889b7d580d887ad2-01',
              'x-argus': 'ytnIx2uNODjcjH5q2fedDJBPyhESbg1qOfPLddjn5dLBtSSZX/oV7MMeFfKWIW9NjV1jdoLkoviscE95VJ2o1kQrdNDkG+XGLkHiln9HsKc9xOXpaOc/Pi/kA7N5Osb+XA+Y/HkIwg6cEnHiFQ1oSS53PLInzgy94JhCNT5xj3EYn5W5vpwj79dAyuRyL8PrmoXW9LBKRkvV/If/6gFak8+QY/MH9xk0S3qGdmIo3ZxnUuBbvop1x2Yu3349ZCQMlq7kmBo+4ZE7NiRt2HoCTisb',
              'x-gorgon': '8404203100000ee4522115c7a7e14c40d905f014f3e73736f82a', 'x-khronos': '1651559331',
              'x-ladon': 'i3PCWpmhbsxHpKqPlElHBXWB4zat5Atn4HGghMhZN3lhYYeH'}
    data = {
        "ad_id": 11, "amount": 461, "ad_rit": "11", "extra_data": {"enter_from": "task"},
        "task_key": "excitation_ad", "extra": {"track_id": "7085890886882084878"}, "task_id": "210",
        "ad_alias_position": "coin", "is_post_login": 'false', "ad_from": "coin", "score_source": 1,
        "coin_count": 461,
        "exci_extra": {"cid": 1729596394142755, "req_id": "202204130915590102081020701726BDF3", "rit": 20047}
    }
    re = requests.post(url=url, headers=header, data=json.dumps(data), cookies=cookie)
    print(re.text)
#认正阅读
def rzread(cookies,token):
    def read(g_id):
        api = 'https://api3-normal-lf.toutiaoapi.com/score_task/v1/task/get_read_bonus/'
        pdata = {'pass_through': 'default', 'is_pad': '0',
                 'act_token':'CbKKB2kKaYifAocl6r_qSJsPlM90YahQz2D4Lhnc-xxC7Ws9DiFXMVqQbeHaXtCHaEZGoomXPJ3eiPg_OZN3zA',
                 'act_hash': '4823f2b8e1306558044de925bb4ec496',
                 'cookie_base': 'WCilq_0e2W-djHKxuMgfck0jZ6qpCgtEronl1r0f1NdjjoFmNE_kKKapK18JpyoEtI6DIvOwfgF-kDvpP0Wbs0XR0MhqTONZy040k7SdCBw',
                 'cookie_data': 'KWD6GOF-mlEWW7t0kHhC2g', 'iid': '3382530259551581', 'device_id': '2400977487399848',
                 'ac': 'mobile', 'channel': 'lite_xiaomi_64', 'aid': '35', 'app_name': 'news_article_lite',
                 'version_code': '875', 'version_name': '8.7.5', 'device_platform': 'android', 'os': 'android',
                 'ab_version': '668907%2C4061157%2C668905%2C4061123%2C668906%2C4061131%2C668904%2C4061108%2C668903%2C4061151%2C1859937%2C668908%2C4061161%2C2220242%2C3596061%2C3958946%2C4021758%2C3801463%2C4006186',
                 'ab_client': 'a1%2Ce1%2Cf2%2Cg2%2Cf7', 'ab_group': 'z2', 'ab_feature': 'z1', 'abflag': '3',
                 'ssmix': 'a', 'device_type': 'MI%20CC%209e', 'device_brand': 'Xiaomi', 'language': 'zh',
                 'os_api': '29', 'os_version': '10', 'manifest_version_code': '8750', 'resolution': '720*1475',
                 'dpi': '320', 'update_version_code': '87507', '_rticket': '1650937418991', 'sa_enable': '0',
                 'dq_param': '2', 'plugin_state': '139681992962077', 'isTTWebView': '1',
                 'session_id': 'ec93e9b3-0f70-47fb-9a97-c25773cb0e44', 'host_abi': 'arm64-v8a',
                 'rom_version': 'miui_v125_21.4.22', 'cdid': '6b68202d-3da9-4ee1-909e-8ebe5337dd3d',
                 'polaris_version': '1.0.5', 'status_bar_height': '26',
                 'group_id': g_id, 'impression_type': 'push'}
        headers = {'Host': 'api3-normal-lf.toutiaoapi.com', 'accept-encoding': 'gzip',
                   'x-ss-req-ticket': '1650937418994', 'x-vc-bdturing-sdk-version': '2.2.1.cn',
                   'x-tt-dt': 'AAAYT5BJ3RYHDLFICUYVNVTPHLIGSAAFYNO4XP7BLJKOOUJSN2AVQTQPRLYU5M7QGYPYG3T6VRTEBBOSS4H6SHWNWIIMMLGGP4HXTK6KZZEW4NRHWUNBAVVZTOMUX5QRFVFKOMWEZM3CPVHAQBDGRTA',
                   'sdk-version': '2',
                   'x-tt-token':token,
                   'passport-sdk-version': '30442', 'x-tt-store-region': 'cn-cq', 'x-tt-store-region-src': 'did',
                   'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 10; MI CC 9e MIUI/21.4.22) NewsArticle/8.7.5 tt-ok/3.10.0.2',
                   'x-ladon': 'nFcbS9vfbtR6JXqoMNEeTau+Hi/MiC2h2rUoMLQncZPamytj', 'x-khronos': '1650937418',
                   'x-argus': '6qHwJ2NC8yIZnE7A1AqmU4iJKSomLBpSKw2zkZhdjmTqPyTB17CQYJf5FljTly49ycm7TubMADm/UwquQ59kTXKGSnZD7UyghqRKV7XDQQtUWniH2IiYozegNbJUbc8n4eg+EojRqQ8TsoImkRlObViE+Y+t95ZxKe5nI5XG0d4ChyTFCdTvrNw5ESxxSnKJR3hNhiNETXePltZpSeHCemwc7YKfUXDM/9x21nswIr9GxodPOK1lCdIlMdaM+RmO2sORs46Wf9OFefDJ0K/pbJki',
                   'x-gorgon': '8404e0d1000048e9316847636358ccacdbe6cc8aa11aa721aa70'}
        r = requests.get(url=api, headers=headers, cookies=cookies, params=pdata)
        try:
            jb=r.json()['data']['score_amount']
            print(f'奖励认真阅读的你{jb}')
        except:
            print('阅读失败')
            sys.exit()
    def pagemid():
        api = 'https://search5-search-hl.toutiaoapi.com/search/suggest/homepage_suggest/?suggest_params=%7B%22suggest_word%22%3A%7B%22from%22%3A%22feed%22%2C%22sug_category%22%3A%22__all__%22%7D%2C%22refresh_type%22%3A0%2C%22need_gold_count%22%3A%221%22%7D&recom_cnt=2&iid=3382530259551581&device_id=2400977487399848&ac=4g&channel=lite_xiaomi_64&aid=35&app_name=news_article_lite&version_code=875&version_name=8.7.5&device_platform=android&os=android&ab_version=1859937%2C668908%2C3937402%2C668907%2C3937398%2C668905%2C3937366%2C668906%2C3937374%2C668904%2C3937345%2C668903%2C3937392%2C3801463%2C4006186%2C2220242%2C3520490%2C3596061%2C3958946&ab_client=a1%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=z2&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+CC+9e&device_brand=Xiaomi&language=zh&os_api=29&os_version=10&manifest_version_code=8750&resolution=720*1475&dpi=320&update_version_code=87507&_rticket=1650633775147&sa_enable=0&dq_param=2&plugin_state=139681997156381&isTTWebView=1&session_id=0336438a-09b6-40f9-a69a-98be8461b398&host_abi=arm64-v8a&tma_jssdk_version=2.8.0.16&rom_version=miui_v125_21.4.22&cdid=6b68202d-3da9-4ee1-909e-8ebe5337dd3d'

        headers = {'x-ss-req-ticket': '1650633775151', 'x-vc-bdturing-sdk-version': '2.2.1.cn',
                   'x-tt-dt': 'AAARVPQGU33KSUPNNKWKXWPKDGO22LMQCFJD7DUFJ6EOV6QE4QUJDF5KAJQO7GXJUIHSOERH24MZ3UXP4IK4K3QF63CMAW47GHDK5KPBLNH42I64DP6U3PCV6OZ3O5FNVJR2N5TD6N6Q44XHYUHUBIY',
                   'sdk-version': '2',
                   'x-tt-token': token,
                   'passport-sdk-version': '30442',
                   'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 10; MI CC 9e MIUI/21.4.22) NewsArticle/8.7.5 cronet/TTNetVersion',
                   'x-tt-store-region': 'cn-sc', 'x-tt-store-region-src': 'did', 'x-tt-request-tag': 's=1;p=0',
                   'x-ss-dp': '35', 'x-tt-trace-id': '00-517099bb0d887ad22400ba82d1e20023-517099bb0d887ad2-01',
                   'accept-encoding': 'gzip, deflate, br',
                   'x-argus': 's6ryIzjz//vZGys5Nqj+sGQTM+oZJLiWy9ADVUjYoqWHdcJBbmcVwJdlUWMG8oBTV/2UPnLN8FauuDwG9uTyVp/gorNF8IFrP9U78Rj2zvDmnotOHwe0Kx1OhQVR88Ry2yck4sCGAvFch10cF32utwebO06Ad0quQxshALtsoa2b/d5F8YCpjpaxn7RZF9IwXF/3n4eeTZsZU3WU2Fd4Yy+3pX8XDYsobM4wrgBEfHlvksqrr5tRiomsy5DB6dBPqrTe/rhURQvgVo44i4UNgfJV',
                   'x-gorgon': '840420010000654a04c913f5d09336ee71c473fc404d27106673', 'x-khronos': '1650633774',
                   'x-ladon': '+/f3OuiynMvCrFnK5ZPx66zgPSpQAVtPcxwQ7VGLAsyYyB2y'}
        r1 = requests.get(url=api, headers=headers, cookies=cookies)
        try:
            ra = r1.json()
            for i in ra['data']['suggest_words']:
                time.sleep(15)
                read(i['id'])
                break
        except:
            print('错误获取id')
            time.sleep(60)
    pagemid()
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
            time.sleep(30)
            print('\n')
            print('尝试开始看一次广告')
            gg(json.loads(a_len[ck]), t_token[0])
            time.sleep(45)
            print('\n')
            print('开始认真阅读一次')
            rzread(json.loads(a_len[ck]), t_token[0])
            time.sleep(6)