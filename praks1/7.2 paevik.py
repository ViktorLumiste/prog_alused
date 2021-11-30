from datetime import *

paevik = open("paevik.txt" , "a", encoding = "UTF-8")
kuupaev = datetime.today()
kirje = input("Sisesta sissekande teksti: ")
paevik.write("\n" + str(kuupaev) + "\n")
paevik.write(kirje + "\n")

paevik.close()