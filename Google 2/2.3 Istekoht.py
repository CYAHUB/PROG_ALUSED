from random import randint
istekoht = str(input("Kas soovite istekohta ise valida (Ise) või loosida (loos)?"))
if istekoht == "ise":
    text1 = "Valisite ise."
    aken = str(input("Kas soovite istuda akna ääres (aken) või mitte (muu)?"))
elif istekoht == "loos":
    text1 = "Istekoht loositi."

if istekoht == "ise":
    if aken == "aken":
        text2 = "Aknakoht"
    elif aken == "muu":
        text2 = "Vahekäigukoht"
elif istekoht == "loos":
    arv = randint(1, 3)
    if arv == 1:
        text2 = "Aknakoht"
    elif arv == 2 or 3:
        text2 = "Vahekäigukoht"
print(text1 + " " + text2)

