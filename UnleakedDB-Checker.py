import time 
import os 
import requests 
from colorama import Fore


banner = '''

██╗    ██╗███████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
██║    ██║██╔════╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ████╗ ████║██╔═══██╗██╔══██╗╚══███╔╝╚══███╔╝
██║ █╗ ██║█████╗  █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗██╔████╔██║██║   ██║██║  ██║  ███╔╝   ███╔╝ 
██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██║   ██║██║  ██║ ███╔╝   ███╔╝  
╚███╔███╔╝███████╗███████╗██║     ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
                   Hacked Account database | Open-Source Project by WeepingAngel
                       GitHub: https://www.github.com/Crafttino21                                                                                


'''

choice = '''
[1] Load all Registerd Datas

[2] Check if your Account got Leaked

[3] Support the Creator

'''



print(Fore.LIGHTMAGENTA_EX + banner)

print(choice)

x = input("root~$ ")

if x == '1':
    keysite = requests.get("https://raw.githubusercontent.com/Crafttino21/Unleaked-DB/main/Database%20v1/Unleaked-by-WeepingAngel.txt")
    print(Fore.CYAN + keysite.text)
    
    
if x == '2':
    db1 = requests.get("https://raw.githubusercontent.com/Crafttino21/Unleaked-DB/main/Database%20v1/Unleaked-by-WeepingAngel.txt")
    print("Enter your data here (Email:Password)")
    acc = input(" > ")
    if acc in db1.text:
        print(Fore.RED + "Your Account got Leaked and is Registerd on our Database! Please change your Data!")
    else:
        print(Fore.LIGHTGREEN_EX + "Youre Safe, Your Account isnt Registed on Our Databse :)")
    



