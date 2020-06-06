sistem = []                #sistem için bir liste oluştur.
while True:                #bilinmeyen sayıda input almak için sonsuz döngü kur.
    oyuncu = input()       #input al.
    if oyuncu == "0":      #input sıfıra eşitse:
        break                   #döngüyü kır.
    else:                  #değilse:
        sistem.append(oyuncu)   #oyuncuyu ekle.
print("Toplam", len(sistem), "oyuncu sisteme başarıyla kaydedildi.") #toplam oyuncu
#                  -----4. soru ile farklı olan kısım-----
cevap = input("Tüm oyuncular sistemden silinip takımdan atılsın mı?")

if cevap != "Y":                        #eğer cevap "Y" DEĞİL ise:
    pass                                    #hiçbir şey yapma.
else:                                   #eğer cevap "Y" ise: (bütün oyuncular listeden çıkarılmalı.)
    k = 0
    sistemLen = len(sistem)
    while k<sistemLen:      #oyuncuları listeden çıkarmak için gereken döngü:
        print(sistem.pop(), "takımdan atıldı.")
        k = k+1
