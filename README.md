# OCR AI code

A simple command-line OCR tool powered by [EasyOCR](https://github.com/JaidedAI/EasyOCR).

## Setup

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Place an image named `image.png` in this folder, then run:

```bash
python ocr.py
```

The extracted text is printed to the console and saved to `result.txt`.

To change the image filename or language, edit the `IMAGE_PATH` / `LANGUAGES` constants at the top of `ocr.py`.
