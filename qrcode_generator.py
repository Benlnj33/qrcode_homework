import os
import qrcode

class QRCodeGenerator:
    def __init__(self, url, image_path):
        self.url = url
        self.image_path = image_path

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=2,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.image_path)
        print("QR code image saved successfully:", self.image_path)

        # Display the QR code in the terminal
        self.display_ascii_qr_code()

    def display_ascii_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        # Print the ASCII representation of the QR code
        qr.make(fit=True)
        qr.print_ascii()

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
