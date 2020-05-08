#           Programming with Python3 - Exercise set #1
#                    Written by Mustafa Gilli
#                     github.com/GillsEffect
#
#
#
#  Bir oyun programcısı olduğunuzu hayal edin. Sizden geliştirdiğiniz
#  karakterin can ve enerji seviyelerini hesaplamanız ve bunları ekrana
#  alt alta bastırmanız isteniyor.
#
#  -----------------------------------------------------------------------------
#  Soru 1:
#  Karakteriniz henüz hiç savaşa girmediğini düşünün.  Bu yüzden can ve enerji
#  seviyesi şu an 10 birim. Ekrana her 1 birim Can için "C", her 1 birim Eneji
#  için "E" karakteri bastıran bir program yazın.
#
#  Programınızı çıkarması gereken OUTPUT:
#  CCCCCCCCCC
#  EEEEEEEEEE
#
#  İPUCU: 2 tane print fonksiyonu kullanmanız yeterli. Stringlerin integerlar ile
#  çarpılabildiğini hatırlayın. Örneğin print("ali" * 2) komutu size 'aliali'
#  stringini verir.
#
#  -----------------------------------------------------------------------------
#  Soru 2.1:
#  Karakteriniz yolda bir golemin saldırısına uğradı. Karakterinizin aldığı
#  hasar can değerinizi 6'ya, bu savaşta kullandığı beceriler ise enerji
#  seviyenizi 5'e düşürdü. Ancak bu sefer eksik her 1 Can ve Enerji seviyesi
#  için "-" karakteri bastırdığınız bir program yazın.
#
#  OUTPUT:
#  CCCCCC----
#  EEEEE-----
#
#
#
#  Soru 2.2:
#  Can ve Enerji barlarınızın başına ve sonuna köşeli parantezler ekleyin.
#
#  OUTPUT:
#  [CCCCCC----]
#  [EEEEE-----]
#
#  İPUCU: iki veya daha fazla stringin toplanabildiğini hatırlayın. Örneğin
#  print("ahmet" + " " + "haşim") size 'ahmet haşim' stringini verir.
#  -----------------------------------------------------------------------------
#  Soru 3:
#  Karakteriniz karşısına çıkan ilk handa yemek yedi ve iyice dinlendi. Şu an
#  Can ve Enerji seviyesi full ve 10. Bu noktadan sonra karakterinizin Moral
#  seviyesini de <float> cinsinden bastırmanız bekleniyor.
#
#  Moral seviyesi formülü: (Can*Enerji)/10
#
#  OUTPUT:
#  [CCCCCCCCCC]
#  [EEEEEEEEEE]
#  10.0
#
#  İPUCU: 10 ve 10.0'ın farklı değerler olduğunu hatırlayın.
#  -----------------------------------------------------------------------------
#  Soru 4:
#  Şimdi de karakterinizin herhangi bir andaki Can ve Enerji seviyelerinin
#  görülebilmesi için Can ve Enerji inputları alan daha sonra bu inputlara göre
#  Can, Enerji ve Moral outputlarını veren bir program yazın.
#
#  INPUT#1:
#  5
#  3
#  OUTPUT#1:
#  [CCCCC-----]
#  [EEE-------]
#  1.5
#
#  INPUT#2:
#  9
#  9
#  OUTPUT#2:
#  [CCCCCCCCC-]
#  [EEEEEEEEE-]
#  8.1
#
#  İPUCU: Programa input alabilmek için derste öğrendiğimiz input() fonksiyonunu
#  kullanın. Aldığınız inputları bir değişkene atamanız gerektiğini unutmayın.
#  Can ve Enerji değişkenlerinizi kullanarak Moral seviyenizi hesaplayın.
#  Özetle 2 input(), 3 print() fonksiyonu kullanabilirsiniz. Can barında x kadar
#  'C' var iken, 10-x kadar '-' olduğunu da unutmayın.
#  -----------------------------------------------------------------------------
#  Soru 5:
#  Karakteriniz macerasının devamında 3 ork ile karşılaştı. Orkların her biri
#  bir kez vurdu ve karakterinizin canı bunun sonucunda azaldı. Karakterinizin
#  son Can, Enerji ve Moral seviyesini ekrana bastıran bir program yazın.
#
#  (Orkların güçleri eşit sayılacak ve tek bir input ile belirlenecek.)
#
#   INPUT#1:
#   10
#   10
#   2
#   OUTPUT#1:
#   [CCCC------]
#   [EEEEEEEEEE]
#   4.0
#
#   INPUT#2:
#   9
#   5
#   3
#   OUTPUT#2:
#   [-----------]
#   [EEEEE------]
#   0.0
#
#  -----------------------------------------------------------------------------
#  Çözümlerinizi ayrı ayrı python scriptlerine yazın. Her birinin başına
#  isminizi yorum satırı olarak ekleyin. Scriptleri
#
#  set1soru1.py
#  set1soru2.py
#  set1soru22.py
#  set1soru3.py
#  set1soru4.py
#  set1soru5.py
#
#  şeklinde isimlendirin. Soruları bir sonraki dersimizde hep beraber
#  inceleyip çözeceğiz. KOLAY GELSİN!
#  -----------------------------------------------------------------------------
