import base64
import requests
import urllib
import os

PROXY_DNS = 'https://1.0.0.1/dns-query'

def get_list():
    res = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Proxy/Proxy.list")
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text

def write_cn_dns(file):
    file.write("https://doh.pub/dns-query\n")
    file.write("https://doh.360.cn/dns-query\n")

def write_out_dns(file):
    list = str(get_list())
    list = list.split("\n")
    for line in list:
        if line.startswith('#') or line.startswith('IP-CIDR') or line.startswith('DOMAIN-KEYWORD'):
            continue
        elif line.startswith('DOMAIN-SUFFIX'):
            line = line.replace('DOMAIN-SUFFIX,', '')
            
        elif line.startswith('DOMAIN'):
            line = line.replace('DOMAIN,', '')
        if len(line) > 1:
            write_line(adguard_file, line)


def write_line(file, line):
    formatted_line = '[/%s/]%s\n' % (line, PROXY_DNS)
    file.write(formatted_line)

if __name__ == '__main__':
    adguard_file = open('adguard.txt', mode='w', encoding='utf-8')
    write_out_dns(adguard_file)
    write_cn_dns(adguard_file)
    adguard_file.write('\n')
    adguard_file.close()

