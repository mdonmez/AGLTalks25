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


# USE THIS IF YOU WANT TO ADD A BLANK SLIDE
# def add_blank_slide_to_pdf(input_pdf: str, output_pdf: str) -> None:
#     """
#     Adds a blank slide of specified size to the end of a PDF file.

#     Args:
#         input_pdf (str): Path to the input PDF file.
#         output_pdf (str): Path to the output PDF file.
#     """
#     merger = PdfWriter()
#     merger.append(input_pdf)
#     merger.add_blank_page()
#     merger.write(output_pdf)
#     merger.close()


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
        "eski-sunum-pdfler/meta-intro.pdf",
        "eski-sunum-pdfler/hilal-sunum.pdf",
        "eski-sunum-pdfler/betul-sunum.pdf",
        "eski-sunum-pdfler/yasin-sunum.pdf",
        "eski-sunum-pdfler/nehir-sunum.pdf",
        "eski-sunum-pdfler/hacer-sunum.pdf",
        "eski-sunum-pdfler/cuneyt-sunum.pdf",
        "eski-sunum-pdfler/ezgi-sunum.pdf",
        "eski-sunum-pdfler/efe-sunum.pdf",
        "eski-sunum-pdfler/elif-sunum.pdf",
        "eski-sunum-pdfler/meta-outro.pdf",
    ]

    output_pdf = "META-SLIDE-2025.pdf"
    merge_pdfs(pdf_files, output_pdf)


if __name__ == "__main__":
    main()
