õuntekogus = float(input("Mitu kilogrammi õunu on? "))
def mahlapakkidearv(mahlapakkidearv):
    pakid = õuntekogus * 0.4 / 3
    return round(pakid)

print(mahlapakkidearv(õuntekogus))