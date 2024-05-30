# N = int(input())

# for i in range(1, 101):
#     if i%N == 0 or str(N) in str(i):
#         print("Clap", end = "")
#     else:
#         print(i, end = "")
#     if i%10 == 0:
#         print()
#     else:
#         print(" ", end = "")

def clap_7(N):
    output = ""
    for i in range(1, 101):
        if i%N == 0 or str(N) in str(i):
            output += "Clap"
        else:
            output += str(i)
        output += " "
        if i%10 == 0:
            output += "\n"
        # else:
        #     output += " "
    return output

for i in range(2, 10):
    output = clap_7(i)
    output = output.rstrip("\n")
    with open(f"./outputs/clap_7/{i-1}.txt", "w") as f:
        f.write(output)





