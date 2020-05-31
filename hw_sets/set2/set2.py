#                 Programming with Python3 - Exercise set #2
#                       Written by Mustafa Gilli
#                         github.com/GillsEffect
#
#                              TransferGo
# Bilgisayar mühendisliği terk bir teknik direktör olduğunuzu hayal edin.
# Takımınıza yapacağınız transferler için bir program(TransferGo) yazmanız isteniyor.
#
# Soru1:(TransferGo v0.1)
# Transfer ettiğiniz futbolcunun bilgilerini kaydeden, ve kayıt edildiğinde
# onaylayan bir program yazın. Futbolcunun; adını, soyadını, geldiği takımı,
# transfer bedelini, ayakkabı numarasını, mevkiisini kaydedin ve ekrana bastırın.
# (Programınızda listeleri kesinlikle kullanın. Bir liste oluşturun ve içine
# input değerlerini birer eleman olarak verin. Daha sonra liste elemanlarını
# print fonksiyonunu kullanarak outputtaki gibi alt alta bastırın.)
#
# INPUT#1:
# Mustafa Gilli
# Real Madrid
# 1000000 Euro
# 42.5
# Orta Saha
#
# OUTPUT#1:
# Transfer edilen futbolcunun:
# Adı: Mustafa Gilli
# Geldiği takım: Real Madrid
# Transfer bedeli: 1000000 Euro
# Ayakkabı Numarası: 42.5
# Mevkii: Orta Saha
# Transfer Onaylandı!
#
# INPUT#2:
# Duygu Özaslan
# Barcelona
# 1000000 TL
# 44
# Kaleci
#
# OUTPUT#2:
# Transfer edilen futbolcunun:
# Adı: Duygu Özaslan
# Geldiği takım: Barcelona
# Transfer bedeli: 1000000 TL
# Ayakkabı Numarası: 44
# Mevkii: Kaleci
# Transfer Onaylandı!

# İPUCU: Her iki input için de 5 elemanlı bir listeye,
# 7 tane print fonksiyonuna ihtiyacınız olacak.
#
#
#
# Soru#2:(TransferGo v1.0)
# Yönetim kurulu yeni transfer ettikleri bir oyuncunun ismini sisteme kendileri
# kaydetmek istiyor ve bu yüzden sizden bir program istiyor. İnput olarak bir isim
# alan daha sonra bu ismi bir listeye ekleyen ve onay mesajı veren bir program yazın.
# (Kesinlikle bir liste kullanmalısınız. Liste kullanılmayan çözümler geçerli değil.)
#
# INPUT#1:
# Scarlett Johansson
# OUTPUT#1:
# Scarlett Johansson sisteme kaydedildi.
#
# INPUT#2:
# Chris Hemsworth
# OUTPUT#2:
# Chris Hemsworth sisteme kaydedildi.
#
# İPUCU: Boş bir liste oluşturduktan sonra listeler üzerinde kullanılan
# <.append> ya da <.pop> methodlarındandan birine ihtiyacınız olacak.
# Hangisi olduğuna karar verin.
#
#
#
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
#
#
#
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
# Edgar Wright sisteme kaydedildi.
# Bernardo Bertolucci sisteme kaydedildi.
# Steven Spielberg sisteme kaydedildi.
# Quentin Tarantino sisteme kaydedildi.
# Christopher Nolan sisteme kaydedildi.
# Marlon Brando sisteme kaydedildi.
# Tom Hanks sisteme kaydedildi.
# Keanu Reeves sisteme kaydedildi.
# Toplam 8 oyuncu sisteme başarıyla kaydedildi.
#
# INPUT#2:
# Ethan Hawke
# Elijah Wood
# Ian McKellen
# 0
#
# OUTPUT#2:
# Ethan Hawke sisteme kaydedildi.
# Elijah Wood sisteme kaydedildi.
# Ian McKellen sisteme kaydedildi.
# Toplam 3 oyuncu sisteme başarıyla kaydedildi.
#
#
# İPUCU: Döngüler ve koşullu durumları kullanmanız gereken güzel bir örnek.
# Her iterasyonda önce input alan sonsuz bir döngüye (infinite loop) ihtiyacınız
# var. Programınız bu döngüden ancak input olarak "0" girildiğinde çıkmalı. <while>
# döngüsüne, <if,else> yapısına, <input> fonksiyonuna, döngüyü kırmak için <break>
# anahtar kelimesine ve toplam oyuncu için len() fonksiyonuna ihtiyacınız olacak.
#
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
# ------------------------------------------------------------------------------
# Cevaplarınızı https://www.onlinegdb.com/online_python_debugger sitesi üzerinden
# ya da Atom kullanarak yazın ve test edin. Her bir sorunun cevabını whatsapp üzerinden
# ayrı ayrı atın. Okunabilir fotoğraflar, Atom ile oluşturduğunuz python dosyaları
# ya da doğrudan mesaj şeklinde atabilirsiniz. Mesaj şeklinde atacaksanız bu üç karakteri
# kopyalayın:
# ```
# Mesajınızın başına ve sonuna yazdığınızda mesaj kod formatında atılacaktır.
# Yazdığınız kodu mesaj olarak atarken bu şekilde atmazsanız doğruluğunu kontrol edemem.
# Çözümler gelecek dersimizde yayınlanacak. BOL ŞANS.
# --------------------------------GÜNCELLEME------------------------------------
#
# 1. sorudaki inputlar için input fonksiyonu kullanmanıza gerek yok, sabit bir
# listeye elemanları vererek çalışabilirsiniz. İnput ile yapan arkadaşların
# değiştirmelerine gerek yok.
#
# Bilgisayarında python2.7 olan arkadaşlar bazı SyntaxError'lar alabilir. Beklenmedik
# syntax errorlar alırsanız özelden ulaşmanız halinde yardımcı olacağım.
