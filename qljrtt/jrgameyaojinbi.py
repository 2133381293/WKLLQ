'''
cron:0 0 7,12,18 * * ?
new Env('今日头条2种树摇金币.')
'''
#jrtoken   jrcookie变量名
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
    api = 'https://minigame3-normal-lf.zijieapi.com/ttgame/game_orchard/fortune_tree/double_reward?watch_ad=1&status=1&is_first_free=0&os_version=10&version_code=875&device_id=2400977487399848&iid=3382530259551581&app_name=news_article_lite&device_platform=android&device_type=MI+CC+9e&channel=lite_xiaomi_64&aid=35&version_name=8.7.5&update_version_code=87507'
    header={'user-agent': 'Mozilla/5.0 (Linux; Android 10; MI CC 9e Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 NewsArticle/8.7.5.0 ToutiaoMicroApp/2.31.1.1 PluginVersion/874011', 'content-type': 'application/json', 'sdk-version': '2', 'x-tt-token': token, 'passport-sdk-version': '30442', 'x-tt-request-tag': 's=-1;p=1', 'x-ss-dp': '35', 'x-tt-trace-id': '00-279b88820101391fd24699493c6c0023-279b88820101391f-01', 'referer': 'https', 'accept-encoding': 'gzip, deflate, br', 'x-argus': 'ZOJgB0Ew6IRdxPP2DSVj0A65a1xjznJ0oEntyEaQ8p/A3bwNRGi7IsDaJhSnaIWxVEEygqwIFLA7WteHa9gLPFdTjGbqjlKMbI7j4ahd6Dh2+DvC7R2ymeKg4xA2mMAjCm7OmKoDivHfj3XMjroB56X3fGshHHNNmwSAaYp0cojRymYEIcFhfKOEo3sTT7vzApXLBCBjs4ZucEIdlM9vYqDQ', 'x-gorgon': '840440fb00002b9f576ffefab7b04b4381fc0ffdca7a81f1b59b', 'x-khronos': '1649931943', 'x-ladon': 'jPpTM+VyNqwhAWnsv8IpkIT04shmg68bbQzsYLnB1mD2nbxF'}
    a = 0
    for i in range(50):

        re = requests.get(url=api, headers=header, cookies=cookie)
        try:
            jb=re.json()['data']['reward_num']
            print(f'种树摇金币获得{jb}')

            a += 1
        except:
            print(f'失败\n{re.text}')
            with open('jxrz.txt', 'a') as f:
                f.write(str(a)+'\n')
            sys.exit()
        aa = random.randint(68, 125)
        print(f'等待{aa}秒继续')
        time.sleep(a)


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
            print(f'⚠️第{ck+1}账号开始做任务')
            kbx(json.loads(a_len[ck]), t_token[0])
            time.sleep(6)