import os
from pypdf import PdfReader

class DataAgent:
    def __init__(self, raw_dir="data/raw"):
        self.raw_dir = raw_dir
        # Ensure the directory exists
        if not os.path.exists(self.raw_dir):
            os.makedirs(self.raw_dir)

    def handle_upload(self, uploaded_file):
        """Saves file and returns the text content."""
        # 1. Save the file to the destination folder
        file_path = os.path.join(self.raw_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # 2. Extract text based on file type
        if uploaded_file.name.endswith('.pdf'):
            return self._extract_pdf(file_path)
        else:
            return self._extract_txt(file_path)

    def _extract_pdf(self, path):
        reader = PdfReader(path)
        return " ".join([p.extract_text() for p in reader.pages])

    def _extract_txt(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()