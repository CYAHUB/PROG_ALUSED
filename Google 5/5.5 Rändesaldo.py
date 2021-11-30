fail = open("sisseranne.txt", encoding="UTF-8")
fail1 = open("valjaranne.txt", encoding="UTF-8")
sisse = []
välja = []
for rida in fail:
    sisse.append(int(rida))
for rida1 in fail1:
    välja.append(int(rida1))
for i in range(len(sisse)):
    sisse[i] = sisse[i] - välja[i]
print(sisse)




