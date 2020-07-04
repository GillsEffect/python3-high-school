#                     Programming with Python3
#                     Written by Mustafa Gilli
#                      github.com/GillsEffect
#
#                   IF/ELIF/ELSE KONU ANLATIM DOKÜMANI
#
# Dersimizin şimdiye kadarki bölümünde her koşulda çalışan kodlar yazdık. Hatasız yazılmış
# her kod satırımızın çalıştığını gördük. Peki sadece belli koşullarda çalışacak,
# o koşullar sağlanmadığında ise çalışmayacak kodları nasıl yazacağız?
#
# Bu noktada Python'ın <if>, <elif> ve <else> anahtar kelimelerini öğrenmemiz gerekiyor.
# Hızlı bir örnekle giriş yapalım:
print("-"*30)


print("Hoşgeldiniz")                                                 # 1. satır
yas = int(input("Yaşınızı girin:"))          #15                      # 2. satır
if yas < 21:                                                         # 3. satır
    print("Sokağa çıkmak için çok gençsiniz. Lütfen evde kalın.")    # 4. satır
print("Hoşçakalın")                                                  # 5. satır


print("-"*30)
# Yukarıdaki örnek kodda
# 1. satırda "Hoşgeldiniz" stringini ekrana bastırdık.
# 2. satırda input aldık ve <yas> adında bir değişkene atadık.
# 3. satırda <yas> değişkenini <if> sorgusunda kullandık. <yas> değişkenine atanan
# değer ile 21 sayısını karşılaştırdık. Örneğin yaşımız 16 olsun, yazmış olduğumuz
# "yas < 21" ifadesi boolean bir değer olan True anlamına gelecektir. Python <if>
# anahtar kelimesinin yanında True olarak değerlendirilmiş bir ifade gördüğünde
# <if> bloğuna giriş yapar ve o bloktaki kodların tamamını çalıştırır. Yani 4. satırdaki
# <print> komutu çalışır ve içine yazılan stringi ekrana bastırır. Daha sonra <if>
# bloğunun içinde başka komut olmadığı için ana bloktan çalışmaya devam ederek
# 5. satırdaki "Hoşçakalın" stringini bastırır.
#
# Burada dikkat edilmesi gereken en önemli durum; 1., 2. ve 5. satırdaki komutların hepsi
# kesinlikle çalışır ancak 4. satırdaki <print> SADECE VE SADECE <yas> değişkenine
# verilen değer 21'den küçük ise çalışır.
#
# Peki <yas> değişkenimizin 21'den küçük olduğu durumlar dışında ekrana bir string
# bastırmak isteseydik nasıl yapardık?
# Bu noktada <else> anahtar kelimesi hayatımıza giriyor. İnceleyelim:
print("Hoşgeldiniz")                                                            # 1. satır
yas = int(input("Yaşınızı girin:"))                                             # 2. satır
if yas < 21:                                                                    # 3. satır
    print("Sokağa çıkmak için çok gençsiniz. Lütfen evde kalın.")               # 4. satır
else:                                                                           # 5. satır
    print("Sokağa çıkabilirsiniz. Lütfen sadece gerektiğinde dışarı çıkın.")    # 6. satır
print("Hoşçakalın")                                                             # 7. satır


print("-"*30)
# <else> anahtar kelimesinin altında kalan bloktaki kodlar SADECE VE SADECE <yas>
# değişkeninin 21'E EŞİT VE 21'DEN BÜYÜK OLDUĞU DURUMLARDA çalışır. Örneğin yaşınız
# 25 ise 4. satır çalışmazken 6. satır çalışır ve verilen string ekrana bastırılır.
#
#
# Peki 65 yaşın üstündekiler için de bir mesajımız olsaydı nasıl iletirdik?
# Bu noktada ise <elif> anahtar kelimesini öğrenmeye ihtiyacımız var. <elif> anahtar kelimesi
# "else if" yani "değilse ve şöyleyse" ifadesi için bir kısaltmadır. Hemen örnekte
# ne işe yaradığını görelim:
print("Hoşgeldiniz")                                                            # 1. satır
yas = int(input("Yaşınızı girin:"))                                             # 2. satır
if yas < 21:                                                                    # 3. satır
    print("Sokağa çıkmak için çok gençsiniz. Lütfen evde kalın.")               # 4. satır
elif yas > 65:                                                                  # 5. satır
    print("Sokağa çıkmak için çok yaşlısınız. Lütfen evde kalın.")              # 6. satır
else:                                                                           # 7. satır
    print("Sokağa çıkabilirsiniz. Lütfen sadece gerektiğinde dışarı çıkın.")    # 8. satır
print("Hoşçakalın")                                                             # 9. satır


print("-"*30)

# Yukarıdaki örnekte Python <yas> değişkenini önce 21 ile karşılaştıracak, eğer 21'e
# eşit ya da 21'den büyükse 65 ile karşılaştıracak, eğer 65'e eşit ya da 65'ten küçükse
# <else> bloğundaki <print> komutunu çalıştıracaktır.
#
# Burada dikkat etmeniz gereken en önemli nokta IF/ELIF/ELSE bloklarından YALNIZCA BİRİ
# çalıştırılacaktır.
#
#
#                           CONDITIONAL EXPRESSIONS
# Bu başlık altında yukarıdaki '<' ve '>' ifadeleri gibi <if> sorgularında
# kullanabileceğimiz bazı karşılaştırma operatörlerini inceleyeceğiz.
#
# >=
# İki sayının birbirinden büyük ya da birbirine eşit olup olmadığını sorgular.
#
# <=
# İki sayının birbirinden küçük ya da birbirine eşit olup olmadığını sorgular.
#
# ==
# İki sayının birbirine eşit olup olmadığını sorgular. (Eşitse True döndürür.)
#
# !=
# İki sayının birbirine eşit olup olmadığını sorgular. (Eşitse False döndürür.)
#
# and "ve"
# Bu anahtar kelime SADECE VE SADECE soluna ve sağına yazılan statement'ların
# ikisi birden True ise True döner. Örneğin:

print(10>20 and 40>50) # False and False -> False
print(10<20 and 40>50) # True and False -> False
print(10>20 and 40<50) # False and True -> False
print(10<20 and 40<50) # True and True -> True


print("-"*30)

# or "veya"
# Bu anahtar kelime SADECE VE SADECE soluna ve sağına yazılan statement'ların
# ikisi birden False ise False döner.Örneğin:

print(10>20 or 40>50) # False and False -> False
print(10<20 or 40>50) # True and False -> True
print(10>20 or 40<50) # False and True -> True
print(10<20 or 40<50) # True and True -> True


print("-"*30)
