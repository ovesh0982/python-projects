from pdf2docx import Converter

def convert_pdf_to_word(pdf_file, word_file):
    # Initialize the converter
    cv = Converter(pdf_file)
    # Convert the PDF to Word
    cv.convert(word_file, start=0, end=None)  # You can specify start and end pages
    # Close the converter
    cv.close()
    print(f'PDF has been converted to Word: {word_file}')

# Example usage
pdf_file = 'C:/Users/DESKTOP/Desktop/python/convertpdf_to_word/1000042886.pdf'  # Path to your PDF file
word_file = 'ooo.dock'  # Path to save the Word document
convert_pdf_to_word(pdf_file, word_file)
