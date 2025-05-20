import pikepdf

old_pff = pikepdf.Pdf.open("C:/Users/DESKTOP/Desktop/python/pdfprotection/pdf2.pdf")

no_extr = pikepdf.Permissions(extract=False)

old_pff.save("protected.pdf",encryption=pikepdf.Encryption(user="123asd",owner="ovesh",allow=no_extr))