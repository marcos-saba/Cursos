import emoji
from time import sleep
print('#'*10, ' \033[1;4;33mCONTAGEM PARA OS FOGOS\033[m ', '#'*10)
for c in range(10, -1, -1):
    print(f'\033[30m{c}')
    sleep(1)
print(emoji.emojize('\033[1;31mBOOM!!!\033[33m :fireworks:'), emoji.emojize(':fireworks: '*2))


