The Keysight U1232A handheld digital multi-meter has a optical to Bluetooth module U1177A alowing remote management with SCPI commands:

1. Connect to the module:
```
sudo bluetoothctl
# scan on
# pair 00:12:6F:2D:20:CE
# quit
sudo nohup rfcomm connect /dev/rfcomm0 00:12:6F:2D:20:CE 1 &
#speed 9600
```
2. Run the script:
```
sudo python3 test.py
connected...STAT?
"000000000110L00200000"
"000000000110L00200000"
CONF?
"V,0,DC"
"V,0,DC"
FETC?
+1.96700000E-02
2023-57-02T10:57:39Z
SYST:BATT?
60%
60%
SYST:BEEP
FETC?
+1.96800000E-02
2023-57-02T10:57:40Z
SYST:BATT?
61%
61%
SYST:BEEP
```
