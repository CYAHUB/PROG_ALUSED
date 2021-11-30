fail = str(input("Palun sisestage failinimi: "))
tundmatu = []
loend = 0
muusika = open(fail, encoding="UTF-8")
for rida in muusika:
    loend += 1
    tundmatu.append(str(rida))
    print(str(round(loend)) + ". " + rida)
search = int(input("Valige laulu järjekorranumber: "))
print("Mängitav muusikapala on " + str(tundmatu[-1 + search]))