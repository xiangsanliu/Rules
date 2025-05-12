from asyncore import write
from typing import Set
import requests


def get_list(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text.split('\n')


def convert(lines):
    classical = set()
    domain = set()
    for line in lines:
        if line.startswith('#') or len(line) == 0:
            continue
        if line.startswith('DOMAIN-SUFFIX'):
            domain.add(line.split(',')[1])
        else:
            classical.add(line)
    return domain, classical


def write_to_file(filename, lines, format_str):
    ad_file = open(filename, mode='w', encoding='utf-8')
    ad_file.write("payload:\n")
    for line in lines:
        ad_file.write(format_str.format(line))

    ad_file.close()
    print('The {} has been built successfully! Rule size: {}.'.format(
        filename, len(lines)))


urls = {
    "adlite":
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
    "microsoft":
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.list"
}


def main():
    for key in urls.keys():
        rules = get_list(urls.get(key))
        domain, classical = convert(rules)
        write_to_file("./clash/{}-domain.yaml".format(key), domain, "  - '+.{}'\n")
        write_to_file("./clash/{}-classical.yaml".format(key), classical, "  - {}\n")
        


if __name__ == '__main__':
    main()
