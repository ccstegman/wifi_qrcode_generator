import qrcode

ssid = input("Network name: ")
password = input("Password:")

# Format the WiFi information as a string
wifi_string = f"WIFI:T:WPA;S:{ssid};P:{password};;"

# Generate the QR code
img = qrcode.make(wifi_string)

# Save the QR code to a file
img.save("qrcode.png")