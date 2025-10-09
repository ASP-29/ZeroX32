#ZeroX32 Project
A projects that were created as multi-tool projects such as flipper zero and well-known open source projects such as bruce firmware
Powered by ESP3-S3 for main microcontroller


##WiFi
  - Scanning ap,station,and finding hidden ssid name
  - Deauth attack on selected target
  - Wifi beacon attack with name custom ssid list and random name
  - Evil portal with html page up to 5 different page for each device and domains name can be customized
  - Packet Monitor for detecting deauth attack from other attacker in nearby


##Bluetooth
  - Ble spam Ios,swift pair,samsung and google fast pair
  - Remote controller that can act like Media controll and mouse


##Infrared
  - Read for custom ir remote
  - Load the ir remote data from files,also compatible with flipper zero ir database
  - Sending each ir data sequenced with interval for performing bruteforce
  - Universal remote like flipper zero,see the sdcard files under infrared/UNIVERSAL REMOTE/..
  Supported IR protocol
    | Protocol               | Send | Receive | Description                        |
    |------------------------|------|---------|------------------------------------|
    | NEC                    | ✅   | ✅       | Common in many TV remotes          |
    | SONY                   | ✅   | ✅       | Sony TVs, audio systems            |
    | SAMSUNG                | ✅   | ✅       | Samsung TVs and AC units           |
    | LG                     | ✅   | ✅       | LG TVs and air conditioners        |
    | JVC                    | ✅   | ✅       |                                    |
    | PANASONIC              | ✅   | ✅       | Includes Panasonic AC              |
    | MITSUBISHI_AC          | ✅   | ✅       | Mitsubishi air conditioners        |
    | DAIKIN                 | ✅   | ✅       | Daikin AC (multiple variants)      |
    | FUJITSU_AC             | ✅   | ✅       | Fujitsu air conditioners           |
    | TOSHIBA_AC             | ✅   | ✅       | Toshiba air conditioners           |
    | HITACHI_AC             | ✅   | ✅       | Hitachi air conditioners           |
    | GREE                   | ✅   | ✅       | Gree air conditioners              |
    | WHIRLPOOL_AC           | ✅   | ✅       | Whirlpool air conditioners         |
    | COOLIX                 | ✅   | ✅       | Used in TCL, Nikai, and similar    |
    | MIDEA                  | ✅   | ✅       | Midea air conditioners             |
    | RC5 / RC6              | ✅   | ✅       | Used in Philips and others         |
    | SHARP                  | ✅   | ✅       | Sharp TVs                          |
    | SANYO_AC               | ✅   | ✅       | Sanyo air conditioners             |
    | CARRIER_AC             | ✅   | ✅       | Carrier air conditioners           |
    | AUX                    | ✅   | ✅       | AUX brand ACs                      |
    | VOLTAS                 | ✅   | ✅       | Voltas air conditioners            |
    | YORK                   | ✅   | ✅       | York ACs                           |
    | TECO                   | ✅   | ✅       | Teco ACs                           |
    | ZEPEAL                 | ✅   | ✅       |                                    |
    | BOSE                   | ✅   | ✅       |                                    |
    | PIONEER                | ✅   | ✅       |                                    |
    | RCMM                   | ✅   | ✅       | Used in some advanced remotes      |
    | RAW / PRONTO           | ✅   | ❌       | Manual/custom IR signal sending    |
    | GLOBALCACHE            | ✅   | ❌       | Sends in GlobalCache format        |
    | SHERWOOD               | ✅   | ❌       | Send-only protocol                 |
    | LEGOPF                 | ✅   | ✅       | LEGO Power Functions (IR motors)   |

    For legacy list
    | Index | Protocol              | Index | Protocol               |
    |-------|-----------------------|-------|------------------------|
    | 1     | RC5                   | 65    | DAIKIN160              |
    | 2     | RC6                   | 66    | NEOCLIMA               |
    | 3     | NEC                   | 67    | DAIKIN176              |
    | 4     | SONY                  | 68    | DAIKIN128              |
    | 5     | PANASONIC             | 69    | AMCOR                  |
    | 6     | JVC                   | 70    | DAIKIN152              |
    | 7     | SAMSUNG               | 71    | MITSUBISHI136          |
    | 8     | WHYNTER               | 72    | MITSUBISHI112          |
    | 9     | AIWA_RC_T501          | 73    | HITACHI_AC424          |
    | 10    | LG                    | 74    | SONY_38K               |
    | 11    | SANYO                 | 75    | EPSON                  |
    | 12    | MITSUBISHI            | 76    | SYMPHONY               |
    | 13    | DISH                  | 77    | HITACHI_AC3            |
    | 14    | SHARP                 | 78    | DAIKIN64               |
    | 15    | COOLIX                | 79    | AIRWELL                |
    | 16    | DAIKIN                | 80    | DELONGHI_AC            |
    | 17    | DENON                 | 81    | DOSHISHA               |
    | 18    | KELVINATOR            | 82    | MULTIBRACKETS          |
    | 19    | SHERWOOD              | 83    | CARRIER_AC40           |
    | 20    | MITSUBISHI_AC         | 84    | CARRIER_AC64           |
    | 21    | RCMM                  | 85    | HITACHI_AC344          |
    | 22    | SANYO_LC7461          | 86    | CORONA_AC              |
    | 23    | RC5X                  | 87    | MIDEA24                |
    | 24    | GREE                  | 88    | ZEPEAL                 |
    | 25    | PRONTO                | 89    | SANYO_AC               |
    | 26    | NEC_LIKE              | 90    | VOLTAS                 |
    | 27    | ARGO                  | 91    | METZ                   |
    | 28    | TROTEC                | 92    | TRANSCOLD              |
    | 29    | NIKAI                 | 93    | TECHNIBEL_AC           |
    | 30    | RAW                   | 94    | MIRAGE                 |
    | 31    | GLOBALCACHE           | 95    | ELITESCREENS           |
    | 32    | TOSHIBA_AC            | 96    | PANASONIC_AC32         |
    | 33    | FUJITSU_AC            | 97    | MILESTAG2              |
    | 34    | MIDEA                 | 98    | ECOCLIM                |
    | 35    | MAGIQUEST             | 99    | XMP                    |
    | 36    | LASERTAG              | 100   | TRUMA                  |
    | 37    | CARRIER_AC            | 101   | HAIER_AC176            |
    | 38    | HAIER_AC              | 102   | TEKNOPOINT             |
    | 39    | MITSUBISHI2           | 103   | KELON                  |
    | 40    | HITACHI_AC            | 104   | TROTEC_3550            |
    | 41    | HITACHI_AC1           | 105   | SANYO_AC88             |
    | 42    | HITACHI_AC2           | 106   | BOSE                   |
    | 43    | GICABLE               | 107   | ARRIS                  |
    | 44    | HAIER_AC_YRW02        | 108   | RHOSS                  |
    | 45    | WHIRLPOOL_AC          | 109   | AIRTON                 |
    | 46    | SAMSUNG_AC            | 110   | COOLIX48               |
    | 47    | LUTRON                | 111   | HITACHI_AC264          |
    | 48    | ELECTRA_AC            | 112   | KELON168               |
    | 49    | PANASONIC_AC          | 113   | HITACHI_AC296          |
    | 50    | PIONEER               | 114   | DAIKIN200              |
    | 51    | LG2                   | 115   | HAIER_AC160            |
    | 52    | MWM                   | 116   | CARRIER_AC128          |
    | 53    | DAIKIN2               | 117   | TOTO                   |
    | 54    | VESTEL_AC             | 118   | CLIMABUTLER            |
    | 55    | TECO                  | 119   | TCL96AC                |
    | 56    | SAMSUNG36             | 120   | BOSCH144               |
    | 57    | TCL112AC              | 121   | SANYO_AC152            |
    | 58    | LEGOPF                | 122   | DAIKIN312              |
    | 59    | MITSUBISHI_HEAVY_88   | 123   | GORENJE                |
    | 60    | MITSUBISHI_HEAVY_152  | 124   | WOWWEE                 |
    | 61    | DAIKIN216             | 125   | CARRIER_AC84           |
    | 62    | SHARP_AC              | 126   | YORK                   |
    | 63    | GOODWEATHER           | 127   | BLUESTARHEAVY          |
    | 64    | INAX                  |       |                        |

    You can load ir file from Flipper Zero
    Related repo https://github.com/logickworkshop/Flipper-IRDB
    Thanks for amazing library created by @crankyoldgit https://github.com/crankyoldgit/IRremoteESP8266

