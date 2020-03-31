print('#+'*10, '\033[4;35mSOMA DE MÚLTIPLOS\033[m', '+#'*10)
v = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c # outro jeito s = s + c
        v = v + 1
print(f'\033[30mA \033[4msoma\033[m \033[30mdos {v} valores \033[4mímpares e múltiplos\033[m '
      f'\033[30mde \033[4m3\033[m \033[30mentre \033[4m1\033[m \033[30me \033[4;30m500'
      f'\033[m \033[30mvale \033[4;36m{s}.')
