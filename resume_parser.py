from pdfminer.high_level import extract_text
import tempfile

def extract_resume_text(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        text = extract_text(temp_path)

        if text:
            return text.lower()

        return ""

    except Exception as e:
        return ""