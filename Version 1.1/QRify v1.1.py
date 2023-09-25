import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 400, 200)

        self.data_label = QLabel("Enter the Data:")
        self.data_entry = QLineEdit()
        self.file_name_label = QLabel("Name it as:")
        self.file_name_entry = QLineEdit()
        self.generate_button = QPushButton("Generate QR Code")
        self.status_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.data_entry)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.file_name_entry)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.status_label)

        self.generate_button.clicked.connect(self.generate_qr_code)

        self.setLayout(layout)

    def generate_qr_code(self):
        data = self.data_entry.text()
        image_name = self.file_name_entry.text()

        if data and image_name:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png)", options=options)

            if file_path:
                qr_img.save(file_path)
                self.status_label.setText("QR code generated and saved")
            else:
                self.status_label.setText("QR code generation cancelled")
        else:
            self.status_label.setText("Please enter data and image name")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()

    # Set Fusion style with a dark theme
    app.setStyle("Fusion")

    # Customize dark theme colors
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    
    # Set the palette for the application
    app.setPalette(dark_palette)

    window.show()
    sys.exit(app.exec_())
