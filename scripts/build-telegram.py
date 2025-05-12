import requests
import os


def get_telegram():
    res = requests.get('https://cdn.jsdelivr.net/gh/Loyalsoldier/surge-rules@release/ruleset/telegramcidr.txt')
    if res.status_code != 200:
        raise Exception('Connect error')
    return res.text


if __name__ == '__main__':
    telegram = get_telegram()
    telegram = telegram.split('\n')
    telegram_file = open(os.getcwd() + '/temp/telegram.txt', mode='w', encoding='utf-8')
    telegram_snippet = open(os.getcwd() + '/snippet/telegram.txt', mode='w', encoding='utf-8')
    for line in telegram:
        if len(line) > 0:
            telegram_file.write('%s,PROXY,no-resolve\n' % line.replace('IP-CIDR6', 'IP-CIDR'))
            telegram_snippet.write('%s\n' % line.replace('IP-CIDR6', 'IP-CIDR'))
    telegram_file.close()
    telegram_snippet.close()
    print('The telegram rule has been built successfully! Rule size: {}.'.format(len(telegram)))