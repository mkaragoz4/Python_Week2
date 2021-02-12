xcumle=input("Bir cumle yazin:")
cumle=xcumle.lower()
soz=dict()
noktalamalar=[', ', '?', ':', ';', ',', '.', '!', '/', ' ']
for x in range(len(cumle)):
    if cumle[x] not in noktalamalar:
        soz.update({cumle[x]:cumle.count(cumle[x])})
print(sorted(soz.items()))
input("Bitti.")
