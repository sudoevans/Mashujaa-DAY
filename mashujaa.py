#Stupid Codes Season 1 ep 5 huh. ;)
#Mashujaa Day in Style!
# Code By  Gamer_Snave
import sys, os, time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
os.system("cls")
Greetings='''
█░█ █▀▀ █░░ █░░ █▀█ ░     █░█ █     █ ▀█▀ ▀ █▀ ▀
█▀█ ██▄ █▄▄ █▄▄ █▄█ █     █▀█ █     █ ░█░ ░ ▄█ ▄ \n\


█▀▄▀█ ▄▀█ █▀ █░█ █░█ ░░█ ▄▀█ ▄▀█   █▀▄ ▄▀█ █▄█
█░▀░█ █▀█ ▄█ █▀█ █▄█ █▄█ █▀█ █▀█   █▄▀ █▀█ ░█░'''

happy=''' 
╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━┳━━━┳━━━┳╮╱╭┳╮╱╭╮╱╭┳━━━┳━━━╮╱╭━━━┳━━━┳╮╱╱╭╮╭━━━━╮╱╱╭╮╱╱╭╮
┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃╭━╮┃╭━╮┃┃╱┃┃┃╱┃┃╱┃┃╭━╮┃╭━╮┃╱╰╮╭╮┃╭━╮┃╰╮╭╯┃┃╭╮╭╮┃╱╱┃╰╮╭╯┃
┃╰━╯┣━━┳━━┳━━┳╮╱╭╮┃╭╮╭╮┃┃╱┃┃╰━━┫╰━╯┃┃╱┃┃╱┃┃┃╱┃┃┃╱┃┃╱╱┃┃┃┃┃╱┃┣╮╰╯╭╯╰╯┃┃┣┻━╮╰╮╰╯╭┻━┳╮╭╮
┃╭━╮┃╭╮┃╭╮┃╭╮┃┃╱┃┃┃┃┃┃┃┃╰━╯┣━━╮┃╭━╮┃┃╱┃┣╮┃┃╰━╯┃╰━╯┣━━┫┃┃┃╰━╯┃╰╮╭╯╱╱╱┃┃┃╭╮┃╱╰╮╭┫╭╮┃┃┃┃
┃┃╱┃┃╭╮┃╰╯┃╰╯┃╰━╯┃┃┃┃┃┃┃╭━╮┃╰━╯┃┃╱┃┃╰━╯┃╰╯┃╭━╮┃╭━╮┣━┳╯╰╯┃╭━╮┃╱┃┃╱╱╱╱┃┃┃╰╯┃╱╱┃┃┃╰╯┃╰╯┃
╰╯╱╰┻╯╰┫╭━┫╭━┻━╮╭╯╰╯╰╯╰┻╯╱╰┻━━━┻╯╱╰┻━━━┻━━┻╯╱╰┻╯╱╰╯╱╰━━━┻╯╱╰╯╱╰╯╱╱╱╱╰╯╰━━╯╱╱╰╯╰━━┻━━╯
╱╱╱╱╱╱╱┃┃╱┃┃╱╭━╯┃
╱╱╱╱╱╱╱╰╯╱╰╯╱╰━━╯'''


sal=''' 
█▄█ █▀█ █░█   ▄▀█ █▀█ █▀▀   ▄▀█   █░█ █▀▀ █▀█ █▀█ █
░█░ █▄█ █▄█   █▀█ █▀▄ ██▄   █▀█   █▀█ ██▄ █▀▄ █▄█ ▄  \n\ '''

bye=''' 
█▀▀ █▀█ █▀█ █▀▄▀█ ▀
█▀░ █▀▄ █▄█ █░▀░█ ▄  \n\

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃┃╱╰╋━━┳╮╭┳━━┳━╮┃╰━━┳━╮╭━━┳╮╭┳━━╮
┃┃╭━┫╭╮┃╰╯┃┃━┫╭╯╰━━╮┃╭╮┫╭╮┃╰╯┃┃━┫
┃╰┻━┃╭╮┃┃┃┃┃━┫┃╱┃╰━╯┃┃┃┃╭╮┣╮╭┫┃━┫
╰━━━┻╯╰┻┻┻┻━━┻╯╱╰━━━┻╯╰┻╯╰╯╰╯╰━━╯ \n\


██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░
██║░░░░░██║░░██║██║░░░░░
██║░░░░░██║░░██║██║░░░░░
███████╗╚█████╔╝███████╗
╚══════╝░╚════╝░╚══════╝
!'''



def display_green(message):
    for char in Greetings:
        sys.stdout.write(Fore.GREEN+Back.BLACK+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.005)
        else:
            time.sleep(1)
def display_red(message):
    for char in happy:
        sys.stdout.write(Fore.RED+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.005)
        else:
            time.sleep(0.01)
def display_yellow(message):
    for char in sal:
        sys.stdout.write(Fore.YELLOW+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.01)
        else:
            time.sleep(0.5)
def display_clear(message):
    for char in bye:
        sys.stdout.write(Fore.GREEN+char)
        sys.stdout.flush()
        if char !="\n":
            time.sleep(0.005)
        else:
            time.sleep(0.1)



display_green(Greetings)
display_red(happy)
display_yellow(sal)
os.system("cls")
display_clear(bye)
os.system("cls")
os.system('exit')









    


