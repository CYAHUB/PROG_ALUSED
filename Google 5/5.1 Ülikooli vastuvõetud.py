wat = int(input("Palun sisestage, millise aasta andmeid vajate: "))

fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()

print(str(wat) + " aastal oli vastuvõetuid " + str(vastuvõetud[2011 - wat]))

