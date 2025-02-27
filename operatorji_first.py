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