import os, urllib.request

url = "https://tigermomo.pythonanywhere.com/static/img/logo.png"
icon_dir = os.path.join(os.path.dirname(__file__), 'assets', 'icon')
os.makedirs(icon_dir, exist_ok=True)
icon_file = os.path.join(icon_dir, 'app_icon.png')

print(f"Downloading app icon from {url} to {icon_file}...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        with open(icon_file, 'wb') as f_out:
            f_out.write(response.read())
    print("Downloaded app_icon.png successfully!")
except Exception as e:
    print(f"Error downloading icon: {e}")
