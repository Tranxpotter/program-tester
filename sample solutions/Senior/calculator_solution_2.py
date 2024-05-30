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

print(calculator(input()))