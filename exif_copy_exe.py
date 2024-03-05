import tkinter as tk
from tkinter import filedialog
from PIL import Image
import piexif

def extract_exif_from_png():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    exif_data = img.info.get("exif")
    if exif_data:
        with open("exif_data.txt", "wb") as f:
            f.write(exif_data)
        status_label.config(text="eXIf data extracted successfully.")
    else:
        status_label.config(text="No eXIf data found in the selected PNG file.")

def embed_exif_to_jpeg():
    png_exif_path = "exif_data.txt"
    jpeg_file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not jpeg_file_path:
        return
    img = Image.open(jpeg_file_path)
    with open(png_exif_path, "rb") as f:
        exif_data = f.read()
    exif_dict = piexif.load(exif_data)
    exif_bytes = piexif.dump(exif_dict)
    img.save(jpeg_file_path, "jpeg", exif=exif_bytes, quality=100, optimize=False, icc_profile=img.info.get('icc_profile'), subsampling=0)
    status_label.config(text="eXIf data embedded successfully.")

# GUIの作成
root = tk.Tk()
root.title("eXIf Chunk Transfer")
root.geometry("300x150")

# ボタンの作成
extract_button = tk.Button(root, text="Extract eXIf from PNG", command=extract_exif_from_png)
extract_button.pack(pady=10)

embed_button = tk.Button(root, text="Embed eXIf to JPEG", command=embed_exif_to_jpeg)
embed_button.pack(pady=5)

# ステータスラベルの作成
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()