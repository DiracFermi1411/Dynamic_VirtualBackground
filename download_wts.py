import os

# Specify the Google Drive link and the destination folder
google_drive_link = "https://drive.google.com/file/d/1XS8-W__x2jCgeM3LDrqmdXH0WKRrwa5F/view?usp=drive_link"
destination_folder = "weights"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Use wget to download the file
os.system(f"gdown -O {os.path.join(destination_folder, 'pano.ckpt')} {google_drive_link}")