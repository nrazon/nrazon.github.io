# Play geliştirici sayfası görsellerini üretir (Chrome headless + Pillow). Çıktı: Downloads\play-developer-page
# Kullanım: .\tools\devpage\yap.ps1   (yeni uygulama eklenince header.html'e ikonunu ekle)
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
$kok = $PSScriptRoot
$cikti = Join-Path $env:USERPROFILE 'Downloads\play-developer-page'
New-Item -ItemType Directory -Force $cikti | Out-Null
$gecici = Join-Path $env:TEMP 'devpage'
New-Item -ItemType Directory -Force $gecici | Out-Null

function Cek($boyut, $dosya, $sayfa) {
    Remove-Item "$gecici\$dosya" -ErrorAction SilentlyContinue
    Start-Process -FilePath $chrome -Wait -NoNewWindow -ArgumentList '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--force-device-scale-factor=1', "--window-size=$boyut", "--screenshot=$gecici\$dosya",
        "file:///$($kok.Replace('\','/'))/$sayfa" | Out-Null
}
Cek '512,512' 'icon.png' 'icon.html'
Cek '4096,2304' 'header.png' 'header.html'

$py = @"
from PIL import Image
import os
c = r'$cikti'
t = r'$gecici'
ic = Image.open(os.path.join(t, 'icon.png')).convert('RGB').resize((512, 512), Image.LANCZOS)
ic.save(os.path.join(c, 'developer-icon-512.png'), optimize=True)
h = Image.open(os.path.join(t, 'header.png')).convert('RGB')
assert h.size == (4096, 2304), h.size
for q in (95, 92, 88, 84, 80, 75):
    p = os.path.join(c, 'header-image-4096x2304.jpg')
    h.save(p, 'JPEG', quality=q, optimize=True, subsampling=0 if q >= 88 else 2)
    if os.path.getsize(p) < 1000 * 1000:
        print('header kalite', q, os.path.getsize(p) // 1024, 'KB'); break
print('ikon', os.path.getsize(os.path.join(c, 'developer-icon-512.png')) // 1024, 'KB')
"@
$betik = Join-Path $gecici 'pil.py'
Set-Content -Path $betik -Value $py -Encoding UTF8
py -3 -I $betik
