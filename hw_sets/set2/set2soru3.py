sistem = []                                     #sistem için bir liste oluştur.
number = int(input())                           #kaç oyuncu alınacağını öğren.
i = 0                                           #while için index variable.
while i<number:                                 #girilecek oyuncu sayısı kadar döndür:
    oyuncu = input()                                #kullanıcıdan oyuncuyu al.
    sistem.append(oyuncu)                           #sistem adlı listeye ekle.
    i = i+1                                         #i'yi güncelle.
j=0                                         #onay mesajları için gereken while'ın index var..
while j<len(sistem):                        #sistem listesinin uzunluğu kadar döndür:
    print(sistem[j], "sisteme kaydedildi.")     #onay mesajı
    j = j+1                                     #j'yi güncelle.


# SORU#3:(TransferGo v1.1)
# İkinci sorudaki programı teslim ettiniz ve yönetim kurulu üyeleri programınızı
# çok beğendi. Ancak isteklerini tam olarak anlatamadıkları için sizden yeni
# isteklerine göre benzer ama yeni bir program yazmanızı istiyorlar. Yeni program da
# sisteme oyuncuları kaydedecek ancak önceki gibi her seferinde sadece 1
# oyuncu değil. Kullanıcıdan alınacak integer değeri kadar oyuncuyu sisteme girmeli.
# Yani önce kaç transfer olacağı girilecek daha sonra o transferler tek tek sisteme
# eklenecek.
#
# INPUT#1:
# 3
# Marlon Brando
# Tom Hanks
# Keanu Reeves
#
# OUTPUT#1:
# Marlon Brando sisteme kaydedildi.
# Tom Hanks sisteme kaydedildi.
# Keanu Reeves sisteme kaydedildi.
#
#
# INPUT#2:
# 5
# Edgar Wright
# Bernardo Bertolucci
# Steven Spielberg
# Quentin Tarantino
# Christopher Nolan
#
# OUTPUT#2:
# Edgar Wright sisteme kaydedildi.
# Bernardo Bertolucci sisteme kaydedildi.
# Steven Spielberg sisteme kaydedildi.
# Quentin Tarantino sisteme kaydedildi.
# Christopher Nolan sisteme kaydedildi.
#
# INPUT#3:
# 0
# OUTPUT#3:
# <Program hiçbir şey bastırmadan sonlanır.>
#
# İPUCU: Döngüler(loops) bilgilerinizi kullanmanız gereken güzel bi örnek. v1.0'daki
# gibi bir liste methodu kullanacaksınız ancak bu sefer işin içine <while> da girdi.
# Önce integer değerini alın ve döngülerinizi o değer kadar döndürün. İnputları almak
# için bir döngüye, onay mesajları için başka bir döngüye ihtiyacınız var. <while>
# kullandığınızı unutmayın. İki nokta ve TAB bırakma gibi syntax kurallarına dikkat edin.
