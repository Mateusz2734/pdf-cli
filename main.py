from pypdf import PdfMerger, PdfReader, PdfWriter, PageRange

reader = PdfReader("test1.pdf")

print(len(reader.pages))

rang = PageRange(":8").indices(3)
print(rang)