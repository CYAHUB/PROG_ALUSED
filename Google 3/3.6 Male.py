täisolevinimene = int(input("Sisestage täisarv: "))

ruutu = 64
if 1 < ruutu:
    arv = 2 ** täisolevinimene / 2
print("Nisuteri " + str(täisolevinimene) + ". ruudu eest: " + str(round(arv)))