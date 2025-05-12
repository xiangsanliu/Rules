import requests
import os
import re
import base64


def get_netease():
    res = requests.get(
        # 'https://cdn.jsdelivr.net/gh/blackmatrix7/ios_rule_script/rule/Shadowrocket/NetEaseMusic/NetEaseMusic.list'
#         'https://cdn.jsdelivr.net/gh/ACL4SSR/ACL4SSR@master/Clash/Ruleset/NetEaseMusic.list'
        'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/NetEaseMusic/NetEaseMusic.list'
        )
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text


if __name__ == '__main__':
    gfw = get_netease()
    gfw = gfw.split('\n')
    gfw_file = open(os.getcwd() + '/temp/netease.txt', mode='w', encoding='utf-8')
    for line in gfw:
        if not line.startswith('#') and len(line) > 0:
            gfw_file.write('%s,网易云音乐\n' % line)
    gfw_file.close()
