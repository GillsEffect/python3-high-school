#                     Programming with Python3
#                     Written by Mustafa Gilli
#                      github.com/GillsEffect
#
#                    WHILE KONU ANLATIM DOKÜMANI
# Programlamada bazen ihtiyacımız olan bir satırı defalarca kez çalıştırmamız
# gerekebilir. Örneğin 0'dan 15'e kadar sayıları alt alta bastırmayı deneyelim.
#
# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# print(11)
# print(12)
# print(13)
# print(14)
#
# 15 satır alt alta print yazmanın ne kadar can sıkıcı olduğunu daha yazarken fark
# edebilirsiniz. İşte bunun gibi aynı satır veya satırlar bütününü
# birden fazla kez çalıştırmak istediğimizde döngüler(loops) konusu hayatımıza girer.
# Python3'te bir döngü oluşturmamız için gereken 2 anahtar kelime vardır: <while> ve <for>.
#
# Bu dokümanda while konusunu göreceğiz.
#
# Üstteki örneği while ile inceleyelim.

print('-'*15)#ayraç print'i

i = 0               #index variable
while i<15:         #i 15'ten küçük olduğu sürece:
    print(i)            #i'yi bastır.
    i = i+1             #i'yi arttır.
print("Döngü sonu")

print('-'*15)#ayraç print'i

# Yukarıdaki 5 satır kod çalıştığında 0'dan 15'e kadar (15 dahil değil) bütün sayıları
# alt alta bastırır.
#
# Peki nasıl?
# While komutu gövdesine(body) yazılan satırların hepsini yanına yazılan
# şart(condition) True olduğu sürece tekrar tekrar çalıştırır.
#
# Peki while gövdesi neresidir ve bunu ne belirler?
# 38 ve 39. satırlara bakın. Bu 2 satırın diğer iki satırdan 1 TAB mesafesi kadar
# içeride yazılmış olduğunu görüyoruz. İşte While satırının altında 1 TAB mesafesi
# içeride yazılmış her satır while'ın gövdesine dahildir. Python'da buna INDENTATION denir.
# If/elif/else konusunda da gördüğümüz gibi body'leri belirlemede kullanılır.
#
# Indentation bir syntax(yazım ve imla) kuralıdır. Bu kurala dikkat etmediğiniz sürece
# KESİNLİKLE VE KESİNLİKLE %99 ihtimalle hata alırsınız, %1 ihtimalle ise kodunuz
# çalışır ama beklediğiniz gibi bir sonuç vermez. Bu yüzden bu syntax kuralına dikkat
# edeceğiz.
#
# Çalışmalarınızda indentation ile alakalı bir hata yaparsanız kodunuzun IndentationError
# adında özel bi error verdiğini görürsünüz. Bu noktada geri dönüp kontrol etmeniz gerekir.
#
# Bir diğer syntax kuralı ise iki noktadır. while yazarak başladığınız bir satır
# KESİNLİKLE VE KESİNLİKLE iki nokta(:) ile bitmelidir. Yani şart'ı yazdıktan sonra
# iki nokta koymazsanız kodunuz SyntaxError alır.
#
# Peki şart(condition) nedir?
# Şartlar True ya da False dönen ifadelerdir. While ile kullanıldığında True olması
# body'deki kodların çalıştırılacağını gösterir. Body'ye dahil olan son satır da
# çalıştırıldıktan sonra Python geri döner ve şart'ı tekrar kontrol eder. Eğer şart
# hala True dönüyorsa body tekrar çalışır, False dönüyorsa body'nin bittiği yerin
# alt satırında kalan kodlar çalışmaya devam eder.
#
# Yukarıdaki örnekte döngüyü 15 kez tekrar etmemize yarayan ve döngünün en önemli
# elemanı olan index variable'ı görüyorsunuz. Genelde i ile isimlendirilir.
# i'yi 0'a eşitledik ve 15 olana kadar i'yi bastır dedik. Ancak bir işlem daha var.
# DÖNGÜ SONUNDA i'Yİ ARTTIRMAK. index variable'ı bastırma işlemi bittikten sonra
# arttırarak bi sonraki adıma hazırlanırız. İlk adımda 0<15 şart'ı True döndüğü için
# body çalışırken, ikinci adımda 1<15 şartı True döndüğü için çalışır. 3.de 2<15,
# 4.de 3<15 ... diye devam eder. Son olarak i 14'e eşitken yani 14<15 şartında body
# çalışır ve içinde i arttırılır. Bu da bi sonraki adımda 15<15 in False dönmesine
# yol açar ve bu durum döngüyü sonlandırır. Body dışında kalan ilk koddan (40. satır)
# başlayarak kodunuz çalışmaya devam eder.
#
# Döngüler listeler ile birlikte de kullanılabilir. Bir listenin elemanları ile bir
# iş yapmak istediğimizde listenin eleman sayısı kadar döngüyü döndürürüz. Örneğin:

