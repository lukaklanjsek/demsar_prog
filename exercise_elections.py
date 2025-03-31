"""
It is election season! The candidates are numbered from  1 to StKandidatov, which is smaller or same than MaxStKandidatov.
Assemble a subprogram that would draw a histogram of results.

shape and form of expected subprogram:

const MaxStVolilcev = ...; MaxStKandidatov = ...;
type GlasoviT = array [1..MaxStKandidatov] of integer;

procedure Histogram(StKandidatov, StVolilvec: integer; Glasovi: GlasoviT);
begin
 ...
end;
"""

# begin:

max_st_volilcev = int(input("Najvecje stevilo volilcev je: "))

max_st_kandidatov = int(input("Najvecje stevilo kandidatov je: "))
st_volilcev = 0
st_kandidatov = 0



while True:
    st_kandidatov = int(input("Koliko je dejanskih kandidatov: " ))
    if 0 < st_kandidatov <= max_st_kandidatov:
        break
    else:
        print(f"Vnos dejanskega števila kandidatov, med 1 in {max_st_kandidatov}")

while True:
    st_volilcev = int(input("Koliko vas dejansko voli: "))
    if 0 < st_volilcev <= max_st_volilcev:
        break
    else:
        print(f"Prosimo vnesite število volilcev, ki je med 1 in {max_st_volilcev}")

glasovi_T = []
i = 0
for i in range(0, st_volilcev):
    while True:
        try:

            glas = int(input(f"Vnesi glasove enega na enkrat: {i+1}.:"))
            if 0 < glas <= st_kandidatov:
               glasovi_T.append(glas)
               break
            else:
                print(f"Iščemo številko med 1 in {st_kandidatov}")
        except ValueError:
            print("Prosim vnesite številko.")

print("list of glasovi_T: ", glasovi_T)    # test print to see where we are

import matplotlib.pyplot as plt

plt.hist(glasovi_T)
plt.show()
