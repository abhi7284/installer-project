import zipfile
import os
import sys

# Determine the path for the bundled zip file
if getattr(sys, 'frozen', False):
    # If the script is running in a bundle, find the bundled zip
    zip_file_path = os.path.join(sys._MEIPASS, "capture.zip")
else:
    # For testing outside PyInstaller, you can place the zip file in the same folder
    zip_file_path = "capture.zip"

# Define the extraction directory
extract_to = "extracted_files"  # Adjust as needed

# Create the extraction directory if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f"Extracted {zip_file_path} to {extract_to}")
