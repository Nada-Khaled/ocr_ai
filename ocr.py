import os
import sys

import easyocr

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(SCRIPT_DIR, "front_id_3.3MB.png")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "result.txt")
LANGUAGES = ["ar", "en"]


def main():
    # if not os.path.isfile(IMAGE_PATH):
    #     print(f"Image not found: {IMAGE_PATH}", file=sys.stderr)
    #     print("Place an image named 'front_id_3.3MB.png' next to this script and try again.", file=sys.stderr)
    #     sys.exit(1)

    print(f"Loading EasyOCR model for language(s): {', '.join(LANGUAGES)} ...")
    reader = easyocr.Reader(LANGUAGES)

    print(f"Reading text from {IMAGE_PATH} ...")
    results = reader.readtext(IMAGE_PATH, detail=0)
    text = "\n".join(results) if results else "(no text found)"

    print("\n--- Extracted text ---")
    print(text)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nSaved extracted text to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
