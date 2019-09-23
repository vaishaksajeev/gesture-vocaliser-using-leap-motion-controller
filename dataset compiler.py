import csv

with open('headers.csv','r') as rFile:
    reader = csv.reader(rFile)
    lines = list(reader)
with open('data.csv', 'wb') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)


alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alph:
    x='asla '
    x+=i
    x+='.csv'
    with open(x,'r') as rFile2:
        reader=csv.reader(rFile2)
        line=list(reader)
        del line[0]
    with open('data.csv', 'ab') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)


