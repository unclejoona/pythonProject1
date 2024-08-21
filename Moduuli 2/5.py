import math
luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

input1 = float(input("Anna leiviskät.\n"))
input2 = float(input("Anna naulat.\n"))
input3 = float(input("Anna luodit.\n"))
sum = float(input1*leiviska +input2*naula + input3*luoti)
print("Massa nykymittojen mukaan:")
if(sum > 1000):
    print(str(int(sum/1000)) + " kilogrammaa ja " + str(round(sum%1000,2)) + " grammaa.")
else:
    print(str(sum) + " grammaa.")