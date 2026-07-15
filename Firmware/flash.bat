@echo off
setlocal EnableDelayedExpansion
title ZeroX32 Flasher

echo Available COM Ports:
echo.

set i=0

for /f "tokens=3" %%a in ('reg query "HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM"') do (
    set /a i+=1
    set port!i!=%%a
    echo !i!. %%a
)

if %i%==0 (
    echo.
    echo No COM ports found.
    pause
    exit /b
)

echo.
set /p port_choice=Choose COM port number: 

if not defined port%port_choice% (
    echo Invalid selection.
    pause
    exit /b
)

set com_port=!port%port_choice%!

echo.
echo Selected Port : %com_port%
echo.

echo Select the hardware:
echo 1. ESP32S3
echo 2. BW16
set /p choice=Choose (1 or 2): 

if "%choice%"=="1" (
    echo Writing to ESP32-S3 on port %com_port%...
    esptool.exe --chip esp32s3 --port %com_port% --baud 921600 erase_flash
    esptool.exe --chip esp32s3 --port %com_port% --baud 921600 write_flash ^
        0x0 bootloader.bin ^
        0x8000 partitions.bin ^
        0x10000 firmware.bin ^
        0x410000 littlefs.bin
) else if "%choice%"=="2" (
    echo Writing to BW16 on port %com_port%...
    amebatool.exe .\bin %com_port% --verbose=5
) else (
    echo Invalid selection.
)

pause