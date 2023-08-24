coin = int(input('Enter the number of coins: '))
from random import randint
Eagle_count = 0
Tails_count = 0
coin_flips = ""
for i in range(coin):
    temp = randint(0, 1)
    coin_flips += str(temp) + ' '
    if temp > 0:
        Eagle_count = Eagle_count + 1
    else:
        Tails_count = Tails_count + 1

print(coin_flips)

if Eagle_count > Tails_count:
    print(f'We need to flip, {Tails_count} coins')
else:
    print(f'We need to flip, {Eagle_count} coins')