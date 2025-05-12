import base64
import requests
import urllib
import os

# node file from https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic

def get_node():
    res = requests.get("https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic/raw/master/Shadowrocket/shadowrocket-server.txt")
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text

if __name__ == '__main__':
    node = str(get_node()) + '=='
    node = base64.b64decode(node).decode('utf-8')
    node = node.split("\n")[0].split('#')[0]
    node = node + '#' + urllib.parse.quote('网易云音乐')
    node = base64.b64encode(node.encode()).decode('utf-8')
    node_file = ad_file = open(os.getcwd() + '/node.txt', mode='w', encoding='utf-8')
    node_file.write(node)
    node_file.close()
    print('Netease node converted!')
    