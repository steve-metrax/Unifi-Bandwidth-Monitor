# LilyGo T-Display S3 UniFi Dashboard

A MicroPython-based dashboard for monitoring UniFi network bandwidth (upload/download) and connected clients on the LilyGo T-Display S3 (320x170 landscape).

![Unifi Monitor Image](https://github.com/steve-metrax/Unifi-Monitor/blob/main/IMG_9638.JPG)

https://lilygo.cc/products/t-display-s3

## Features
- Displays upload and download speeds (0.1-950 Mbps, logarithmic scale) as bar graphs with outlines.
- Shows connected client count.
- Updates every ~5-10 seconds via UniFi API.
- Runs autonomously on power-on.

## Hardware
- LilyGo T-Display-S3 (ESP32-S3, ST7789 display, 320x170).
- USB power adapter or LiPo battery (3.7V, 500mAh+).
- Tested Ubiquiti UniFi Cloud Gateway Ultra, other Unifi routers mileage may vary!

## Software
- MicroPython firmware for ESP32-S3.
- https://github.com/russhughes/st7789_mpy
- Required files: `main.py`, `vga2_8x16.py`.

## Installation
1. Flash MicroPython firmware for LilyGo T-Display S3 (download from https://github.com/russhughes/st7789_mpy). Nice one Russ, a steep learning curve but got there in the end.
2. Use Thonny or another IDE to upload `main.py` and `vga2_8x16.py` to the device.
3. Update `WIFI_SSID`, `WIFI_PASSWORD`, `CONTROLLER_URL`, `USERNAME`, and `PASSWORD` in `main.py` with your settings.
4. Power on via USB or battery—the dashboard will autostart.

## Usage
- The display shows bar graphs for upload/download speeds, client count, and status messages.
- Adjust `MAX_SPEED` or `utime.sleep()` in `main.py` if needed for your bandwidth or refresh rate.

## Credits
- Created by Steve Upson with help from Grok 3 (xAI), quite a lot of help actually as this is not in my wheelhouse! The networking bit is very much in my wheelhouse.
- Uses libraries from [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy), again thanks Russ!
- ZX Spectrum BASIC is about the limit of my knowledge when it comes to programming so getting this working did give me a buzz.

## Improvements
- Looks, I'm no graphic artist so plenty of scope for improvement
- Refresh, the display refresh is once every 5 to 10 seconds, plenty of scope for improvement.
- The LilyGo T-Display-S3 WiFi antenna on the circuit board is very crap! I have tested 2 and both were crap. I would recommend an add on antenna, looks like there is a plug for one soldered on the back of the board. 

## License
MIT License (not sure what this means but it's yours, use/mod as you want, just give me a mention)

Copyright (c) 2025 Steve Upson

Permission is hereby granted, free of charge, to any person obtaining a copy...

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











