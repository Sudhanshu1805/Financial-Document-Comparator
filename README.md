# AI-Powered Financial Document Comparison Tool

## Overview
This project is a tool to analyze and compare financial documents. It extracts text using OCR, calculates text similarity using TF-IDF and cosine similarity, and detects anomalies with Isolation Forest.

## Features
- Extract text from PDF and image files
- Compare documents using text similarity
- Detect anomalies in document content

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-doc-comparator.git
   cd financial-doc-comparator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

## Usage
1. Upload two financial documents (PDF or images).
2. View the similarity score and anomaly predictions.

## Technologies Used
- PyPDF2
- Tesseract OCR
- Scikit-learn
- Streamlit
- Python

## License
This project is open-source under the MIT License.