##Sub-Ghz
  - Supported protocol
    | Device / Protocol Type              | Supported | Notes                                                  |
    |------------------------------------|-----------|--------------------------------------------------------|
    | Intertechno (old models)           | ✅         | Fixed code only, rolling code not supported           |
    | Nexa (older versions)              | ✅         | Basic RF switches, works with RCSwitch                |
    | Elro RF switches                   | ✅         | Common 433MHz devices                                 |
    | Brennenstuhl remote plugs          | ✅         | Some models supported                                 |
    | Chacon                             | ✅         | Similar to Intertechno                                |
    | KlikAanKlikUit (KAKU)              | ✅         | Limited to old models without rolling code            |
    | HomeEasy (UK, old models)          | ✅         | Older versions supported                              |
    | Generic 433 MHz Chinese remotes    | ✅         | Widely used in low-cost RF transmitters/receivers    |
    | EV1527 RF modules                  | ✅         | Very common encoder chip (fixed code)                |
    | PT2262 / SC2262 / HX2262           | ✅         | Basic encoding chip used in many RF devices           |
    | LC Technology RF Modules           | ✅         | Cheap TX/RX modules compatible with Arduino           |
 - Read and decoded supported protocol and save it
 - Read raw for uknown protocol and save it
 - already some preset with modulation AM270,AM650,FM238,FM476,FM95,FM15k,Pagers,HND_1,HND_2 thanks for derek jamieson explanation wiki https://github.com/jamisonderek/flipper-zero-tutorials/wiki/Sub-GHz
 - Supported Flipper Zero .sub file (only raw format) can be transmitted/replayed
 - Jammer feature with continues wave
 - Frequency analyzer for detecting your keyfob frequency if you don't know it
 - related repo
   https://github.com/tobiabocchi/flipperzero-bruteforce
   https://github.com/UberGuidoZ/Flipper


