import qrcode
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, filedialog

def generate_qr_code():
    data = data_entry.get()
    image_name = file_name_entry.get()
    
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
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=image_name)
        if file_path:
            qr_img.save(file_path)
            status_label.config(text="QR code generated and saved")
        else:
            status_label.config(text="QR code generation cancelled")
    else:
        status_label.config(text="Please enter data and image name")

# Create a tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Data input
data_label = Label(window, text="Enter the Data:")
data_label.pack()
data_entry = Entry(window)
data_entry.pack()

# Image name input
file_name_label = Label(window, text="Name it as:")
file_name_label.pack()
file_name_entry = Entry(window)
file_name_entry.pack()

# Generate button
generate_button = Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Status label
status_label = Label(window, text="")
status_label.pack()

window.mainloop()
