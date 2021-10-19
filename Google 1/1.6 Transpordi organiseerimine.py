print("Kui palju on inimesi : ")
inimestearv = int(input())
print("Kui palju on kohti?")
kohtadearv = int(input())
bussid = float(inimestearv) // kohtadearv
mahajäänud = inimestearv % kohtadearv
if mahajäänud > 0:
    bussid = bussid + 1
    print(str(mahajäänud) + " inimesi jäi maha. Tuli lisada üks buss juurde mis on kokku busse : " + str(bussid))
else:
    print("Inimesi ei jäänud maha kedagi.")
