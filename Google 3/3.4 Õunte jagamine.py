
from random import randint
lv = 14
sum = 0
arv = int(input("Mitu pöialpoissi tahab õuna? "))
while sum < arv:
 rand = randint(1,2)
 print(str(rand))
 lv = lv - rand
 sum = sum + 1
print("Lumivalgeksele jäi " + str(lv) + " õuna.")