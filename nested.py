for i in range(3):
    for j in range(5, 8):
        print(f"{i} - {j}") 



# írjátok ki a 10x10 es szorzótáblát
for i in range(1, 11):
    for j in range(1, 11):
        prod=i * j
        print(f"{i} x {j} = {prod}")

# négyzetrácsos 10x10 szorzotábla

line = ""
for i in range(1, 11):
    line += str(i) + " "
print(line)

for i in range(1, 11):
    line = ""
    for j in range(1, 11):
        result = i * j
        if result < 10:
            line += " "
        line += str(result) + " "
    print(line)