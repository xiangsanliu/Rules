import requests


def get_ad(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')

reject_url = 'https://cdn.jsdelivr.net/gh/ACL4SSR/ACL4SSR@master/Clash/BanAD.list'

if __name__ == '__main__':
    reject = get_ad(reject_url)
    ad_file = open('clash/adlite.txt', mode='w', encoding='utf-8')
    for line in reject:
        if not line.startswith('#') and not line.startswith('DOMAIN-KEYWORD') and len(line) > 0:
            line = line.replace('DOMAIN-SUFFIX,', '')
            ad_file.write('.%s\n' % line)
    ad_file.close()
    print('The ad rule has been built successfully! Rule size: {}.'.format(len(reject)))
