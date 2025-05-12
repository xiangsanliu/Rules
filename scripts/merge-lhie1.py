import os
import time
import requests


def get_index(lines):
    index = 0
    for line in lines:
        index += 1
        if line == '[Rule]\n':
            return index


def get_lhie1():
    res = requests.get(
        'https://cdn.jsdelivr.net/gh/lhie1/Rules@master/Shadowrocket/Complete.conf')
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')

if __name__ == '__main__':
    parent_path = os.getcwd()
    file_netease = open(parent_path + '/temp/netease.txt', mode='r')
    file_merge = open(parent_path + '/merge-lhie1.conf', mode='w')
    lines_1 = get_lhie1()
    lines_2 = file_netease.readlines()

    file_merge.write(
        "# Update at " + time.strftime("%Y-%m-%d %H:%M:%S %Z") + "\n")

    flag = True
    for rule_1 in lines_1:
        if rule_1.startswith('# > Netease Music'):
            flag = False
        if not flag and len(rule_1) < 1:
            flag = True

        if rule_1.startswith('GEOIP'):
            file_merge.write('# > Netease Music Unblock\n')
            for rule_2 in lines_2:
                file_merge.write(rule_2)
            file_merge.write('\n')
        if flag:
            file_merge.write(rule_1 + '\n')

    print('lhie1/Complete.conf merged')

    file_netease.close()
    file_merge.close()
