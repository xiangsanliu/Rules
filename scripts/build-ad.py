import requests
import os


def get_ad(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')

reject_url = 'https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/reject.txt'

if __name__ == '__main__':
    reject = get_ad(reject_url)
    ad_file = open(os.getcwd() + '/temp/ad.txt', mode='w', encoding='utf-8')
    for line in reject:
        if not line.startswith('#') and len(line) > 0:
            ad_file.write('%s,REJECT\n' % line)
    ad_file.close()
    print('The ad rule has been built successfully! Rule size: {}.'.format(len(reject)))
