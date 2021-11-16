# 3.5
arv = int(input("Sisesta ringide arv: "))
porgandid = 0
ring = 1
while ring <= arv:
    porgandid = porgandid + ring
    ring = ring + 1
print("Porgandite koguarv on " + str(porgandid))