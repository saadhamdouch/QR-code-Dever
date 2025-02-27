import qrcode

# Créer un QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://www.dever.host")
qr.make(fit=True)

# Sauvegarder le QR code en tant qu'image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcodedever.png")