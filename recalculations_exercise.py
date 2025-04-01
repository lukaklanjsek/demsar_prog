"""
Write a program, that would use standard input of ten rows with seven numbers,
followed by a row of ten numbers, that would tell order sufficiency.
input values order: lige, milje, furlongi, jardi, čevlji, dlani, palci
by the relations between values:
    1 liga = 3 milje,
    1 milja = 8 furlongov,
    1 furlong = 220 jardov,
    1 jard = 3 čevlji,
    1 čevelj = 3 dlani,
    1 dlan = 4 palci;
Use the biggest units possible.

example: 5000 jardov = 0 2 6 160 0 0 0.
"""

lige = 0
milje = 0
furlongi = 0
jardi = 0
cevlji = 0
dlani = 0
palci = 0

print("Hello and welcome the recalculations exercise. Please enter your 10 orders:")

for i in range(0, 1):
    while True:
        try:
            liga, milja, furlong, jard, cevelj, dlan, palec = map(int, input(f"Order count {i+1} (seven numbers): ").split())
            lige += liga
            milje += milja
            furlongi += furlong
            jardi += jard
            cevlji += cevelj
            dlani += dlan
            palci += palec
            i += 1
            break

        except ValueError:
            print("please enter 7 numbers")

print("pre-calc: ", lige, milje, furlongi, jardi, cevlji, dlani, palci)    # test print

dlani += palci // 4
palci = palci % 4
cevlji += dlani // 3
dlani = dlani % 3
jardi += cevlji // 3
cevlji = cevlji % 3
furlongi += jardi // 220
jardi = jardi % 220
milje += furlongi // 8
furlongi = furlongi % 8
lige += milje // 3
milje = milje % 3

print("post-calc: ", lige, milje, furlongi, jardi, cevlji, dlani, palci)    # test print II

lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1 = 0, 0, 0, 0, 0, 0, 0

while True:
    try:
        lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1 = map(int, input("Enter what you told the factory: ").split())
        break
    except ValueError:
        print("please enter 7 collected numbers")

while True:
     if True:
        lige == lige1
        milje == milje1
        furlongi == furlongi1
        jardi == jardi1
        cevlji == cevlji1
        dlani == dlani1
        palci == palci1
        print("Narocil si ravno prav blaga")
        break
     elif lige < lige1 and  milje < milje1 and  furlongi < furlongi1 and jardi < jardi1 and  cevlji < cevlji1 and  dlani < dlani1 and  palci < palci1:
            print("Narocil si *** prevec blaga")
            break
     else:
         print("Narocil si *** premalo blaga")
         break

"""
                elif True:
                lige > lige1
                milje > milje1
                furlongi > furlongi1
                jardi > jardi1
                cevlji > cevlji1
                dlani > dlani1
                palci > palci1
                print("Narocil si *** premalo blaga")
"""