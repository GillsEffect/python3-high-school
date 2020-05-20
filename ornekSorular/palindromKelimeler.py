#Girilen kelimenin palindrom olup olmadığını kontrol eden program.

kelime = input("Bir kelime girin:")

if kelime == kelime[::-1]:
    print(kelime, " palindrom bir kelimedir.")
else:
    print(kelime, " palindrom bir kelime değildir.")
