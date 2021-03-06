'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
lst = list()
for line in handle:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            z = line.split()
            lst.append(z[5].split(':')[0])
            
#appending the list  must be clear

flist = []
for i in lst:
    dic[i] = lst.count(i)
for key,valu in dic.items():
    flist.append((key,valu))
    
for k,v in sorted(flist):
    print(k,v)
