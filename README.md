## qr_read - QR Code Reader

Short description  
**Reads textual information from an image file (GIF, PNG, JPEG, etc.) by scanning for QR codes and printing decoded text to the console.**

---

## Project layout
- qr_read/ - program source
  - main module (entrypoint shown in repository root or inside qr_read)
  - miscellaneous.py - helper utilities used by the program

---

## Requirements
- **Python 3.8+**
- Python packages:
  - opencv-python
  - pyzbar

Install with pip:
```bash
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencv-python pyzbar
```

On Debian/Ubuntu (alternative / additional system packages):
```bash
sudo apt-get install python3-opencv python-zbar libzbar0 && sudo apt-get clean
```

---

## Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-directory>
```
2. (Optional) Create and activate a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org opencv-python pyzbar
```

If you provide a requirements.txt, use:
```bash
pip install -r requirements.txt
```

---

## Usage
Run the program with the required -f / --qr_file argument pointing to the image file containing the QR code:
```bash
python3 -m qr_read -f path/to/image.png
```
Or, if the package is not installed as a module:
```bash
python3 qr_read/main.py -f path/to/image.png
```
Output:
- Prints each decoded QR-code line to stdout, prefixed with "Строка из QR-кода:" (the program's messages are in Russian).
- If nothing is found, the program reports that no QR data was found in the specified file.

---

## Behavior details
- Images are loaded with OpenCV and decoded with pyzbar.
- Non-printable ASCII control characters are removed from decoded text using a regular expression before printing.
- The program verifies the input file is readable via Miscellaneous.is_file_readable() before attempting decoding.
- Console messages and prompts are in Russian.

---

## Examples
Generate a sample QR code (for example at http://qrcoder.ru), save it as qrcode.png and run:
```bash
python3 -m qr_read -f qrcode.png
```
Expected console output: decoded text lines printed (one per line), or a message indicating nothing was found.

---

## Troubleshooting
- If pyzbar cannot find zbar on Linux, install libzbar (libzbar0 / zbar-tools).
- If decoding fails on small or low-resolution images, try a higher-resolution image or re-save it with better quality.

---

## License
This project is licensed under **GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007**.
