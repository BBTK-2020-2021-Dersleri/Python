#Created on Fri. Dec 11 20:57 2020
#@author: Aydın CESUR
hayvanlar = {"memeliler": [],"balıklar": [],"omurgasızlar": [],"sürüngenler":[],"kuşlar":[]}
while True:
    secim = int(input("1-) Yeni Hayvan Girin\n2-) Sözlükte Hayvan Ara\n3-) Sözlüğün Sıralı Çıktısını Al\n4-) Çıkış"))
    if secim == 1:
        turler = tuple(hayvanlar.keys())
        print("Hayvan Türü Seçiniz")
        for i in range(0,len(turler)):
            print("{} -) {}".format(i+1,turler[i]))
        tur = int(input())
        print(turler[tur-1])
        if tur > 5 or tur < 1:
            print("Yanlış Tür girdiniz\n")
        else:
            hayvan_ismi = input("Hayvan İsmi Giriniz:")
            if hayvan_ismi in hayvanlar[turler[tur-1]]:
                print("Hayvan zaten sözlükte ekli")
            else:
                hayvanlar[turler[tur - 1]] = hayvanlar[turler[tur - 1]] + [hayvan_ismi]
                print(hayvanlar)
    elif secim == 2:
        turler = tuple(hayvanlar.keys())
        print("Hayvan Türü Seçiniz")
        for i in range(0,len(turler)):
            print("{} -) {}".format(i+1,turler[i]))
        tur = int(input())
        print(turler[tur-1])
        if tur > 5 or tur < 1:
            print("Yanlış Tür girdiniz\n")
        else:
            hayvan_ismi = input("Hayvan İsmi Giriniz:")
            if hayvan_ismi in hayvanlar[turler[tur-1]]:
                print("Hayvan sözlükte mevcut")
            else:
                print("Hayvan sözlükte mevcut değil")
    elif secim == 3:
        turler = tuple(hayvanlar.keys())
        for tur in turler:
            print("{}: ".format(tur), end = " ")
            for hayvan in hayvanlar[tur]:
                print(hayvan,end = ",")
            print("\n")
    else:
        break