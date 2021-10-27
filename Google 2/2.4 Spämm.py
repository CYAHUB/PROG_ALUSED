suurus = float(input("Sisestage kirja suurus: "))
pealkiri = str(input("Sisestage kirja teema pealkiri: "))
fail = str(input("Kas kirjaga on kaasas fail? "))
print1 = "Kiri ei ole spämm"
print2 = "Kiri on spämm"

if suurus < 1.0 and fail == "jah":
    print(print1)
elif pealkiri == "":
    print(print2)
else:
    print(print2)