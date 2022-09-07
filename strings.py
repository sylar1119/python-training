name = "John Doe"
for c in name:
    print(c)

count = 0
for c in name:
    if c == "o":
        count +=1
print(count)

print(name[3])

# slicing

print(name[0:4])
print(len(name))

print("John" in "John Doe")

if "John" in name:
    print("Na ez is egy John")

#stringeknek vannak saját függvényeik
print(name.upper())

fruit = "           alma             "
print(fruit.strip())

print("john" in "Jake Jack John")
