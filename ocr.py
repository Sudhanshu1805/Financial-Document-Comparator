# --- ocr.py ---
# Extract text from PDFs and images
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import os

def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF files using PyPDF2."""
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_image(image_path):
    """Extracts text from image files using Tesseract OCR."""
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)