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

#list_of_candidates = [list() for a in range(st_kandidatov)]
#print(list_of_candidates)    # test print to see where we are


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





#number_of_arguments = len(glasovi_T)

#def the_spread():
#    for a in glasovi_T:

#for n in glasovi_T:

#    list_of_candidates.insert("n", "*")
#    break
#print(list_of_candidates[0])

"""
import matplotlib.pyplot as plt

plt.hist(glasovi_T)
plt.show()
"""
# rezultati = [[] for k in range(1, st_kandidatov)]

#l = 0
#while l < len(glasovi_T):
#    break
#print(rezultati)
#l = 0
#while l < len(glasovi_T):
#    break