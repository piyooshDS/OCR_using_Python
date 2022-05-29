from tabula import read_pdf
from tabula import convert_into
import PyPDF2

pdf1File=open('FNB Cheque Aug15.pdf','rb')
pdf1Reader=PyPDF2.PdfFileReader(pdf1File)
print pdf1Reader.numPages
pdfWriter = PyPDF2.PdfFileWriter()

for pagenum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage()
	pdfWriter.addPage(pageObj)
	

pdfOutputFile = open('FNB Cheque Aug15.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
	


df = read_pdf("combi2.pdf", output_format="json")
df = convert_into("combi2.pdf","test_FNB.csv",output_format="csv")


f=open('3.txt','w+')

print >> f,df

f.close()


