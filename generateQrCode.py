import qrcode
from PIL import Image

# Paramètres du QR code
qr = qrcode.QRCode(
    version=1,  # Contrôle la taille du QR code (1 à 40, 1 étant le plus petit)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Niveau de correction d'erreur (H est le plus élevé)
    box_size=10,  # Taille de chaque "boîte" du QR code
    border=4,  # Taille de la bordure (en boîtes)
)
qr.add_data("https://www.dever.host")
qr.make(fit=True)

# Créer l'image du QR code
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Charger le logo
logo = Image.open("devericon.png")

# Redimensionner le logo (environ 20% de la taille du QR code)
logo_size = img.size[0] // 5
logo = logo.resize((logo_size, logo_size))

# Calculer la position pour centrer le logo
logo_position = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2
)

# Superposer le logo sur le QR code
img.paste(logo, logo_position, logo)

# Sauvegarder le QR code final
img.save("qrcode_with_logo.png")

print("QR code avec logo généré avec succès : qrcode_with_logo.png")