hytit = ["A","B","C","LUX"]

input1 = str(input("Anna hyttiluokka:"))

if input1 in hytit:
    if input1 == hytit[0]:
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif input1 == hytit[1]:
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif input1 == hytit[2]:
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka")