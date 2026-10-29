# FCC 12 Slip Systems Visualizer — Flask

This project serves the supplied FCC slip-systems webpage through Python Flask. The original HTML, CSS, and browser-side JavaScript are preserved in `templates/index.html`, including the Three.js visualizer, preset systems, custom plane/direction controls, Schmid-factor calculator, and PNG export controls.

## Run locally (Windows)

1. Install Python 3.10 or newer.
2. Extract this folder, then open Command Prompt or PowerShell in the folder.
3. Create and activate a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start Flask:

   ```powershell
   python app.py
   ```

6. Open **http://127.0.0.1:5000** in your browser.

## Run locally (macOS / Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000**.

## Notes

- Flask serves the page; the interactive 3D scene and calculations run in your browser.
- The page loads Three.js and OrbitControls from public CDNs, so an internet connection is required for those libraries unless you choose to host them locally.
- This is configured for local development. Before deploying publicly, turn off Flask debug mode and use a production WSGI server.
