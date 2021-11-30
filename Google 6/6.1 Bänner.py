def banner(lause):
    return lause.upper()

arv = int(input("Sisestage mitu korda äratada: "))
arv2 = str(input("Sisestage reklaamlause: ")).upper()

for i in range(arv):
    print(banner(arv2))
    