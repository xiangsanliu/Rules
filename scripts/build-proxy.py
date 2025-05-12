import requests
import os


def get_proxy(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')


proxy_urls = []
# proxy_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/proxy.txt')
proxy_urls.append('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/gfw.txt')

if __name__ == '__main__':
    proxy = set()
    
    for url in proxy_urls:
        rules = set(get_proxy(url))
        proxy = proxy.union(rules)
    proxy = list(proxy)
    proxy.sort()
    proxy_file = open(os.getcwd() + '/temp/proxy.txt', mode='w', encoding='utf-8')
    for line in proxy:
        if not line.startswith('#') and len(line) > 0:
            proxy_file.write('%s,PROXY\n' % line)
    proxy_file.close()
    print('The proxy rule has been built successfully! Rule size: {}.'.format(len(proxy)))
