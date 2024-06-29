import PyPDF2, re
def reading_pdf_text(filename):

    with open(filename, 'rb') as f:

        pdf = PyPDF2.PdfReader(f)

        num_pages = len(pdf.pages)

        text = ''

        for page in pdf.pages:

            page_text = page.extract_text()

            text += page_text

        text = re.sub(r'(\w)([A-Z])', r'\1 \2', text)
        text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)

        return text
