import webbrowser
import subprocess

def open_facebook():
    webbrowser.open("https://facebook.com")

def open_google():
    webbrowser.open("https://google.com")
    
def open_youtube():
    webbrowser.open("https://youtube.com")

def close_browser():
    command = 'taskkill /F /IM chrome.exe'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("Browser is closed")
    else:
        print("Failed to close the browser")
