

import qrcode
from PIL import Image


def generate_qr_code(data, file_name="qrcode.png"):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image file
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")

# Example usage
generate_qr_code("https://www.example.com", "example_qrcode.png")
