içiçedöngü = []

for x in range(3):
     for y in range(3):
          içiçedöngü.append((x,y))

print(içiçedöngü)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)