print('-'*10)#ayraç print'i

liste = ["bugün", "güzel", "bir", "gün", "öyle", "değil", "mi?"]    #listemiz
print("Başlangıçtaki liste:", liste)        #listeyi bastır
i = 0                                       #index var.
while i<len(liste):                         #i listenin uzunluğundan(4) küçük olduğu sürece:
    liste[i] = liste[i] + " :)"                 #listenin mevcut elemanını güncelle.
    i = i+1                                     #i'yi arttır.
print("Yeni liste:", liste)                 #yeni listeyi bastır

print('-'*10)#ayraç print'i

# Yukarıdaki döngü liste'nin elemanlarını tek tek değiştirerek sonuna " :)" stringini
# eklememizi sağlıyor.96. satırdaki işlemin string concatenation olduğunu, iki stringi
# toplayarak çalıştığımızı önceki derslerimizden hatırlayın. len() fonksiyonu içine
# argüman olarak verilen string ya da listenin eleman sayısını döndürür. Döngü şartında
# biz de bundan yararlandık. Her adımda i'yi listenin uzunluğu(4) ile karşılaştırdık
# ve listenin sonuna gelene kadar her eleman için body'yi bir kez çalıştırdık.
# Body içinde ise liste'nin elemanlarına ulaşmak için i'yi kullanarak indexleme yaptık
# (liste[0], liste[1], liste[2] ve liste[3] gibi).
#
#                       WHILE İLE BİRDEN FAZLA INPUT ALMA
# Bazen fazla sayıda input almaya ihtiyacımız olur. Bu durumlarda da while kullanabiliriz.
# 3 durumda inceleyelim.
#
# ÖNCEDEN BİLDİĞİNİZ SAYIDA INPUT ALMA
#
# Örneğin 8 adet input almak istedinizi varsayalım. Mesela bu whatsapp grubunuzdaki
# arkadaşlarınızın isimleri olabilir.

print("-"*10)

i=0
while i<8:
    isim = input("Bir isim girin:")
    i = i+1

print("-"*10)

# Örnekteki kodu çalıştırdığınızda döngü 8 kez çalışacak ve 8 adet input girebileceksiniz.
# Peki program çalışmadan önce kaç input alacağınızı bilmiyorsunuz diyelim. (Yani kullanıcı
# kaç input gireceğine kendisi karar vermek istiyor.)
#
# VERİLEN SAYI KADAR INPUT ALMA

print("-"*10)

i=0                                         #index var.
number = int(input("Bir sayı girin"))       #input sayısını belirlemek için istenen integer
while i<number:                             #i number'dan küçük olduğu sürece:
    isim = input("Bir isim girin")              #input al ve isim'e ata.
    i = i+1                                     #i'yi arttır.

print("-"*10)

# Örnekteki kodu çalıştırdığınızda ilk girilen input, kaç tane isim inputu almak
# istediğinizi belirler. 10 yazarsanız programın devamında 10, 100 yazarsanız programın
# devamında 100 input girebilirsiniz.
#
# BELİRSİZ SAYIDA INPUT ALMA
# Bazen kaç input almanız gerektiğini asla bilemeyip istediğiniz herhangi
# bir anda o an input vermeyi bitirmek isteyebilirsiniz. Bu durumda aşağıdaki örnekteki
# gibi bir çözüm uygulamanız gerekir. Döngüyü kaç kez tekrar edeceğimizi bilmediğimiz
# için şart yerine True vererek sonsuz bir döngü oluştururuz. Ancak bu sonsuz döngüden
# eninde sonunda çıkmalıyız ki programımız takılı kalmasın. Bunun için bir durdurma
# karakteri belirleriz(Örnekte bu karakter "0" stringi).Klavyeden o karakter
# girildiğinde break komutu ile döngüyü kırarak input alma işlemini sonlandırırız.
# Belirlediğimiz durdurma karakeri girilmediği sürece input girebileceğimizi unutmayalım.
# (index variable'a da ihtiyacımız olmadığına dikkat edin.)
print("-"*10)

while True:             #Sonsuz kere döndür:
    isim = input()          #input al ve isim'e ata.
    if isim == "0":         #eğer aldığımız input "0"a eşitse:
        break                   #döngüyü kır.(input almayı sonlandır.)
