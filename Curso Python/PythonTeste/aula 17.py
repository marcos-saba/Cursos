num = [2, 5, 9, 1]
num[2] = 3
num.append(4)
num.sort(reverse=True)
num.insert(2, 0)
#num.remove()
if 5 in num:
    num.remove(5)
else:
    print('Not found')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
