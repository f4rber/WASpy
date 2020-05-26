import time
import colorama
from tools.logo import main_logo
from tools.WAFchecker import waf_checker
from tools.Dorker import dork_start
from fuzzing.main_inj import inj
from tools.QuoteChecker import checker
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    main_logo()
    print(colorama.Fore.RESET + '''\n
 [1] Find sites using dorks

 [2] SQL fuzzer

 [3] Directory scan

 [4] WAF checker
 
 [5] Find vulnerable site

 [99] Exit
''')

    menu_option = int(input(colorama.Fore.RESET + '[OPTION] ==> '))
    if menu_option == 1:
        dork_start()
        decision1 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
        if decision1 == "y":
            main()
        else:
            decision2 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
            if decision2 == "y":
                exit()
            else:
                main()

    elif menu_option == 2:
        inj()
        decision3 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
        if decision3 == "y":
            main()
        else:
            decision4 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
            if decision4 == "y":
                exit()
            else:
                main()

    elif menu_option == 3:
        from tools.Dirscan import dirscan
        dirscan()
        decision5 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
        if decision5 == "y":
            main()
        else:
            decision6 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
            if decision6 == "y":
                exit()
            else:
                main()

    elif menu_option == 4:
        waf_checker()
        decision7 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
        if decision7 == "y":
            main()
        else:
            decision8 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
            if decision8 == "y":
                exit()
            else:
                main()

    elif menu_option == 5:
        decision9 = input(colorama.Fore.RESET + "Scan sites using dorks? (y/n)\n[OPTION] ==> ")
        if decision9 == "y":
            dork_start()
            checker()
            decision10 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
            if decision10 == "y":
                main()
            else:
                decision10 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
                if decision10 == "y":
                    exit()
                else:
                    main()
        else:
            checker()
            decision11 = input(colorama.Fore.RESET + "\nOpen main menu? (y/n)\n[OPTION] ==> ")
            if decision11 == "y":
                main()
            else:
                decision12 = input(colorama.Fore.RESET + "Are you sure you want to quit? (y/n)\n[OPTION] ==> ")
                if decision12 == "y":
                    exit()
                else:
                    main()
    elif menu_option == 99:
        exit()
    else:
        print(colorama.Fore.RESET + "WRONG COMMAND!")
        time.sleep(1)
        main()


if __name__ == '__main__':
    main()
    print(colorama.Fore.RESET + '\n[$] Created by F4RB3R with Love.')
