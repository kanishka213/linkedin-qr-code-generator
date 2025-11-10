import qrcode

linkedin_url = "https://www.linkedin.com/in/kanishka-srivastava-cse/"  

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(linkedin_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("linkedin_qr.png")

print("✅ LinkedIn QR code generated successfully! Saved as 'linkedin_qr.png'")
