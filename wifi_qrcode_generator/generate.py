import qrcode

ssid = input("Network name: ")
password = input("Password:")

# Format the WiFi information as a string
wifi_string = f"WIFI:T:WPA;S:{ssid};P:{password};;"

# Generate the QR code
img = qrcode.make(wifi_string)

# Save the QR code to a file.
img.save("qrcode.png")

# NOTE: THE QR CODE MAY NOT SHOW UP IN THE SOLUTION EXPLORER. YOU MAY HAVE TO OPEN THE FILE EXPLORER ON YOUR DESKTOP AND FIND THE .PNG FILE IN THERE.