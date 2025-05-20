import PyPDF2

# Open the PDF file
with open('C:/Users/DESKTOP/Desktop/python/table_extraction/pdf1.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    
    # Loop through all pages
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    # Print extracted text
    print(text)

