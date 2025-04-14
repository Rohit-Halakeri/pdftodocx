import streamlit as st
from pdf2docx import Converter
import os
import tempfile

st.set_page_config(page_title="PDF to DOCX Converter", layout="centered")

st.title(" PDF to DOCX Converter")
st.write("Upload a PDF and get a Word file (.docx) version using `pdf2docx`.")

uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_pdf is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_pdf.read())
        pdf_path = temp_pdf.name

    docx_name = uploaded_pdf.name.replace(".pdf", ".docx")
    docx_path = os.path.join(tempfile.gettempdir(), docx_name)

    if st.button("Convert to DOCX"):
        try:
            st.info("Converting...")
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            with open(docx_path, "rb") as f:
                st.success(" Conversion complete!")
                st.download_button(label="⬇ Download DOCX",
                                   data=f,
                                   file_name=docx_name,
                                   mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        except Exception as e:
            st.error(f"Conversion failed: {e}")
