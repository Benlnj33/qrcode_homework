import os
import qrcode
import base64

class QRCodeGenerator:
    def __init__(self, url, image_path):
        self.url = url
        self.image_path = image_path

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.image_path)
        print("QR code image saved successfully:", self.image_path)

        # Convert the image to base64
        with open(self.image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Embed the base64-encoded image into README.md using Markdown
        with open("README.md", "a") as readme_file:
            readme_file.write(f"\n\n![QR Code](data:image/png;base64,{base64_image})")

if __name__ == "__main__":
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the URL
    url = "https://github.com/Benlnj33"

    # Define the path to save the image (in the current directory)
    image_path = os.path.join(current_directory, "github_qr.png")

    # Instantiate the QRCodeGenerator class
    qr_generator = QRCodeGenerator(url, image_path)

    # Generate and save the QR code
    qr_generator.generate_qr_code()