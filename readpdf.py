from PyPDF2 import PdfReader


def read_files_to_text(multiple_files):
    texts = []
    for file in multiple_files:
        if is_pdf(file):
            texts.append(read_all_text(file))
        else:
            # skip
            pass
    return texts


def is_pdf(file):
    return file.name.endswith(".pdf")


def read_all_text(file):
    pdf = PdfReader(file)
    return "".join([page.extract_text() for page in pdf.pages])
