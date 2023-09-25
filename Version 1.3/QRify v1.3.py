import sys
import qrcode
import re
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMenuBar,
    QMenu, QAction, QFrame, QScrollArea, QSpacerItem, QSizePolicy,
    QMessageBox, QFileDialog, QProgressBar, QToolTip
)
from PyQt5.QtGui import QPalette, QColor, QIntValidator, QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer

class QRCodeGenerator(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app  # Store the QApplication instance

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRify")
        self.setFixedSize(400, 200)
        self.setGeometry(400, 250, 400, 250)
        self.setWindowIcon(QIcon(r"..\Images\QRify Window1.ico"))

        # Set Fusion style with a dark theme
        self.app.setStyle("Fusion")

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

        # Set the palette for the QR code generator page
        self.setPalette(dark_palette)

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
            self.status_label.setText("QRifyed!, code generated and saved")
            self.progress_bar.setVisible(False)
        else:
            self.status_label.setText("QR code generation cancelled")

    def clear_inputs(self):
        self.data_entry.clear()
        self.file_name_entry.clear()
        self.status_label.clear()

class HomePage(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app  # Store the QApplication instance

        self.init_ui()

    def init_ui(self):
        # Set up the main window
        self.setWindowTitle("QRify")
        self.setFixedSize(800, 600)
        self.setGeometry(300, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\QRify Window1.ico"))

        # Set Fusion style with a dark theme
        self.app.setStyle("Fusion")

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

        # Set the palette for the home page
        self.setPalette(dark_palette)

        # Create a QLabel to display the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap(r"..\Images\QRify BG 2.jpg")

        # Set the desired width and height for the background image
        desired_width = 1280
        desired_height = 720
        pixmap = pixmap.scaled(desired_width, desired_height)

        # Calculate the position to center the background image
        label_x = int((self.width() - pixmap.width()) / 2)
        label_y = int((self.height() - pixmap.height()) / 2)

        self.background_label.setGeometry(label_x, label_y, pixmap.width(), pixmap.height())
        self.background_label.setPixmap(pixmap)

        # Ensure the label is behind all other widgets
        self.background_label.lower()

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 800, 500)  # Cover the whole window
        pixmap = QPixmap(r"..\Images\QRify Logo 2.png")
        
        # Define the desired width and height (adjust these values as needed)
        label_width = 650
        label_height = 350
        self.image_label.setPixmap(pixmap.scaled(label_width, label_height, aspectRatioMode=1))

        # Center the label in the window
        label_x = int((650 - label_width) / 2) + 190
        label_y = int((350 - label_height) / 2) - 20
        self.image_label.move(label_x, label_y)

        # Create a button to open the QR code generator page
        self.open_qr_button = QPushButton("Generate QR Code", self)
        self.open_qr_button.setGeometry(245, 450, 320, 70)
        self.open_qr_button.clicked.connect(self.open_qr_page)

        # Apply custom style to the button
        self.open_qr_button.setStyleSheet(
            """
            QPushButton {
                background-color: #e3e5e4;
                color: #191919;
                border: 2px solid #000000;
                border-radius: 5px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #e3e5e4;
                border: 2px solid #e3e5e4;
                border-radius: 5px;
                font-size: 20px;
            }
            """
        )

    def open_qr_page(self):
        self.qr_page = QRCodeGenerator(self.app)
        self.qr_page.show()
        self.hide()

class PageManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.homepage = HomePage(self.app)
        self.qr_page = QRCodeGenerator(self.app)
        self.current_page = None

    def show_homepage(self):
        if self.current_page:
            self.current_page.close()
        self.homepage.show()
        self.current_page = self.homepage

    def show_qr_page(self):
        if self.current_page:
            self.current_page.close()
        self.qr_page.show()
        self.current_page = self.qr_page

    def run(self):
        self.show_homepage()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    page_manager = PageManager()
    page_manager.run()
