# LilyGo T-Display S3 UniFi Dashboard

A MicroPython-based dashboard for monitoring UniFi network bandwidth (upload/download) and connected clients on the LilyGo T-Display S3 (320x170 landscape).

![Unifi Monitor Image](https://github.com/steve-metrax/Unifi-Monitor/blob/main/Image%202025-03-10%20at%2023.32.14_82104025.jpg)

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
1. Flash MicroPython firmware for LilyGo T-Display S3 (download from https://github.com/russhughes/st7789_mpy).
2. Use Thonny or another IDE to upload `main.py` and `vga2_8x16.py` to the device.
3. Update `WIFI_SSID`, `WIFI_PASSWORD`, `CONTROLLER_URL`, `USERNAME`, and `PASSWORD` in `main.py` with your settings.
4. Power on via USB or battery—the dashboard will autostart.

## Usage
- The display shows bar graphs for upload/download speeds, client count, and status messages.
- Adjust `MAX_SPEED` or `utime.sleep()` in `main.py` if needed for your bandwidth or refresh rate.

## Credits
- Created by Steve Upson with help from Grok 3 (xAI), quite alot of help actually as this is not in my wheelhouse! The networking bit is very much in my wheelhouse.
- Uses libraries from [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy).

## License
MIT License

Copyright (c) 2025 Steve Upson

Permission is hereby granted, free of charge, to any person obtaining a copy...
