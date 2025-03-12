# LilyGo T-Display S3 UniFi Dashboard

A MicroPython-based dashboard for monitoring UniFi network bandwidth (upload/download) and connected clients on the LilyGo T-Display S3 (320x170 landscape).

![Unifi Monitor Image](https://github.com/steve-metrax/Unifi-Monitor/blob/main/IMG_9638.JPG)

## Features
- Displays upload and download speeds (0.1-950 Mbps, logarithmic scale) as bar graphs with outlines.
- Shows connected client count.
- Updates every ~5-10 seconds via UniFi API.
- Runs autonomously on power-on.

## Hardware
- LilyGo T-Display S3 (ESP32-S3, ST7789 display, 320x170).
- USB power adapter or LiPo battery (3.7V, 500mAh+).

## Software
- MicroPython firmware for ESP32-S3.
- https://github.com/russhughes/st7789_mpy
- Required files: `main.py`, `vga2_8x16.py`.

## Installation
1. Flash MicroPython firmware for LilyGo T-Display S3 (download from https://github.com/russhughes/st7789_mpy). Nice one Russ, a steep learing curve but got there in the end.
2. Use Thonny or another IDE to upload `main.py` and `vga2_8x16.py` to the device.
3. Update `WIFI_SSID`, `WIFI_PASSWORD`, `CONTROLLER_URL`, `USERNAME`, and `PASSWORD` in `main.py` with your settings.
4. Power on via USB or battery—the dashboard will autostart.

## Usage
- The display shows bar graphs for upload/download speeds, client count, and status messages.
- Adjust `MAX_SPEED` or `utime.sleep()` in `main.py` if needed for your bandwidth or refresh rate.

## Credits
- Created by Steve Upson with help from Grok 3 (xAI), quite alot of help actually as this is not in my wheelhouse! The networking bit is very much in my wheelhouse.
- Uses libraries from [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy), again thanks Russ!
- ZX Spectrum BASIC is about the limit of my knowlege when it comes to programing so getting this working did give me a bit of a buzz.

## Improvements
- Looks, I'm no graphic artist so plenty of scope for improvement
- Refresh, the display refresh is once every 5 to 10 seconds, plenty of scope for improvement.

## License
MIT License (not sure what this means but it's yours, use/mod as you want, just give me a mention)

Copyright (c) 2025 Steve Upson

Permission is hereby granted, free of charge, to any person obtaining a copy...

## For the beginner
Here's the bit where I try to explain to the complete beginner how you get this working, "strap in" !


