i=0
fruits = ["elma", "armut", "kel", "mahmut"] #len(fruits) =>>> 4
while i < len(fruits):
    if fruits[i] == "kel":
        i = i+1
        continue
    else:
        print(fruits[i])
        i = i+1
