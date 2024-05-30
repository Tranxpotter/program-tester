import random

max_N = 100
max_M = 100

def generate_product():
    code = str(random.randint(1000000000000, 9999999999999))
    price = str(round(random.randint(1, 1000)/10, 1))
    return code, price
def generate_products(N:int):
    products = []
    output = ""
    for i in range(N):
        code, price = generate_product()
        products.append(code)
        output += f"{code} {price}\n"
        
    return products, output

def generate_buys(M:int, products:list):
    output = ""
    for i in range(M):
        choice = random.choice(products)
        output += f"{choice}\n"
    return output
    

def generate_test_case(N:int|None = None, M:int|None = None):
    if N is None:
        N = random.randint(1, max_N)
    products, products_input = generate_products(N)
    if M is None:
        M = random.randint(1, max_M)
    buys_input = generate_buys(M, products)
    
    return f"{N}\n{products_input}{M}\n{buys_input}"
    
def parkncome(inp:str):
    inp = inp.splitlines()
    N = int(inp[0])
    products = dict()
    for i in range(N):
        code, price = inp[i+1].split()
        products[code] = float(price)

    total = 0
    M = int(inp[N+1])
    for i in range(M):
        product = inp[N+2+i]
        total += products[product]
    return total

for i in range(10):
    if i == 0:
        input = generate_test_case(N=1, M=1)
    elif i < 9:
        input = generate_test_case(N=(i*10+1))
    else:
        input = generate_test_case(N=100, M=100)
    
    output = parkncome(input)
    with open(f"./inputs/parkncome/{i+1}.txt", "w") as f:
        f.write(input)
    
    with open(f"./outputs/parkncome/{i+1}.txt", "w") as f:
        f.write(str(output))