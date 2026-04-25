import os
import time
import random
import sys

# Mac Terminal Renk Paleti
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def screen_clear():
    # Hata mesajlarını gizleyerek ekranı temizle
    os.system('clear 2>/dev/null')

def mac_alert(title, message):
    # Mac uyarı penceresi - Hataları dışarı sızdırmaz
    cmd = f"osascript -e 'display dialog \"{message}\" with title \"{title}\" buttons {{\"TAMAM\"}} default button \"TAMAM\" with icon caution' 2>/dev/null"
    os.system(cmd)

def mac_sound():
    # En garanti Mac sesi (Bip) - Hata vermez
    os.system("osascript -e 'beep' 2>/dev/null")

def main_header():
    screen_clear()
    print(f"{RED}{BOLD}===================================================={RESET}")
    print(f"{RED}{BOLD}          ZYnaX v45: macOS ULTIMATE EDITION         {RESET}")
    print(f"{RED}{BOLD}===================================================={RESET}")
    print(f"{CYAN}Sistem:{RESET} macOS Kernel | {CYAN}Durum:{RESET} {GREEN}Bypass Active{RESET}")
    print(f"----------------------------------------------------")

def main():
    # Başlangıç efektleri
    mac_sound()
    mac_alert("ZYnaX CORE", "Sistem Erişimi Onaylandı! Yusuf Dadaş Paneli Yükleniyor.")
    
    main_header()
    
    print(f"{YELLOW}[+] Modüller taranıyor...{RESET}")
    time.sleep(1)
    
    # ZYnaX'ın kalbi: IP İzleme ve Uyarı Sistemi
    print(f"\n{PURPLE}--- ZYnaX KONTROL MERKEZİ ---{RESET}")
    print("1) IP İzleme Modülünü Başlat (Classic)")
    print("2) Sahte Sistem Hatası Gönder")
    print("3) Mac Sesini Fulleyip 'Bip' Çal")
    print("4) Sistemi Uykuya Gönder")
    print("5) Çıkış")

    try:
        secim = input(f"\n{YELLOW}Komut Girin > {RESET}")

        if secim == "1":
            print(f"\n{RED}[!] CANLI TRAFİK ANALİZİ BAŞLADI...{RESET}\n")
            while True:
                ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                print(f"{BLUE}[ZYnaX-IP]{RESET} Bağlantı Kesildi: {GREEN}{ip}{RESET} | Durum: {RED}REJECTED{RESET}")
                time.sleep(0.1)
        
        elif secim == "2":
            mac_sound()
            mac_alert("SYSTEM ERROR", "Kritik Hata: ZYnaX v45 dosyalarınızı şifreledi! ")
            main()

        elif secim == "3":
            print(f"{RED}Ses ve Bip testi yapılıyor...{RESET}")
            os.system("osascript -e 'set volume output volume 100' 2>/dev/null")
            os.system("osascript -e 'beep 2' 2>/dev/null")
            main()

        elif secim == "4":
            print(f"{YELLOW}Sistem uykuya geçiyor...{RESET}")
            time.sleep(2)
            os.system("osascript -e 'tell app \"System Events\" to sleep' 2>/dev/null")

        elif secim == "5":
            print(f"{GREEN}ZYnaX kapatıldı. Güle güle dadaş!{RESET}")
            sys.exit()
        
        else:
            main()

    except KeyboardInterrupt:
        main()

if __name__ == "__main__":
    main()
