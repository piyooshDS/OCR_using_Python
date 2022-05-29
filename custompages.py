from tabula import read_pdf
from tabula import convert_into
import csv
#df = read_pdf("Nedbank Cheque Account.pdf", output_format="csv",pages="2-8")
df = read_pdf("Nedbank_ocr.pdf", pages="all",multiple_tables=True)

df = convert_into("Nedbank_ocr.pdf","test_fnb.csv",output_format="csv", pages="all",multiple_tables=True)

with open("test_fnb.csv", "rb") as f:
    data = list(csv.reader(f))

with open("test_fnb.csv", "wb") as f:
    writer = csv.writer(f)
    for row in data:
    	if row[0] != "Date Transaction":
    	 writer.writerow(row)


