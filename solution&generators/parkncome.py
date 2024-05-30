N = int(input())
products = dict()
for i in range(N):
    code, price = input().split()
    products[code] = float(price)

total = 0
M = int(input())
for i in range(M):
    product = input()
    total += products[product]
print(total)
