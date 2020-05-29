hp = int(input())  # 9
en = int(input())  # 9
moral = (hp*en)/10.0 # 8.1
print('[' + 'C'*hp + '-' * (10-hp) + ']')
print('[' + 'E'*en + '-' * (10-en) + ']')
print(moral)
