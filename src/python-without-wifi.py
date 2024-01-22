#First, install the micropython-ble library on your ESP32. You can do this by connecting to the ESP32 via the REPL (Read-Eval-Print Loop) and running the following command:
import upip
upip.install("micropython-ble")

#Now, you can use the following code to advertise a BLE service that allows you to send WiFi credentials to the ESP32:
import ubluetooth as bluetooth
import ubinascii
import time

def on_rx(handler):
    while ble.gatts_if == -1:
        pass

    def on_gatt_rx_event(event, handler=handler):
        conn_handle, value_handle = handler.get_event_data()
        data = handler.read_event(conn_handle, value_handle)
        handler.write_event(conn_handle, value_handle, b"\x01")  # Acknowledge receipt
        handler.prepare_write_event(conn_handle, value_handle, 0)  # Enable notifications
        return data

    ble.on_gatts_rx_event(250, on_gatt_rx_event)

def on_tx(handler):
    def on_gatt_tx_event(event, handler=handler):
        conn_handle, value_handle, is_notify = handler.get_event_data()
        handler.prepare_write_event(conn_handle, value_handle, 0)  # Enable notifications
        return None

    ble.on_gatts_tx_event(250, on_gatt_tx_event)

def advertise_service(name):
    ble.gap_advertise(100, bytearray("\x02\x01\x02") + bytearray("\x06\x03\x03\x0A\x18") + ubinascii.a2b_hex("1600") + bytearray("\x02\x09") + name)

def main():
    ble.active(True)
    ble.gap_advertise(100, bytearray("\x02\x01\x02") + bytearray("\x06\x03\x03\x0A\x18") + ubinascii.a2b_hex("1600"))
    ble.gatts_register_services(1)
    ble.gap_advertise(100, bytearray("\x02\x01\x02") + bytearray("\x06\x03\x03\x0A\x18") + ubinascii.a2b_hex("1600") + bytearray("\x02\x09") + "WiFiConf")

    while not ble.gatts_if:
        pass

    on_rx(ble.gatts_subscribe, on_gatt_rx_event)
    on_tx(ble.gatts_subscribe, on_gatt_tx_event)

    advertise_service("WiFiConf")

if __name__ == "__main__":
    ble = bluetooth.BLE()
    main()