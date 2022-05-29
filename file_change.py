with open('file5.json', 'r') as infile, open('r2.json', 'w') as outfile:
    temp = infile.read().replace("\u00ad", "")
    outfile.write(temp)