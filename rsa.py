import sys

f = open(sys.argv[1],"r")
contents = f.readlines()
p, q = 0 , 0

for i in contents:
    if " " in i:
        #set p and q values
        pstring, qstring = i.split()
        p = int(pstring)
        q = int(qstring)
        n = (p * q)
        print (n)

    else:
        print (i)
        #do necessary calculations and print statements




