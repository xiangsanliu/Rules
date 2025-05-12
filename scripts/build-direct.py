import requests
import os


def get_direct(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')


direct_urls = []
direct_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/direct.txt')
direct_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/private.txt')
direct_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/apple.txt')
direct_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/icloud.txt')
# direct_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/cncidr.txt')



if __name__ == '__main__':
    direct = set()
    
    for url in direct_urls:
        rules = set(get_direct(url))
        direct = direct.union(rules)
    direct = list(direct)
    direct.sort()
    direct_file = open(os.getcwd() + '/temp/direct.txt', mode='w', encoding='utf-8')
    for line in direct:
        if not line.startswith('#') and len(line) > 0:
            direct_file.write('%s,DIRECT\n' % line)
    direct_file.close()
    print('The direct rule has been built successfully! Rule size: {}.'.format(len(direct)))
