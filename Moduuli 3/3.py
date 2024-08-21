sukupuoli = str(input("Anna biologinen sukupuolesi:"))
hemo = int(input("Anna hemoglobiiniarvo:"))

if ((sukupuoli == "nainen" and
    hemo >= 117 and hemo <= 175) or
    (sukupuoli == "mies" and
    hemo <= 195 and hemo >= 134)):
    print("Hemoglobiiniarvosi ovat normaalit.")
elif((sukupuoli == "mies" and hemo > 195) or
     (sukupuoli == "nainen" and hemo > 175)):
    print("Hemoglobiiniarvosi ovat korkeat.")
else:
    print("Hemoglobiiniarvosi ovat alhaiset.")