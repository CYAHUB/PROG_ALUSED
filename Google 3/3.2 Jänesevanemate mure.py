arv = int(input("Sisesta ringide arv: "))
porgandid = 0
ring = 1
while ring <= arv:
    if ring % 2 == 0:
        porgandid = porgandid + ring
    ring = ring + 1
print("Porgandite koguarv on " + str(porgandid))