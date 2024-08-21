pituus = float(input("Anna kalan pituus:"))
if(pituus < 37):
    print("Heitä takasin järveen! kala on " + str(37-pituus) + " senttiä liian lyhyt")
else:
    print("Hyvä kala")