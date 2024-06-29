import qrcode

# QR kodu oluşturacak URL
pdf_url = "https://Kendi URL'nizi Giriniz !!!"  # Buraya PDF dosyanızın URL'sini yapıştırın

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(pdf_url)
qr.make(fit=True)

# QR kodu resim dosyası olarak kaydetme
img = qr.make_image(fill_color="black", back_color="white")
img.save("Olusacak_qr_kod_ismini_giriniz.png")

print("QR kodu başarıyla oluşturuldu ve menu_qr.png olarak kaydedildi.")

