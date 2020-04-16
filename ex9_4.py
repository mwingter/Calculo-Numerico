#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
maior = None
maiorEmail = None

for line in handle:
    l = line.split()
    #print(l)
    if ("From" in l):
        #print(l[1])
        word = l[1]
        count[word] = count.get(word,0) + 1
        if (maior == None or maior < count[word]):
            maior = count[word]
            maiorEmail = word
            
print(maiorEmail,maior)
