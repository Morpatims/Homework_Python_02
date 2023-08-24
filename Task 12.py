sum_val = int(input('Enter the sum of numbers: '))
product_val = int(input('Enter the product of numbers: '))

for i in range(1, sum_val):
    j = sum_val - i
    if i * j == product_val:
        print(i, j)
        break
else:
    print('No such pair of numbers found.')