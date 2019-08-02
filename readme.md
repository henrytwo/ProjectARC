Raspberry Pi powered Ceiling Fan art<br><br>
Visit https://henrytu.me/#projects for more details
<br><br>
Step 0: Setup Hardware<br>
Securely attach an LED strip, Raspberry Pi, and Battery bank to a ceiling fan. Remember that uniform circular motion exists and that flying objects hurt if they hit you.<br><br>
Adafruit NEO Compatible LED strips were used in development.
<br><br>
Step 1: Parse image<br>
Before an image can be displayed, it needs to be converted to a format that can be interpreted. Run `python3 convert.py` and follow the on screen instructions.<br><br>
Tip: `Num Pixels` refers to the number of LEDs on the rotating arm.
<br><br>
Step 3: Deployment<br>
Move `main.py` and `pattern.pkl` to the Raspberry Pi.
<br><br>
Run `sudo python3 main.py`
<br><br>
`main.py` MUST be run under root!
