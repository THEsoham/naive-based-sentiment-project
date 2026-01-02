import pypdf

class DataAgent:
    def process_input(self, uploaded_file):
        if uploaded_file.name.endswith('.pdf'):
            reader = pypdf.PdfReader(uploaded_file)
            # Extract text from all pages
            raw_text = " ".join([page.extract_text() for page in reader.pages])
            return raw_text
        elif uploaded_file.name.endswith('.txt'):
            return uploaded_file.read().decode("utf-8")
        else:
            return "Unsupported Format"