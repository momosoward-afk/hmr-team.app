import os, urllib.request

url = "https://tigermomo.pythonanywhere.com/static/img/logo.png"
print(f"Downloading app icon from {url}...")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        img_bytes = response.read()
except Exception as e:
    print(f"Error downloading icon: {e}")
    img_bytes = None

if img_bytes:
    res_dir = os.path.join(os.path.dirname(__file__), 'android', 'app', 'src', 'main', 'res')
    folders = ['mipmap-mdpi', 'mipmap-hdpi', 'mipmap-xhdpi', 'mipmap-xxhdpi', 'mipmap-xxxhdpi']
    for f in folders:
        target_dir = os.path.join(res_dir, f)
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, 'ic_launcher.png')
        with open(target_file, 'wb') as img_out:
            img_out.write(img_bytes)
        print(f'Generated {target_file}')
