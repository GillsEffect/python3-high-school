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

# SORU#5:(TransferGo 'unnecessary version')
# Yönetim kurulu TransferGo'yu geliştirmeye devam ediyor. Bu sefer v2.0'ın üstüne
# öyle bir özellik eklemek istiyorlar ki nedenini anlayamıyorsunuz ama yine de
# istediklerini yapmak zorundasınız. Başlangıçta her şey v2.0'daki ile aynı olacak.
# Klavyeden "0" girilene kadar oyuncu kaydedeceksiniz ve "0" girildikten sonra toplam
# kaydedilen oyuncu sayısını yazdıracaksınız. İşte bu noktada yeni özellik geliyor:
# kullanıcıdan bir input alarak bütün oyuncuları sistemden silme ve takımdan atma
# izni isteyeceksiniz. Eğer input "Y" ise bütün oyuncuları sistemden silip onay
# mesajı vereceksiniz, "N" ise herkesi sisteme kayıtlı bırakıp onay mesajı vereceksiniz.
# Fakat burada dikkat etmeniz gereken bir nokta var: son eklenen oyuncu ilk atılan
# oyuncu olacak, ilk eklenen oyuncu ise son atılan oyuncu olacak.
#
#
#
# INPUT#1:
# Edgar Wright
# Bernardo Bertolucci
# Steven Spielberg
# Quentin Tarantino
# Christopher Nolan
# Marlon Brando
# Tom Hanks
# Keanu Reeves
# 0
# Tüm oyuncular sistemden silinip takımdan atılsın mı? Y
#
# OUTPUT#1:
# Edgar Wright sisteme kaydedildi.
# Bernardo Bertolucci sisteme kaydedildi.
# Steven Spielberg sisteme kaydedildi.
# Quentin Tarantino sisteme kaydedildi.
# Christopher Nolan sisteme kaydedildi.
# Marlon Brando sisteme kaydedildi.
# Tom Hanks sisteme kaydedildi.
# Keanu Reeves sisteme kaydedildi.
# Toplam 8 oyuncu sisteme başarıyla kaydedildi.
# Keanu Reeves takımdan atıldı.
# Tom Hanks takımdan atıldı.
# Marlon Brando takımdan atıldı.
# Christopher Nolan takımdan atıldı.
# Quentin Tarantino takımdan atıldı.
# Steven Spielberg takımdan atıldı.
# Bernardo Bertolucci takımdan atıldı.
# Edgar Wright takımdan atıldı.
#
# INPUT#2:
# Ethan Hawke
# Elijah Wood
# Ian McKellen
# 0
# Tüm oyuncular sistemden silinip takımdan atılsın mı? Y
#
# OUTPUT#2:
# Ethan Hawke sisteme kaydedildi.
# Elijah Wood sisteme kaydedildi.
# Ian McKellen sisteme kaydedildi.
# Toplam 3 oyuncu sisteme başarıyla kaydedildi.
# Ian McKellen takımdan atıldı.
# Elijah Wood takımdan atıldı.
# Ethan Hawke takımdan atıldı.
#
#
# INPUT#3:
# Ethan Hawke
# Elijah Wood
# Ian McKellen
# 0
# Tüm oyuncular sistemden silinip takımdan atılsın mı? N
#
# OUTPUT#3:
# Ethan Hawke sisteme kaydedildi.
# Elijah Wood sisteme kaydedildi.
# Ian McKellen sisteme kaydedildi.
# Toplam 3 oyuncu sisteme başarıyla kaydedildi.
#
# İPUCU: Başlangıçta karmaşık gelebilir. Ancak adım adım ilerlediğinizde çözüm çorap
# söküğü gibi gelecektir, sadece sabırlı olun. Bu örnekte <.append> ve <.pop
# methodlarının ikisine birden ihtiyacınız olacak.
#
