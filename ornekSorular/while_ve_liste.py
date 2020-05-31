# Bu örnekte while ile listelerin üzerinden geçebilmenin bir yolunu görüryorsunuz.
#
i=0
fruits = ["elma", "armut", "kel", "mahmut"] #len(fruits) =>>> 4
while i < len(fruits):          #listenin uzunluğu kadar döndür:
    if fruits[i] == "kel":          #fruits[i] elemanı "kel"e eşitse:
        i = i+1                         #i'yi güncelle
        continue                        #5. satırdaki şarta dön ve kontrol et
    else:                           #değilse:
        print(fruits[i])                #fruits[i]'yi bastır
        i = i+1                         #i'yi güncelle
