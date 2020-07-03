def deleteDuplicated(l = []):
    if type(l) != list:
        return []
    else:
        y = []
        i = 0
        while i<len(l):
            if l[i] not in y:
                y.append(l[i])
            i = i+1
        return y

liste = list(input())
print(deleteDuplicated(liste))







#bir eleman eğer y listenin içinde zaten varsa eklemicez yoksa eklicez
