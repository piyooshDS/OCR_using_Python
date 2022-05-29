import csv
import json
import re

csvfile = open('test_fnb.csv', 'r')
jsonfile = open('fnb.json', 'w')

fieldnames = ["Date","Description A "," Description b","Description c","Amount","Balance","Accrued Bank Charges"]
reader = csv.DictReader( csvfile,fieldnames)
a=0
b=[]
for row in reader:
	a+=1
	if(a>1):

		b.append(row)
		out=json.dumps(b)


jsonfile.write(out)

'''with open('fn.json', 'r') as infile, open('fnb.json', 'w') as outfile:
    temp = infile.read().replace("\u00ad", "-")
    outfile.write(temp)'''





# handle=open('file5.json')
# for i in handle:
# 	print(json.loads(i))
# 	if('\u00ad' in i):
# 		i.replace('\u00ad','')
# handle.close()
# 	# regex = re.compile(r"^.*\u00ad*$", re.IGNORECASE)
# 	for line in out:
# 		   out.write(line)



