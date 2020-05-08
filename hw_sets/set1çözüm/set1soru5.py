hp = int(input())
en = int(input())
dmg = int(input())
new_hp = hp - 3*dmg
moral = (new_hp*en)/10
print('[' + 'C'*(new_hp) + '-' * (10-new_hp) + ']')
print('[' + 'E'*en + '-' * (10-en) + ']')
print(moral)
