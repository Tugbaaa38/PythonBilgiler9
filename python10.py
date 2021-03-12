
#KUME(set)
#kume birden cok veri tipini bir arada bulundurabilir.(sozluk,liste,demet(sonra bakacagiz))
#Birlestirme,kesisim gibi islevleri bu veri tipi ile yapabiliriz.
#aynı olan elemanlari tek bir eleman olarak alir.
#kumeler de degistirilebilen veri turudur.

deneme={"Bilgisayar","Yazilim",1,5,7,7,5,4,9,8,8,"Yazilim"}
print(deneme)  #ciktisi:{1, 4, 5, 'Bilgisayar', 7, 8, 9, 'Yazilim'} 
#goruldugu gibi ayni olan elemanlar tek elemanmis gibi alindi..

tur=set()                              
print(type(tur))

kontrol=5 in deneme
print(kontrol) #true veya false donecek.
print(len(deneme ))
deneme.add("Tugba")    
deneme.add(14)
print(deneme)
deneme.remove("Tugba")   #burada istedigimiz elemani silebiliriz..
print(deneme)

#kume= set(["Yazilim" , "Donanim" , "Yapay" ,"Zeka"])   bu sekilde de tanimlayabiliriz.
kume={"Yazilim" , "Donanim" , "Yapay" ,"Zeka"}
eklenecek = ["Oyun" , "Mobil" , "Guvenlik" , "Egitmen","Zeka"]  #Zeka zaten var bu yuzden tekrar yazdirmaz.

#for i in eklenecek:               
# kume.add(i)
#print(kume)

#eklerken for yerine update metodunu da kullanabiliriz.
kume.update(eklenecek)
print(kume)

#difference metoduna bakacak olursak iki kume arasindaki farki bize verecektir.

kume1= {"Ali","Taner","veysel"}        #set(["Ali" , "Taner", "Veysel"])
kume2= {"Ali","Taner","Masal","Eylul"}  #set(["Ali" , "Taner" , "Masal" , "Eylul"])
print(kume1.difference(kume2))    #kume 1 in kume 2 'den farklarını yazdır.
print(kume2.difference(kume1))    #kume 2'nin kume 1'den farkını yazir.

#Fark bulma islemini soyle daha kolay yapabiliriz.
print(kume1-kume2)    
print(kume2-kume1)

#Kesisim nasil buluruz?
kume1= {"Ali","Taner","veysel"}        
kume2= {"Ali","Taner","Masal","Eylul"}  
print(kume1.intersection(kume2))  #intersection ise bize kesisimi verir. [Ali,Taner]

#Kesisim isleminin kisa yolu nedir?
print(kume1 & kume2)  #Bu da bize Ali ve Taneri verecektir.

#union ise kumelerin birlesimini alir.
print(kume1.union(kume2))

#DEMET(Tuple)
#demetler de birden fazla veri turunu bir arada bulundurabilirler.
#ekleme-cikarma gibi islemler yapilamaz..(Degistirilemeyen veri tipi)

tup1=(2,4,6,8,10)
print(tup1)
print(type(tup1))

print(tup1[-3])  #bize 6 ciktisini verecektir.
print(tup1[::2])

karisik=("Tugba",3,"Kirac",5,8,3)
print(karisik.index("Tugba")) 
print(karisik.count(3))

karisik[0]="Eylul"  #Boyle bir guncelleme yapamayiz..

