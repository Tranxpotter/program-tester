def clap_7(N):
    output = ""
    for i in range(1, 101):
        if i%N == 0 or str(N) in str(i):
            output += "Clap"
        else:
            output += str(i)
        if i%10 == 0:
            output += "\n"
        else:
            output += " "
    return output

print(clap_7(int(input())))