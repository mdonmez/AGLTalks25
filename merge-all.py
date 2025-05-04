"""
Tüm PDF dosyalarını belirtilen sırayla birleştirir ve tek bir PDF dosyası olarak kaydeder.
"""

from pypdf import PdfWriter
from typing import List


def merge_pdfs(pdf_files: List[str], output_pdf: str) -> None:
    """
    Merges multiple PDF files into a single PDF file in the specified order.

    Args:
        pdf_files (List[str]): List of paths to PDF files to merge, in order.
        output_pdf (str): Path to the output merged PDF file.
    """
    merger = PdfWriter()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()


def main():

    # Sıra | Ad                 |
    # ---- | ------------------ |
    # 1    | META INTRO         |
    # 2    | Hatice Hilal Aslan |
    # 3    | Betül Aydoğ        |
    # 4    | Yasin Efe Başer    |
    # 5    | Nehir Oğunday      |
    # 6    | Hacer Bayram       |
    # 7    | Cüneyt Sinan Sevi  |
    # 8    | Ezgi Karaaslan     |
    # 9    | Efe Sağdıç         |
    # 10   | Elif Barın         |
    # 11   | META OUTRO         |

    pdf_files = [
        "giris-pdfler/meta-intro.pdf",
        "giris-pdfler/hilal-sunum.pdf",
        "giris-pdfler/betul-sunum.pdf",
        "giris-pdfler/yasin-sunum.pdf",
        "giris-pdfler/nehir-sunum.pdf",
        "giris-pdfler/hacer-sunum.pdf",
        "giris-pdfler/cuneyt-sunum.pdf",
        "giris-pdfler/ezgi-sunum.pdf",
        "giris-pdfler/efe-sunum.pdf",
        "giris-pdfler/elif-sunum.pdf",
        "giris-pdfler/meta-outro.pdf",
    ]

    output_pdf = "META-AGL-TALKS-SLIDE-2025.pdf"
    merge_pdfs(pdf_files, output_pdf)


if __name__ == "__main__":
    main()
