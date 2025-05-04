"""
Herhangi bir PDF dosyasının en sonuna boş sayfa ekler.
"""

from pypdf import PdfWriter


def add_blank_slide_to_pdf(input_pdf: str, output_pdf: str) -> None:
    """
    Adds a blank slide of specified size to the end of a PDF file.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_pdf (str): Path to the output PDF file.
    """
    merger = PdfWriter()
    merger.append(input_pdf)
    merger.add_blank_page()
    merger.write(output_pdf)
    merger.close()


def main():
    input_path = "giris-pdfler/meta-intro.pdf"
    output_path = "result.pdf"
    add_blank_slide_to_pdf(input_path, output_path)


if __name__ == "__main__":
    main()
