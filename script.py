f = open ("echocardiogram.data", 'r', newline='')
f2 = open ('123.data', 'w')
for row in f:
    line = str()
    for s in row.split(','):
        s = s.strip()
        if s == 'name':
            line = line + '1' + ','
        elif s == '?':
            line = line + '0' + ','
        else:
            line = line + str(round(float(s))) + ','
    f2.write(line)
    f2.write('\n')
f2.close()
f.close()

f2 = open ('123.data', 'r')
l = f2.readlines()
f2.close()
f3 = open('321.data', 'w')
for line in l:
    k = 0
    for s in line:
        if k == 13:
            
    # f3.write(a)
    # f3.write("\n")
f3.close()