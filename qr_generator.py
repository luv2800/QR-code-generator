import qrcode

data = input("Enter text or URL to generate QR code:\n")
img = qrcode.make(data)
img.save("my_qr.png")
print("✅ QR Code saved as my_qr.png")





