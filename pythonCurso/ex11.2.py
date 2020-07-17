import re
hand = open('dados/regex_bigsum.txt', 'r')
numList = list()
n = 0

for line in hand:
    line = line.rstrip()
    #print('Line: ', line)
    stuff = re.findall('[0-9]+', line)

    if len(stuff) < 1 : continue

    print('Stuff: ', stuff)
    for val in stuff:
        num = float(val)
        numList.append(num)
        n+=1


sum = sum(numList)
print('Soma de', n, 'numeros:', sum)