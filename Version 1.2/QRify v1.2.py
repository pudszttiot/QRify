import sys
import qrcode
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QProgressBar, QToolTip
from PyQt5.QtGui import QPalette, QColor, QIntValidator, QIcon
from PyQt5.QtCore import Qt, QTimer

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRify")
        self.setFixedSize(400, 200)
        self.setGeometry(400, 250, 400, 250)
        self.setWindowIcon(QIcon(r"..\Images\QRify Window1.ico"))

        self.data_label = QLabel("Enter the Data:")
        self.data_entry = QLineEdit()
        self.data_entry.setPlaceholderText("Enter URL or text")
        self.file_name_label = QLabel("Save it as:")
        self.file_name_entry = QLineEdit()
        self.file_name_entry.setPlaceholderText("Enter file name")
        self.generate_button = QPushButton("QRify Code")
        self.clear_button = QPushButton("Clear")
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.status_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.data_entry)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.file_name_entry)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)

        self.generate_button.clicked.connect(self.generate_qr_code)
        self.clear_button.clicked.connect(self.clear_inputs)

        self.setLayout(layout)

    def generate_qr_code(self):
        data = self.data_entry.text()
        image_name = self.file_name_entry.text()

        if not data:
            QMessageBox.warning(self, "Warning", "Please enter data.")
            return

        if not re.match(r'^[a-zA-Z0-9_\-.]+$', image_name):
            QMessageBox.warning(self, "Warning", "Please enter a valid file name without special characters.")
            return

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png)", options=options)

        if file_path:
            self.progress_bar.setValue(0)
            self.progress_bar.setVisible(True)
            self.status_label.setText("QRifying code...")

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            qr_img.save(file_path)
            self.status_label.setText("QRific!, code generated and saved")
            self.progress_bar.setVisible(False)
        else:
            self.status_label.setText("QR code generation cancelled")

    def clear_inputs(self):
        self.data_entry.clear()
        self.file_name_entry.clear()
        self.status_label.clear()

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
