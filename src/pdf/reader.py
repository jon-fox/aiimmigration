import fitz  # PyMuPDF dependency

def read_pdf(file_path):
    # open pdf file
    with fitz.open(file_path) as doc:
        text = ""
        # Iterate through each page in the PDF
        for page in doc:
            # Extract text from the current page
            text += page.get_text()
    return text

# Specify the path to your PDF file
file_path = "../../documents/i-130.pdf"
text = read_pdf(file_path)
print(text)
