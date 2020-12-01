print("HESAP MAKINESI UYGULAMASINA HOSGELDİNİZ")
print("---------------------------------------")
print("Toplama islemi için-->1\nCikarma islemi icin-->2\nCarpma işlemi icin-->3\nBölme islemi icin-->4\nCikmak icin-->q")
while(True):
        secenek=input("Seceneginizi giriniz: ")
        if(secenek=='q'):
            print("Cikiliyor....")
            break
        else:
            
            first_number=float(input("Ilk sayinizi giriniz: "))
            second_number=float(input("Ikinci sayinizi giriniz: "))      
            if(secenek=='1'):
                print(first_number+second_number)
            elif(secenek=='2'):
                print(first_number-second_number)
            elif(secenek=='3'):
                print(first_number*second_number)
            elif(secenek=='4'):
                print(first_number/second_number)
            else:
                print("Gecersiz islem")