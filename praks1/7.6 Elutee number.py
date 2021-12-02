def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i) 
    if n < 10:
        return n
    else:
        return elutee(str(n))
fail = open("sunnikuupaevad.txt")
a = 1
while a <= 9:
    elutee = open("eluteenumber" + str(a) + ".txt", encoding = "UTF-8")
    elutee.close()
o = 1
for rida in fail:
    while elutee(rida) != o:
        o += 1
    failinimi = "eluteenumber" + str(o)
    fail1 = open(failinimi + ".txt", "a", encoding = "UTF-8" )
    fail1.write(rida + "\n")
