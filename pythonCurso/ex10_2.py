#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

tuple = tuple()
list = list()
dict = dict()

for line in handle:
    l = line.split()
    if("From" in l):
        #print(l)
        #print(l[5])
        word = l[5]
        #print(word)
        hour = word.split(':')
        #print(hour)
        h = hour[0]
        #print(h)
        
        dict[h] = dict.get(h,0) + 1

list = sorted([ (v,k) for v,k in dict.items()])

for k, v in list:
    print(k, v)
