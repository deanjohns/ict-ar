# A/L ICT 6.2 — Transmission Media in AR

3D cutaway models students can view by scanning a QR code in their notes.
Works on any modern phone — no app to install.

- **twisted-pair**, **coaxial**, **fibre**, **combined** — each has a `.glb` (Android + 3D preview everywhere) and a `.usdz` (iOS AR Quick Look)
- `index.html` lists all four; each `*.html` page shows one model with a **View in your room** button
- `qr/` holds the four printable QR codes

---

## Host it on GitHub Pages — 5 steps

1. Go to **github.com → New repository**. Name it exactly **`ict-ar`**, set it **Public**, click **Create**.
2. On the repo page click **Add file → Upload files**. Drag in **everything in this folder** (the `.html`, `.glb`, `.usdz` files and the `qr` folder). Click **Commit changes**.
3. Go to **Settings → Pages**. Under *Build and deployment → Source*, choose **Deploy from a branch**. Pick branch **`main`**, folder **`/ (root)`**, click **Save**.
4. Wait ~1 minute. The page shows your live address:
   **`https://YOUR-USERNAME.github.io/ict-ar/`**
5. Open that address on your phone to test. Tap any model, then **View in your room**.

That's it — the site is live and free.

---

## Make the QR codes point to your address

The QR codes in this folder (and in the Word document) currently use a
placeholder address. To make them live:

- **Easiest:** send your GitHub username back to me and I'll hand you the
  Word document with working QR codes baked in.
- **Or do it yourself:** `pip install qrcode pillow`, open **`make_qr.py`**,
  change `BASE_URL` to your address from step 4, run `python make_qr.py`,
  and replace the QR images in your notes with the new ones from `qr/`.

> If you name the repo exactly `ict-ar`, the only thing that differs from the
> placeholder is your username — everything else already matches.

---

## Notes

- **iOS** uses the `.usdz` file for AR; **Android** uses the `.glb`. Both are included, so keep every file together in the same folder.
- The pages load the model-viewer library and fonts from the internet, so the **first** scan needs a data/Wi-Fi connection.
- To add more models later (e.g. an Arduino board for Unit 11), drop new `.glb`/`.usdz` + `.html` files into the same repo and add a QR for them.
