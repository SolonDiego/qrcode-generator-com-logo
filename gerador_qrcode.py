import qrcode
from PIL import Image

# Caminhos
logo_path = "Sticker_Instagram_Logo_simple_compose.png"
insta_url = "https://www.instagram.com/"
output_path= "qrcode_instagram.png"

# Geração de QR Code básico
qr = qrcode.QRCode(
    version=2, # Define o tamanho do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Alta correção de erro para suportar a logo
    box_size=10,
    border=4,
)
qr.add_data(insta_url)
qr.make(fit=True)

qr_img = qr.make_image(back_color=(255,255,255), fill_color=(178,55,104))

# Abrir e redimencionar a logo
logo = Image.open(logo_path)
logo_size = 100
logo.thumbnail((logo_size, logo_size))

# Posição central para colar a logo
qr_width, qr_height = qr_img.size
logo_position = ((qr_width - logo_size) // 2 + 20, (qr_height - logo_size) // 2)
qr_img.paste(logo, logo_position, mask=logo if logo.mode == 'RGBA' else None)

# Mostrar a imagem gerada
qr_img.show()

#Salvando o QR code com a logo como imagem
qr_img.save(output_path)