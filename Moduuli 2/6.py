import random

code1 = str()
for i in range(3):
    code1 += str(random.randint(1,9))
code2 = str()
for i in range(4):
    code2 += str(random.randint(1,6))
print("eka lukko koodi:" + code1)
print("toinen lukko koodi:" + code2)
