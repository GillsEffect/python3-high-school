#Listedeki kelimeleri tek tek kontol eden ve palindrom olup olmadıklarını
#yazdıran program.

list = ["küçük", "büyük", "kelime", "enine", "eğri", "ebe"]
i=0
while i < len(list):                #listenin eleman sayısı kadar iterasyon
    if list[i] == list[i][::-1]:        #kelime tersten okunuşuna eşitse
        print(list[i])                     #kelimeyi bastır
        i = i+1                            #i'yi güncelle
    else:                               #kelime tersten okunuşuna eşit değilse
        i = i+1                            #i'yi güncelle 
