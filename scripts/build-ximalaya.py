import requests
import os


def get_conf():
    res = requests.get(
        'https://gitlab.com/ddgksf2013/Cuttlefish/-/raw/master/Rewrite/AdBlock/Ximalaya.conf'
    )
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text


def get_script_name(script_url):
    index1 = script_url.rfind("/")
    index2 = script_url.rfind(".")
    return script_url[index1 + 1:index2]


head = """
name: 喜马拉雅去广告
desc: 喜马拉雅去广告, @ https://gitlab.com/ddgksf2013/Cuttlefish/-/raw/master/Rewrite/AdBlock/Ximalaya.conf

http:
  mitm:
    - "*.xima*.*"
    - ".xmcdn.*"
    
"""

script_url_set = set()

if __name__ == '__main__':
    conf = get_conf()
    conf = conf.split('\n')
    ximalaya = open("sgmodule/ximalaya.stoverride", mode='w', encoding='utf-8')
    rewrites = []
    scripts = []
    for line in conf:
        if line.startswith('^'):
            lines = line.split(' ')
            if len(lines) == 3:
                rewrites.append(lines[0])
            elif len(lines) == 4:
                scripts.append({
                    "url": lines[0],
                    "type": lines[2],
                    "script_url": lines[3]
                })
    ximalaya.write(head)
    ximalaya.write("  url-rewrite:\n")
    for rewrite in rewrites:
        ximalaya.write("    - {} - reject\n".format(rewrite))
    ximalaya.write("  script:\n")
    for script in scripts:
        script_url = script["script_url"]
        script_url_set.add(script_url)
        script_name = get_script_name(script_url)
        ximalaya.write("    - match: {}\n".format(script["url"]))
        ximalaya.write("      name: {}\n".format(script_name))
        ximalaya.write("      type: response\n")
        ximalaya.write("      require-body: true\n")
        ximalaya.write("      timeout: 30\n")
    for script_url in script_url_set:
        script_name = get_script_name(script_url)
        ximalaya.write("script-providers:\n")
        ximalaya.write("  {}:\n".format(script_name))
        ximalaya.write("    url: {}\n".format(script_url))
        ximalaya.write("    interval: 86400\n")
    ximalaya.close()
    print('The stash override has been convert successfully!')
