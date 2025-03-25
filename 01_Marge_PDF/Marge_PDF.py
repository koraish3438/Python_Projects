from PyPDF2 import PdfMerger

Pdf_list = ["1.pdf", "2.pdf", "3.pdf", "4.pdf" , "5.pdf", "6.pdf" , "7.pdf", "8.pdf" , "9.pdf"]

New_Pdf = PdfMerger()

for i in Pdf_list:
    New_Pdf.append(i)

New_Pdf.write("BS.pdf")
New_Pdf.close()