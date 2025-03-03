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

#s = [(1), (2), (3), (4), (5), (6), (7), (8), (9)]
#naj_i = naj_e = -1
#for i, e in enumerate(s):  #defining "s"
#    if i < 0 or naj_e < e:
#        naj_i, naj_e = i, e
        #giving this a pause and running alternative first
#alternative:
#naj = None
#for ie in enumerate(s): #using definition "s" from earlier
#    if naj is None or naj[1] < ie[1]:
#        naj = ie
#print(naj[0])
#print(naj[1])
## this finally prints resulting in: 1 and (7, 8, 9) so noa i am reconfiguring the definintion of "s" again
### i dont know why but i had to put ever y number in that list into ()
#a = ("Miran") #i only copy-pasted the code from above:
#naj = None
#for ie in enumerate(a):
#    if naj is None or naj[1] < ie[1]:
#        naj = ie
#print(ie)  #this doesnt work at first  a->ie  --> this throws out result: (4, 'n') I guess it works, now trying to enumerate in console
#no, something does not work in console, which differs from what the suggestion does in the book

#s = ["Miran", "Miha", "Mitja"]
#for e in "Miran":  #interesting, i dont know why this works
#    print(e, ord(e)) #"ord" returns Unicode code point for one character string

#pass
#for i in range(10):
#    print(i)
#for i in range(6, 11):
#    print(i)

#for e in s: #here I would need an explanation what is 'e'
#    print(e)

#for a while   #just messing around sorry
#    else pass

#a = b = 1  #is any of the first 100 fibonacci numbers dividable by 1131
#for i in range(100):
#    if a % 1131 == 0:
#        print(a, "is possible")
#        break
#    a, b = b, a+b  #why is this fibonacci rule after the 'print(a)' and 'break' line ???
#else:   #also question: why is this in line aligned with 'for' and not 'if'?
#    print("no pass")
## surprise

#lets check out net example, claiming to call an url page
#import urllib.request
#for i in range(5):         #again a random 'i' in here, what for???
#    try:
#        r = urllib.request.urlopen(url) .read()    #what is now 'r' ???
#        break
#    except:
#        pass
#else:
#    print("nothing ever works")


#lets try fibonacci again, this time with a twist
#1. example code:
#def fibonacci(n):
#    a = b = 1
#    for i in range(n):
#        a, b = b, a + b
#    return a, a**2  #okay lets go
#a, a2 = fibonacci(10)    #after aligning this line with 'def', the code prints out result
#print(a, a2)  #question: why is it a2 and not a1? how does a2 work
#how does 'return' work ?

#EXERCISES
#euclid highest common divider     ##break, change environment grab the math book and pen and paper




#def euclid(a, b):  #for the start, this function will have to await
#    if
#hi im back, got distracted a bit
a = c = 144
b = d = 60
results_a = []
results_b = []
results = []
while c != 0:
    if a % c == 0:
        results_a.append(c)
        c -= 1
    else:
        c -= 1
while d != 0:
    if b % d == 0:
        results_b.append(d)
        d -= 1
    else:
        d -= 1
for i in results_a:
    for f in results_b:  #how to add logic into this line
        if i == f:
            results.append(i)
print(results[0])  #finally got working showing only the first input into the results list
#something works, but unsure why  #it doesnt work, always throws out "4"  ##still doesnt work, but it throws out something

# perfect numbers

#import math

#n = 91
#math.sqrt(n) == a   #to ni vredu
#def prastevilo(n):
#    for a in range(n):
#        if n % a != 0:    #here the logic needs rewording
#            a -= 1
#
#print(prastevilo(n))

#lists
s = ["Ana", "Berta", "Cilka",
     "Dani", "Ema",
     "Fani", ]
airports = [
    "Ljubljana - Joze Pucnik",
    "London - Gatwick",
    "Pariz - Charles de Gaulle",
]
#print(s[0:2])
#print(s[2:5])
#print(s[-2:])
#print(s[ : ])
#print(s[::-1])  #woo hoo
s.append("Ingrid")
s.insert(3, "Ester")
s.insert(3, "Erika")
s.extend(["Jasna", "Karla"])
s += ["Cireja", "Creda"]
s[3:3] = ["Ines", "Ahmed"]
#print(s)
s[4:4] = ["Dragica", "Evgenija"]
s += ["Francka"]
s.sort(reverse=True)
print(s)
s = []
#for i in range(5):
#    s.append([])
#s = [[]for i in range(6)]

#examples
s = [1, 2, 3, 4, 5, 6,]
t = [1, 3, 5, 7]
def primerjaj(s, t):
    if s < t:
        return(-1)
    elif s == t:
        return(0)
    elif not s < t:
        return(1)
print(primerjaj(s, t))
