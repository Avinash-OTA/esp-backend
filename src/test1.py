
import network

def wifiTest():
   ssid = "your-SSID"
   password = "your-PASSWORD"

   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect(ssid, password)

   while not wlan.isconnected():
       pass

   print("Connected to Wi-Fi")
   print("Connected to Wi-Fi")
   print("IP Address:", wlan.ifconfig()[0])


if __name__ == "__main__":
    wifiTest() 