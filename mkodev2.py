print("Lutfen iki veya daha fazla elemandan olusan bir deger giriniz:")
while True:
    lstx=input()
    if len(lstx)>1:
        lst=list(lstx)
        print('\n',lst)

        n=int(input("\nListeyi saga kaydirmak icin pozitif, sola kaydirmak icin negatif bir sayi giriniz:"))
        yeni_liste=lst[-n:]+lst[:-n]
        print(yeni_liste)
        input()
        break

    else:
        print("""Hatali girdiniz.
Lutfen tekrar deneyin.\n""")
input("Bitti.")
