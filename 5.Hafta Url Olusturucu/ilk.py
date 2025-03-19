str =["Emirhan KARABACAK", "Selimcan Turan"]
for sahis in str:
    sayac=0
    splitop=sahis.split(" ")
    for harf in splitop:

        print(harf)
        sayac+=1
    print(sayac)