##Bad USB
 - Running your selected ducky script payload,inspired by spacehuhn's wifi duck project https://github.com/SpacehuhnTech/WiFiDuck and forked repo by wasdwasd0105 https://github.com/wasdwasd0105/SuperWiFiDuck
 - Supported with autorun option when usb is plug in on target
 - Supported with flipper zero payload
 - related repo
   https://github.com/bst04/payloads_flipperZero
   https://github.com/MarkCyber/BadUSB


##File Manager
 - Builtin interactive file explorer can performing load saved files,firmware update,rename,delete and managing html files for evil portal
 - Supported web server for file upload


##NRF24L01
 - Can performing a signal jamming like bluetooth,wifi and related connectivity around 2.4Ghz
 - Signal Analyzer / Spectrum Analyzer for monitoring 2.4ghz signal traffic
 - Inspired by cifertech's project https://github.com/cifertech/nRFBox


##Headless Controll
 - can be controlled headless but with limited features with a web server
 - Screen mirroring feature like flipper zero,see this video https://www.youtube.com/shorts/sRir4fzV7GA

I will update other features and documentation over time
for fastest information update you can subscribe my youtube channel https://www.youtube.com/@asp-29blackhat18 and https://www.youtube.com/@ASP29Tech
join my group if you want asking some information directly https://t.me/X32Project

    

