"""
Regenerate the QR codes after you know your GitHub Pages address.

  1.  pip install qrcode pillow
  2.  edit BASE_URL below to YOUR address
  3.  python make_qr.py
  4.  the new PNGs appear in  qr/  — print or paste them into your notes

(You only need this if you change your GitHub username or repo name.)
"""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

# ====== EDIT THIS ONE LINE =================================================
BASE_URL = "https://deanjohns.github.io/ict-ar/"
# ===========================================================================

PAGES = {
    "twisted-pair": "QR_Twisted_Pair",
    "coaxial":      "QR_Coaxial",
    "fibre":        "QR_Fibre_Optic",
    "combined":     "QR_Compare_All_Three",
}

def make(url, path):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=18, border=2)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                        fill_color=(17, 21, 26), back_color=(255, 255, 255))
    img.save(path)

if __name__ == "__main__":
    import os
    os.makedirs("qr", exist_ok=True)
    base = BASE_URL if BASE_URL.endswith("/") else BASE_URL + "/"
    for slug, name in PAGES.items():
        url = base + f"{slug}.html"
        make(url, f"qr/{name}.png")
        print(f"{name}.png  ->  {url}")
    print("\nDone. Re-print the PNGs in qr/ into your notes.")
