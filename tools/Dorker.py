import requests
from bs4 import BeautifulSoup
from .logo import dorker_logo


def dork_start():
    dorker_logo()
    dork = input("Enter dork: ")
    pages = 1
    how_much = input("Enter number of pages to scan: ")
    decision = input("CLean old file? (y/n)\n[OPTION] ==> ")
    if decision == "y":
        file = open("dorks.txt", "w", encoding="utf=8")
        file.write("https://cybersec.org\n")
        file.close()
    else:
        print("Skipping...")
    while pages != int(how_much):
        print("[+] Here's The Results")
        send = requests.get("http://www1.search-results.com/web?q=" + dork + "&page=" + str(pages))
        parsing = BeautifulSoup(send.text, features="html.parser")
        for data in parsing.find_all("cite"):
            print(data.string)
            f = open("dorks.txt", "a", encoding="utf=8")
            f.write(data.string + "\n")
        pages = pages + 1
        if pages == int(how_much):
            print("\nResults was sawed to dorks.txt\n")
