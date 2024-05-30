def calculator(input_str:str):
    nodes = input_str.split()
    
    #Calculate all * /
    new_nodes = []
    index = 1
    while index < len(nodes):
        operator = nodes[index]
        num1, num2 = float(nodes[index-1]), float(nodes[index+1])
        end_of_nodes = False
        while operator == "*" or operator == "/":
            if operator == "*":
                num1 *= num2
            elif operator == "/":
                num1 /= num2
                
            if index + 2 >= len(nodes):
                end_of_nodes = True
                break
            index += 2
            operator = nodes[index]
            num2 = float(nodes[index+1])
        if end_of_nodes:
            new_nodes += [num1]
        else:
            new_nodes += [num1, operator]
            if index + 2 >= len(nodes):
                new_nodes += [num2]
        index += 2
    
    #Calculate + -
    total = 0
    operator = "+"
    for node in new_nodes:
        if node == "+" or node == "-":
            operator = node
        elif operator == "+":
            total += float(node)
        elif operator == "-":
            total -= float(node)
    return total
    


print(calculator(input()))