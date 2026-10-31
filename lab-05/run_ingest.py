from pathlib import Path
from ingest import ingest_pdf, DATA_DIR

class CLIUploadedFile:
    def __init__(self, file_path: Path):
        self.path = file_path
        self.name = file_path.name

    def getvalue(self):
        return self.path.read_bytes()

if __name__ == "__main__":
    # Point to your handbook inside the data folder
    pdf_path = DATA_DIR / "COMPUTING AWARD HANDBOOK_MOHE (2).pdf"
    
    if pdf_path.exists():
        print(f"Ingesting: {pdf_path.name}...")
        mock_file = CLIUploadedFile(pdf_path)
        result = ingest_pdf(mock_file)
        print(result)
    else:
        print(f"Error: Could not find PDF at {pdf_path}")