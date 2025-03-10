""" LilyGo T-Display-S3 320x170 ST7789 display - UniFi Bandwidth Log Bars with Outlines (Autostart) """

from machine import Pin, SPI, freq, PWM
import st7789
import vga2_8x16 as font
import utime
import network
import urequests as requests
import ujson as json
import math

freq(240000000)

WIFI_SSID = "YourCorrectSSID"  # Replace with your actual WiFi SSID
WIFI_PASSWORD = "YourCorrectPassword"  # Replace with your actual WiFi password
CONTROLLER_URL = "https://192.168.1.1"  # UniFi controller URL
USERNAME = "username"  # UniFi controller username
PASSWORD = "password"  # UniFi controller password
SITE = "default"  # UniFi site name
MAX_SPEED = 950  # Maximum bandwidth in Mbps
MIN_SPEED = 0.1  # Minimum visible bandwidth for log scale

GREY = 0x808080  # Custom grey color (RGB 128,128,128 in 16-bit)

def config(rotation=1, buffer_size=0, options=0):
    """Configure the ST7789 display for landscape mode (320x170)."""
    LCD_POWER = Pin(15, Pin.OUT)
    LCD_POWER.value(1)
    return st7789.ST7789(
        Pin(48, Pin.OUT), Pin(47, Pin.OUT), Pin(46, Pin.OUT), Pin(45, Pin.OUT),
        Pin(42, Pin.OUT), Pin(41, Pin.OUT), Pin(40, Pin.OUT), Pin(39, Pin.OUT),
        Pin(8, Pin.OUT), Pin(9, Pin.OUT),
        170, 320,
        reset=Pin(5, Pin.OUT), cs=Pin(6, Pin.OUT), dc=Pin(7, Pin.OUT),
        backlight=Pin(38, Pin.OUT),
        rotation=rotation, options=options, buffer_size=buffer_size)

tft = config(1, buffer_size=64*64*2)

def connect_wifi():
    """Establish WiFi connection, return IP on success, None on failure."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        tft.fill(GREY)
        tft.text(font, "WiFi...", 10, 77, st7789.WHITE, GREY)
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            utime.sleep(1)
            timeout -= 1
        if not wlan.isconnected():
            return None
    return wlan.ifconfig()[0]

def login_unifi():
    """Authenticate with UniFi controller, return cookie on success, None on failure."""
    login_url = f"{CONTROLLER_URL}/api/auth/login"
    login_data = {"username": USERNAME, "password": PASSWORD}
    headers = {"Content-Type": "application/json"}
    
    tft.fill(GREY)
    tft.text(font, "Login...", 10, 77, st7789.WHITE, GREY)
    try:
        response = requests.post(login_url, data=json.dumps(login_data), headers=headers)
        if response.status_code == 200:
            cookie = None
            if hasattr(response, 'headers') and 'Set-Cookie' in response.headers:
                cookie = response.headers['Set-Cookie']
            elif 'set-cookie' in response.raw_headers:
                cookie = response.raw_headers['set-cookie']
            if cookie:
                return cookie
            return None
        return None
    except Exception:
        return None

def get_unifi_stats(cookie):
    """Fetch bandwidth (upload/download) and client count from UniFi."""
    stats_url = f"{CONTROLLER_URL}/proxy/network/api/s/{SITE}/stat/health"
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    try:
        response = requests.get(stats_url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            total_tx_bytes = 0
            total_rx_bytes = 0
            for entry in data['data']:
                if entry['subsystem'] == 'wan':
                    total_tx_bytes += entry.get('tx_bytes-r', 0)
                    total_rx_bytes += entry.get('rx_bytes-r', 0)
            total_tx_mbps = total_tx_bytes / 125000
            total_rx_mbps = total_rx_bytes / 125000
        else:
            return None, None, None
    except Exception:
        return None, None, None

    clients_url = f"{CONTROLLER_URL}/proxy/network/api/s/{SITE}/stat/sta"
    try:
        response = requests.get(clients_url, headers=headers)
        if response.status_code == 200:
            clients_data = json.loads(response.text)
            client_count = len(clients_data['data'])
            return total_tx_mbps, total_rx_mbps, client_count
        return total_tx_mbps, total_rx_mbps, None
    except Exception:
        return total_tx_mbps, total_rx_mbps, None

def draw_log_bar(x, y, speed, min_speed, max_speed, color, label):
    """Draw a logarithmic bar graph with white outline, filling based on speed."""
    tft.rect(x - 1, y - 2, 302, 34, st7789.WHITE)
    speed = min(max(speed, min_speed), max_speed)
    log_min = math.log10(min_speed)
    log_max = math.log10(max_speed)
    log_speed = math.log10(speed)
    bar_length = int(300 * (log_speed - log_min) / (log_max - log_min))
    tft.fill_rect(x, y, bar_length, 30, color)
    speed_str = f"{label}: {speed:.1f} Mbps"
    tft.text(font, speed_str, x, y + 38, st7789.WHITE, GREY)

def main():
    """Initialize and run the UniFi dashboard continuously on power-on."""
    try:
        tft.init()
        backlight = PWM(Pin(38))
        backlight.freq(1000)
        backlight.duty_u16(11000)
        
        ip = connect_wifi()
        if not ip:
            tft.fill(GREY)
            tft.text(font, "No WiFi", 10, 77, st7789.WHITE, GREY)
            utime.sleep(2)
            return
        
        cookie = login_unifi()
        if not cookie:
            tft.fill(GREY)
            tft.text(font, "Login Fail", 10, 77, st7789.WHITE, GREY)
            utime.sleep(2)
            return
        
        tft.fill(GREY)
        tft.text(font, "Stats...", 10, 77, st7789.WHITE, GREY)
        for i in range(11000, 65536, 500):
            backlight.duty_u16(i)
            utime.sleep(0.08)
        
        while True:
            tx_mbps, rx_mbps, client_count = get_unifi_stats(cookie)
            tft.fill(GREY)
            if tx_mbps is not None and rx_mbps is not None:
                draw_log_bar(10, 10, tx_mbps, MIN_SPEED, MAX_SPEED, st7789.RED, "Upload")
                draw_log_bar(10, 70, rx_mbps, MIN_SPEED, MAX_SPEED, st7789.GREEN, "Download")
                if client_count is not None:
                    client_str = f"Clients: {client_count}"
                    tft.text(font, client_str, 10, 130, st7789.WHITE, GREY)
            else:
                tft.text(font, "No Data", 10, 77, st7789.WHITE, GREY)
            utime.sleep(0.5)
        
    finally:
        backlight.duty_u16(0)
        backlight.deinit()
        tft.deinit()

main()