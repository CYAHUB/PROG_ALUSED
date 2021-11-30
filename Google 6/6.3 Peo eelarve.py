def nice(nice):
    maxeelarve = kutsutud * 10 + 55
    return (maxeelarve)

def noice(eelarvearv2):
    mineelarve = tuleb * 10 + 55
    return (mineelarve)

kutsutud = int(input("Mitu inimest on kutsutud? "))
tuleb = int(input("Mitu inimest tuleb? "))

#mineelarve = str(input("Mitu kilogrammi õunu on? "))
#maxeelarve = str(input("Mitu kilogrammi õunu on? "))

print("Maksimaalne eelarve: " + str(nice(kutsutud)))
print("Minimaalne eelarve: " + str(noice(tuleb)))