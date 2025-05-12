import os
import time
import requests


def get_index(lines):
    index = 0
    for line in lines:
        index += 1
        if line.startswith('FINAL'):
            return index - 1
    return index
        
def get_h2y():
    res = requests.get(
        'https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist_ad.conf')
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')


if __name__ == '__main__':
    file_2 = open('temp/netease.txt', mode='r')
    file_merge = open('merge-h2y.conf', mode='w')
    lines_1 = get_h2y()
    lines_2 = file_2.readlines()
    index1 = get_index(lines_1)

    if index1 == 0:
        file_2.close()
        file_merge.close()
        exit()
        
    for i in range(0, index1):
        file_merge.write(lines_1[i])
        file_merge.write('\n')
    file_merge.write('\n')
    
    
    file_merge.write('# 网易云解锁\n')
    for i in range(0, len(lines_2)):
        file_merge.write(lines_2[i])

    
    file_merge.write('\n')
    for i in range(index1, len(lines_1)):
        file_merge.write(lines_1[i])
        file_merge.write('\n')

    print('h2y/sr_top500_banlist_ad.conf merged')

    file_2.close()
    file_merge.close()
