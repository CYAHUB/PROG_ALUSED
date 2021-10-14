name = str(input("Mis nimi on : "))
lubatud_kiirus = int(input("Mis on lubatud kiirus : "))
ületatud_kiirus = int(input("Mis on ületatud kiirus : "))
oled = ületatud_kiirus - lubatud_kiirus
trahv = oled * 3
trahv1 = min(trahv, 190)
print (str(name) + " oli ületanud " + str(oled) + "(km/h) ja trahv on " + str(trahv1)+ " eurot.")
