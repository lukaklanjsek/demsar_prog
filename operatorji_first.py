#a, b = b, a #zamenjava vrednosti spremenljivk
#a, b = b, a + b #v spremenljivko a se napiše vrednost b, v b se pa izracuna a+b
#3.14 % 1.4 = a  #pri 3,14 % 1,4 = a mi je dal syntax error, predlaga ==
#print(a)
#v konzoli je izracunalo z pikami namesto vejicami

#ime = "Miran"
#print("Na splet je prisel" (ime or "Anonymous"))  #string object is not callable    ##kasneje ugotovil da mi manjka +
#print(ime)
#print("Bil je " + ime)  #zadnji popravek: dodan presledek pred drugim "
#print("obiskal je " + (ime and "anonymous"))   #or spremenim v and
#ce bi bilo "ime" prazno:
#ime = ("")
#print("obiskal vas je " + (ime or "ded mraz"))  #prejsnjo str "ime" dam v komentar  #ne dela, dam v komentar tudi printe 9-11
#zdaj dela ko dodam definicijo ime in prazno vrednost :)

#if a is None
#counting starts at zero 0

#j = range(5, 12) #beginning instructions were "for j = 5 to 12" and it doesnt work
#print("*")
#next j
#comment: something close to this supposingly worked before python 3.0

#print(range(12))
#a = range(12, 5, -2)
#print(a)  #this is not working
#for i in range(10):
#    print("*", end=" ")
#this finally works

#if sentences
#a = 9
#b = 14
#if a > 12 or b == 42:
#    f()
#elif a < 0 or b == 2:
#    g()
#elif a > 10:
#    h()
#else:
#    j()
#the above does not work - i couldn't get it to work

#while sentences
#i = 1
#while i <= 10:
#    print(i)
#    i += 1 #beware running the program without this line
#this works very well

#s = ([1, 2, 3, 4, 5, 10])
#for i in range(len(s)):
#    print(s[i])

#for e in s:
#    print(e)
#end of day. "for" loop is doing me problems when reading through the material. I am at page 32 to 34 right now.

s = [(1), (2), (3), (4), (5), (6), (7), (8), (9)]
#naj_i = naj_e = -1
#for i, e in enumerate(s):  #defining "s"
#    if i < 0 or naj_e < e:
#        naj_i, naj_e = i, e
        #giving this a pause and running alternative first
#alternative:
naj = None
for ie in enumerate(s): #using definition "s" from earlier
    if naj is None or naj[1] < ie[1]:
        naj = ie
print(naj[0])
print(naj[1])
## this finally prints resulting in: 1 and (7, 8, 9) so noa i am reconfiguring the definintion of "s" again
### i dont know why but i had to put ever y number in that list into ()
a = ("Miran") #i only copy-pasted the code from above:
naj = None
for ie in enumerate(a):
    if naj is None or naj[1] < ie[1]:
        naj = ie
print(ie)  #this doesnt work at first  a->ie  --> this throws out result: (4, 'n') I guess it works, now trying to enumerate in console
#no, something does not work in console, which differs from what the suggestion does in the book

s = ["Miran", "Miha", "Mitja"]
for e in "Miran":  #interesting, i dont know why this works
    print(e, ord(e)) #"ord" returns Unicode code point for one character string

pass
for i in range(10):
    print(i)
for i in range(6, 11):
    print(i)

for e in s: #here I would need an explanation what is 'e'
    print(e)

#for a while   #just messing around sorry
#    else pass

a = b = 1  #is any of the first 100 fibonacci numbers dividable by 1131
for i in range(100):
    if a % 1131 == 0:
        print(a, "is possible")
        break
    a, b = b, a+b  #why is this fibonacci rule after the print(a) and break line ???
else:   #also question: why is this in line with 'for' and not 'if'?
    print("no pass")
## surprise
