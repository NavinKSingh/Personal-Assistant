import ctypes
from output1 import output
import os

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20  
    SPIF_UPDATEINIFILE = 0x01  
    SPIF_SENDWININICHANGE = 0x02  

    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False

def update_wallpaper():
    image_path = input("Enter the full path of the image to set as wallpaper: ")
    image_path = os.path.abspath(image_path)
    output(image_path)
    
    if not os.path.isfile(image_path):
        print(f"Error: The file at path {image_path} does not exist.")
    elif change_wallpaper(image_path):
        print("Wallpaper changed successfully!")
    else:
        print("Failed to change wallpaper.")
