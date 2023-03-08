numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val1 = min(numbers)
val2 = max(numbers)
val3 = min(letters)
val4 = max(letters)

print(val1)
print(val2)
print(val3)
print(val4)

val5 = numbers[3:6]
val6 = numbers[:3]
val7 = numbers[4:]

print(val5)
print(val6)
print(val7)

numbers[4] = 40  
print("1 =>  ")
print(numbers)

numbers.append(49)
print("2 =>  ")
print(numbers)

numbers.insert(3, 78)
print("3 =>  ")
print(numbers)

numbers.insert(-1, 52)
print("4 =>  ")
print(numbers)

# numbers.pop()               # son elemanı siler
# numbers.pop(0)              # belirtilen indexte elemanı siler
# numbers.pop(-1)

# numbers.remove(49)          # aradığı elaemanı siler

print("5 =>  ")
# print(numbers)


numbers.sort()     # listeyi sıralar
numbers.reverse()     # listeyi tersine çevirir

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)

#  https://docs.python.org/3/tutorial/datastructures.html

