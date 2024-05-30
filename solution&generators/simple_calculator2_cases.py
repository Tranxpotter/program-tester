

def calculator(input_str:str):
    nodes = input_str.split()
    index = 0
    prev_node_indexes = [-1] + [i-1 for i in range(1, len(nodes))]
    
    check_prev = False
    while index < len(nodes)-2:
        first_num = float(nodes[index])
        index += 1
        operator = nodes[index]
        index += 1
        second_num = float(nodes[index])
        
        if operator == "*":
            nodes[index] = first_num * second_num
        elif operator == "/":
            nodes[index] = first_num / second_num
        elif not index < len(nodes)-2:
            if operator == "+":
                nodes[index] = first_num + second_num
            elif operator == "-":
                nodes[index] = first_num - second_num
        
        else:
            next_operator = nodes[index+1]
            if next_operator == "*" or next_operator == "/":
                check_prev = True
                continue
            else:
                if operator == "+":
                    nodes[index] = first_num + second_num
                elif operator == "-":
                    nodes[index] = first_num - second_num
        
        if check_prev:
            condition = True
            prev_node_indexes[index] = prev_node_indexes[index-2]
            if index < len(nodes)-2:
                next_operator = nodes[index+1]
                condition = next_operator == "+" or next_operator == "-"
            if condition:
                prev_operator = nodes[prev_node_indexes[index]]
                prev_num = float(nodes[prev_node_indexes[index]-1])
                if prev_operator == "+":
                    nodes[index] = prev_num + float(nodes[index])
                else:
                    nodes[index] = prev_num - float(nodes[index])
                check_prev = False
    
    return nodes[-1]

case_num = 1

import random
max_N = 1000000
def generate_test_case(N, max_num):
    output = ""
    node_index = 1
    while len(output) < N:
        if node_index % 2 == 0:
            output += random.choice(["+", "-", "*", "/"])
            output += " "
        else:
            output += str(random.randint(1, max_num))
            output += " "
        node_index += 1
    if node_index % 2 == 0:
        output = output[:N]
    else:
        output = output[:len(output)-2]
    return output + "\n"


for i in range(5):
    case = generate_test_case(max_N // random.randint(2, 10) + random.randint(100000, 500000), 99999)
    output = str(calculator(case))
    with open(f"inputs/simple_calculator2/{case_num}.txt", "w") as f:
        f.write(case)
    with open(f"outputs/simple_calculator2/{case_num}.txt", "w") as f:
        f.write(output)
    case_num += 1
    
for i in range(5):
    case = generate_test_case(max_N // random.randint(2, 10) + random.randint(1000, 5000), 99)
    output = str(calculator(case))
    with open(f"inputs/simple_calculator2/{case_num}.txt", "w") as f:
        f.write(case)
    with open(f"outputs/simple_calculator2/{case_num}.txt", "w") as f:
        f.write(output)
    case_num += 1