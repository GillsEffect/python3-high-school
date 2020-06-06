sistem = []                #sistem için bir liste oluştur.
while True:                #bilinmeyen sayıda input almak için sonsuz döngü kur.
    oyuncu = input()            #input al.
    if oyuncu == "0":           #input sıfıra eşitse:
        break                       #döngüyü kır.
    else:                       #değilse:
        sistem.append(oyuncu)       #oyuncuyu ekle.
print("Toplam", len(sistem), "oyuncu sisteme başarıyla kaydedildi.") #toplam oyuncu


# SORU#4:(TransferGo v2.0)
# Üçüncü sorudaki programı teslim ettiniz ve yönetim kurulu üyeleri programınızı
# çok beğendi. Ancak kaydedilecek oyuncu sayısını girerek kendilerini kısıtlamak
# istemiyorlar. Sizden istedikleri aynı şekilde transferleri kaydetmek ancak bu sefer
# programa "0" girene kadar oyuncuların hepsini kaydetmek, "0" değeri girildikten
# sonra ise programın sonlanmasını istiyorlar. Aynı zamanda kaç oyuncuyu sisteme
# kaydettiklerini de onay mesajında görmek istiyorlar.
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
#
# OUTPUT#1:
# Toplam 8 oyuncu sisteme başarıyla kaydedildi.
#
# INPUT#2:
# Ethan Hawke
# Elijah Wood
# Ian McKellen
# 0
#
# OUTPUT#2:
# Toplam 3 oyuncu sisteme başarıyla kaydedildi.
#
#
# İPUCU: Döngüler ve koşullu durumları kullanmanız gereken güzel bir örnek.
# Her iterasyonda önce input alan sonsuz bir döngüye (infinite loop) ihtiyacınız
# var. Programınız bu döngüden ancak input olarak "0" girildiğinde çıkmalı. <while>
# döngüsüne, <if,else> yapısına, <input> fonksiyonuna, döngüyü kırmak için <break>
# anahtar kelimesine ve toplam oyuncu için len() fonksiyonuna ihtiyacınız olacak.
