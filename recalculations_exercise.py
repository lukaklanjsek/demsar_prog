"""
Write a program, that would use standard input of ten rows with seven numbers,
followed by a row of seven numbers, that would tell order sufficiency.
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

for i in range(0, 10):    # for different amount of input lines, change the "10"
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

# print("post-calc orders: ", lige, milje, furlongi, jardi, cevlji, dlani, palci)    # test print II

lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1 = 0, 0, 0, 0, 0, 0, 0

while True:
    try:
        lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1 = map(int, input("Enter what you told the factory: ").split())
        break
    except ValueError:
        print("please enter 7 collected numbers")

# print("Test print pre-calc factory order input:", lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1)    # test print

dlani1 += palci1 // 4
palci1 = palci1 % 4
cevlji1 += dlani1 // 3
dlani1 = dlani1 % 3
jardi1 += cevlji1 // 3
cevlji1 = cevlji1 % 3
furlongi1 += jardi1 // 220
jardi1 = jardi1 % 220
milje1 += furlongi1 // 8
furlongi1 = furlongi1 % 8
lige1 += milje1 // 3
milje1 = milje1 % 3

print("post calc factory input", lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1)    # test print

list_before = [lige, milje, furlongi, jardi, cevlji, dlani, palci]
list_after = [lige1, milje1, furlongi1, jardi1, cevlji1, dlani1, palci1]

differences = [(x-y) for x, y in zip(list_before, list_after)]    # če je pozitivna je naročenega premalo


def check_variables(stevilka):
    if stevilka > 0:
        return "positive"
    elif stevilka < 0:
        return "negative"
    else:
        return "zero"

if_positive = False
if_negative = False
if_zero = False

for stev in differences:
    if check_variables(stev) == "positive":
        if_positive = True
        break
    elif check_variables(stev) == "negative":
        if_negative = True
        break
    else:
        if_zero = True

# final response
if if_positive == True:
    print(f"Narocil si {differences} premalo blaga")
elif if_negative == True:
    print(f"Narocil si {differences} prevec blaga")
else:
    print("Narocil si ravno prav blaga")