import streamlit as st
from pypdf import PdfWriter, PdfReader

st.set_page_config(page_title="📄 PDF Merger Tool", layout="centered")

st.title("📄 PDF Merger Tool")
st.write("Upload your PDF files below to merge them into one.")

# Upload multiple PDFs
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    writer = PdfWriter()

    for uploaded_file in uploaded_files:
        # Read PDF directly from the uploaded file
        reader = PdfReader(uploaded_file)

        # Add each page to writer
        for page in reader.pages:
            writer.add_page(page)

    # Create in-memory merged PDF
    from io import BytesIO
    merged_pdf = BytesIO()
    writer.write(merged_pdf)
    merged_pdf.seek(0)

    st.success("✅ Merging completed successfully!")

    # Download button
    st.download_button(
        label="📥 Download Merged PDF",
        data=merged_pdf,
        file_name="merged_output.pdf",
        mime="application/pdf"
    )
