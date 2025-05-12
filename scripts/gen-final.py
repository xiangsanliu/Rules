import os
import time
import re


def get_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content


values = {
    'build_time': time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    'general': get_from_file(os.getcwd() + '/temp/general.txt'),
    'proxy': get_from_file(os.getcwd() + '/temp/proxy.txt'),
    'direct': get_from_file(os.getcwd() + '/temp/direct.txt'),
    'netease': get_from_file(os.getcwd() + '/temp/netease.txt'),
    'ad': get_from_file(os.getcwd() + '/temp/ad.txt'),
    'telegram': get_from_file(os.getcwd() + '/temp/telegram.txt'),
    'custom': get_from_file(os.getcwd() + '/temp/custom.txt'),
    'adlite': get_from_file(os.getcwd() + '/temp/adlite.txt'),
}

def gen_file(name):
    template_file = open('template/' + name, mode='r', encoding='utf-8')
    template = template_file.read()
    output_file = open(os.getcwd() + '/gen/' + name, mode='w', encoding='utf-8')
    marks = re.findall(r'{{(.+)}}', template)
    for mark in marks:
        template = template.replace('{{' + mark + '}}', values[mark])
    output_file.write(template)
    template_file.close()
    output_file.close()

if __name__ == '__main__':
    file_names = os.listdir("template")
    for name in file_names:
        gen_file(name)