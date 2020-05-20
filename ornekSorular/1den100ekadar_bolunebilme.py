#1'den 100'e kadar 7'ye bölünebilen sayıları bastıran program

i=1
while i < 100:          #100'e kadar iterasyon
    if i%7 == 0:            #Sayı 7'ye bölünebiliyorsa
        print(i)                #sayıyı bastır
        i = i+1                 #i'yi güncelle
    else:                   #Sayı 7'ye bölünemiyorsa
        i = i+1                 #i'yi güncelle
