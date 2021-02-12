gecis=0
ss=1
sayi=int(input('Sayinizi giriniz:'))
lst=list(range(1,sayi+1))
print("\n",lst)
input("\nGecisleri gormek icin Enter'e basin:")
while True:
    del lst[ss::ss+1]
    if sayi==len(lst):
        break
    else:
        gecis+=1
        sayi=len(lst)
        ss+=1
        print("\n{}. gecis:".format(gecis),lst)
print("""
Sansli sayilar {}. gecis ile belirlendi.

Sansli sayilar:""".format(gecis),lst)
input("Bitti.")
