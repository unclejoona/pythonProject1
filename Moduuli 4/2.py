i = 0
while(True):
    luku = float(input("Anna tuuman pituus,\n "
                       "negatiivinen luku lopettaa ohjelman:"))
    if(luku<0):
        break
    print(luku*2.54)