klm=set(input("Bir kelime yazin:"))
klm2=set(input("Bir kelime daha yazin:"))


x=sorted(list(klm.intersection(klm2)))
x="".join(x)
y=sorted(list(klm.difference(klm2)))
y="".join(y)
z=sorted(list(klm2.difference(klm)))
z="".join(z)
sonuc=[x,y,z]
print(sonuc)
input("Bitti.")