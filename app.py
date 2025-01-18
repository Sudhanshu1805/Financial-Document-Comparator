# --- app.py ---
# Streamlit Web Application
import streamlit as st
from src.ocr import extract_text_from_pdf, extract_text_from_image
from src.similarity import calculate_similarity
from src.anomaly import detect_anomalies

st.title("AI-Powered Financial Document Comparison Tool")

uploaded_file1 = st.file_uploader("Upload the first document", type=["pdf", "png", "jpg"])
uploaded_file2 = st.file_uploader("Upload the second document", type=["pdf", "png", "jpg"])

if uploaded_file1 and uploaded_file2:
    # Extract text from files
    if uploaded_file1.name.endswith("pdf"):
        text1 = extract_text_from_pdf(uploaded_file1)
    else:
        text1 = extract_text_from_image(uploaded_file1)

    if uploaded_file2.name.endswith("pdf"):
        text2 = extract_text_from_pdf(uploaded_file2)
    else:
        text2 = extract_text_from_image(uploaded_file2)

    # Calculate similarity
    similarity_score = calculate_similarity(text1, text2)
    st.write(f"Cosine Similarity: {similarity_score:.2f}")

    # Detect anomalies (example: word counts)
    word_counts = [len(text1.split()), len(text2.split())]
    anomalies = detect_anomalies(word_counts)
    st.write(f"Anomaly Predictions: {anomalies}")