from datetime import datetime
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import requests
import sys
import urllib3
import os
from colorama import Fore
from .logo import dirscan_logo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()


user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Cl:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    white = '\033[1m'
    under = '\033[4m'
    target = input(Fore.RESET + "Enter target URL: ")
    thread = int(input(Fore.RESET + "Enter number of threads: "))
    wordlist = input(Fore.RESET + "Use default wordlist? (y/n): ")
    if wordlist == "y":
        wordlist = open("tools/wordlists/dirbuster-medium.txt", 'r')
    else:
        try:
            path_to_wordlist = input(Fore.RESET + "Enter path to wordlist: ")
            wordlist = open(str(path_to_wordlist), 'r')
        except Exception as ex:
            print("Error: " + str(ex))
            wordlist = open("tools/wordlists/dirbuster-medium.txt", 'r')
    random_agent = input(Fore.RESET + "Enable random agent? (y/n): ")


def sizeof(num, suffix='B'):
    for unit in [' ', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return '{:>4} {}{}'.format(format(num, '.3g'), unit, suffix)
        num /= 1024.0


def statuses(line):
    url = str(Cl.target) + str(line)
    if Cl.random_agent == "y":
        user__agent = {'User-agent': UserAgent().random}
        r = requests.get(url, headers=user__agent, timeout=5, allow_redirects=False, verify=False)
    else:
        user__agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        r = requests.get(url, headers=user__agent, timeout=5, allow_redirects=False, verify=False)

    num = int(len(r.text))
    status = r.status_code
    # Success
    if status == 200:
        if line == '':
            pass
        elif len(r.text) == length:
            pass
        else:
            sys.stdout.write(
                Cl.green + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),
                                                          url) + Cl.end)
    # Redirect
    elif status == 301:
        if len(r.text) == length:
            pass
        else:
            sys.stdout.write(
                Cl.red + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),
                                                        url) + Cl.end)
    # Internal server error
    elif status == 500:
        if len(r.text) == length:
            pass
        else:
            sys.stdout.write(
                Cl.pink + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),
                                                         url) + Cl.end)
    # Unauthenticated
    elif status == 401:
        if len(r.text) == length:
            pass
        else:
            sys.stdout.write(
                Cl.yellow + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),
                                                           url) + Cl.end)
    # Forbidden
    elif status == 403:
        if ".ht" in line:
            pass
        elif len(r.text) == length:
            pass
        else:
            sys.stdout.write(
                Cl.blue + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),
                                                         url) + Cl.end)


def prog():
    sys.stdout.flush()
    sys.stdout.write('| {} | [+] Wait a moment ...\r'.format(datetime.now().strftime('%H:%M:%S')))
    sys.stdout.flush()
    sys.stdout.write('| {} | [x] Wait a moment ...\r'.format(datetime.now().strftime('%H:%M:%S')))


try:
    cek = requests.get(str(Cl.target), headers=user_agent, timeout=5, verify=False)
    length = len(cek.text)
except Exception as ex:
    print('ERROR: Invalid address or target is down..' + str(ex))
    sys.exit()

no = 0
file = Cl.wordlist.read().split('\n')
l_count = sum(1 for line in file)
no = no + 1


def dirscan():
    dirscan_logo()
    print('Start scanning directory..')
    print('Wordlist : {} | Thread : {} | Random agent : {}'.format(Cl.wordlist, Cl.thread, Cl.random_agent))
    print('===============================================================================')
    print('| Time     | Info          | URL                                              |')
    print('===============================================================================')
    executor = ThreadPoolExecutor(max_workers=Cl.thread)
    futures = []
    for line in file:
        try:
            a = executor.submit(statuses, line)
            futures.append(a)
            jumlah = (no * 100) / l_count
            sys.stdout.flush()
            sys.stdout.write("| {} | {}% Line : {}\r".format(datetime.now().strftime('%H:%M:%S'), int(jumlah), int(no)))
            sys.stdout.flush()
        except(KeyboardInterrupt, SystemExit):
            print('\r| {} | Exiting program ...'.format(datetime.now().strftime('%H:%M:%S')))
            print('===============================================================================')
            os.kill(os.getpid(), 9)

    while True:
        try:
            prog()
            cek = a.done()
            if cek is True:
                sleep(1)
                print('===============================================================================')
                exit()

        except KeyboardInterrupt:
            print('\r| {} | Exiting program ...'.format(datetime.now().strftime('%H:%M:%S')))
            print('===============================================================================')
            os.kill(os.getpid(), 9)
