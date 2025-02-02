def hesapmakine():
    while True:
           islem=input("İşlem seçin:\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\n5. Çıkış\nSeçiminiz: ")
           
           if islem== "5":
                print("Çıkış yapılıyor")
                break
           if islem not in ["1","2,","3","4","5"]:
                print("işlem yapılamaz")
                break
 
           sayi1 = float(input("Birinci sayıyı girin: "))
           sayi2 = float(input("İkinci sayıyı girin: "))

           if islem== "1":
                sonuc=sayi1+sayi2
           elif islem=="2":
                sonuc=sayi1-sayi2
           elif islem== "3":
                sonuc==sayi1*sayi2
           elif islem=="4":
                if sayi2==0:
                    print("İşlem yapılamaz")
                    continue
                sonuc= sayi1/sayi2
           
           else:
                print("işlem yapılamaz")


           if sonuc.is_integer():
                print(int(sonuc))
           else:
                print(float(sonuc))
            
hesapmakine()


