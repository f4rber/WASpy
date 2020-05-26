import requests
import time
from colorama import Fore
from fake_useragent import UserAgent
import urllib3
from .logo import quote_check_logo


def checker():
    quote_check_logo()
    http = urllib3.PoolManager()
    file = input(Fore.RESET + "Enter file with url`s: ")
    decision = input(Fore.RESET + "Delete old file? (y/n)\n[OPTION] ==> ")
    if decision == "y":
        urls = open(r"injectableURL.txt", mode="w")
        urls.write("https://cybersec.org\n")
        urls.close()
    else:
        print(Fore.RESET + "[+] Skipping...")
    url = open(str(file), "r")
    error = "You have an error in your SQL syntax"
    while url.readline():
        try:
            ua = UserAgent(cache=False)

            headers = requests.utils.default_headers()
            headers.update(
                {
                    'User-Agent': ua.random
                })

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            connect_to = url.readline()
            time.sleep(0.10)
            print(Fore.RESET + "\n[+]########[+]")
            print(Fore.RESET + "[+] Result:")
            print(connect_to)
            send = http.request("GET", str(connect_to) + "'", headers=headers)
            if bytes(error, encoding="utf-8") in send.data:
                print(Fore.GREEN + "Vulnerable!")
                injectable_url = open("injectableURL.txt", 'a')
                injectable_url.write(str(connect_to))
                injectable_url.close()
                print(Fore.RESET + "[+]########[+]\n")
            else:
                print(Fore.RED + "Not vulnerable!")
                print(Fore.RESET + "[+]########[+]\n")
        except Exception as ex:
            print(Fore.RED + "[+] Exception: " + str(ex))
