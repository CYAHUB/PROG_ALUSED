fail = open("konto.txt", encoding="UTF-8")   
pos = []

for rida in fail:
    pos.append(float(rida))
fail.close()
for element in pos:
    if element > 0:
        print(element)
     
