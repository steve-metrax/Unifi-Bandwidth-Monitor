# UniFi Bandwidth Monitor for LilyGo T-Display S3

A MicroPython-based dashboard for monitoring UniFi network bandwidth (upload/download) and connected clients on the LilyGo T-Display S3 (320x170 landscape).

## Features
- Displays upload and download speeds (0.1-950 Mbps, logarithmic scale) as bar graphs with white outlines.
- Shows the number of connected clients.
- Updates every ~5-10 seconds via the UniFi API.
- Runs autonomously on power-on.
- Automatically refreshes the UniFi session cookie to prevent expiration after ~2 hours.

## Screenshots
![Unifi Monitor Image](https://github.com/steve-metrax/Unifi-Monitor/blob/main/IMG_9638.JPG)

*Dashboard displaying upload/download speeds and client count on an Orange background.*

## Hardware
- **LilyGo T-Display S3**: ESP32-S3 with ST7789 display (320x170).
- **Power**: USB power adapter (5V, 1-2A) or LiPo battery (3.7V, 500mAh+).

## Software
- **MicroPython Firmware**: For ESP32-S3 (download from [MicroPython.org](https://micropython.org/download/esp32s3/) or [LilyGo GitHub](https://github.com/Xinyuan-LilyGO/LilyGo-T-Display-S3)).
- **Required Files**:
  - `main.py`: Main script for the dashboard.
  - `vga2_8x16.py`: Font file for text display.

## Installation
1. Flash the latest MicroPython firmware to your LilyGo T-Display S3 using Thonny or esptool.py.
2. Upload `main.py` and `vga2_8x16.py` to the root of the device’s filesystem using Thonny (File > Save As > MicroPython Device).
3. Update the following variables in `main.py` with your settings:
   - `WIFI_SSID`: Your WiFi network name.
   - `WIFI_PASSWORD`: Your WiFi password.
   - `CONTROLLER_URL`: Your UniFi controller URL (e.g., `https://192.168.1.1`).
   - `USERNAME`: Your UniFi controller username.
   - `PASSWORD`: Your UniFi controller password.
   - `SITE`: Your UniFi site name (default is `"default"`).
4. Power on the T-Display S3 via USB or battery—it will autostart and display the dashboard.

## Usage
- The display shows:
  - Red bar for upload speed (top).
  - Green bar for download speed (middle).
  - Client count at the bottom (e.g., “Clients: 5”).
- Status messages like “WiFi...”, “Login...”, or “No Data” appear if there are issues.
- Customize `MAX_SPEED` (default: 950 Mbps) or `utime.sleep()` (default: 0.5s) in `main.py` for your network or refresh rate.

## Troubleshooting
- **No WiFi Connection**: Verify `WIFI_SSID` and `WIFI_PASSWORD` in `main.py`. Ensure the T-Display is within range and uses 2.4 GHz (not 5 GHz).
- **Login Failure**: Check `CONTROLLER_URL`, `USERNAME`, and `PASSWORD`. Ensure the UniFi controller is accessible.
- **Stops After ~2 Hours**: This bug was fixed—script now re-authenticates when the UniFi session cookie expires.

## Changelog
- **Initial Release**: Added bar graph display for UniFi bandwidth and client stats.
- **Bug Fix**: Added automatic cookie refresh to handle UniFi session expiration (~2 hours).

## Credits
- Created by Steve Upson with help from Grok 3 (xAI), quite a lot of help actually as this is not in my wheelhouse! The networking bit is very much in my wheelhouse.
- Uses libraries from [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy), again thanks Russ!
- ZX Spectrum BASIC is about the limit of my knowledge when it comes to programming so getting this working did give me a buzz.

- ## Improvements
- Looks, I'm no graphic artist so plenty of scope for improvement
- Refresh, the display refresh is once every 5 to 10 seconds, plenty of scope for improvement.
- The LilyGo T-Display-S3 WiFi antenna on the circuit board is very crap! I have tested 2 and both were crap. I would recommend an add on antenna, looks like there is a plug for one soldered on the back of the board. 

## License
MIT License

Copyright (c) 2025 Steve Metrax

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# For the beginner
- Here's the bit where I try to explain to the complete beginner how you get this working! I often find myself looking at project's on github and wishing there was a very beginner orientated "How To", well this is my attempt to help out the absolute beginners.  "strap in" 

### Installing Thonny IDE – Windows PC
- I found this to be a very good guide that will help you install Thonny, load the firmware and give it a quick test.
https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/

The firmware is here
- https://github.com/russhughes/st7789_mpy
- Click on "Code" and "Download ZIP"
- Unzip the file on you local PC
- Handley the firmware is in the "Firmware" folder

### I'm going to assume you have Thonny installed and the Lilygo T-Display-S3 connected with the correct firmware.

- Open Thonny
- Select "View" and then "Files"
- In files point to where you have "main.py" and "vga2_8x16.py"
- Double click on "main.py" and update the following lines to match you own settings.
 
![Unifi Monitor Image](https://github.com/steve-metrax/Unifi-Monitor/blob/main/lines-to-edit.jpg).  

- Right click on "main.py" and "Upload to /", this will send to file to the Lilygo board
- Right click on "vga2_8x16.py" and "Upload to /", this will send to file to the Lilygo board
- Reset the board
- Your Lilygo display board should connect to your wifi, login to your Unifi gateway and display the real time bandwidth.

