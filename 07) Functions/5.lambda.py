def square(num): return num**2

print(square(2))

numbers = [1,3,5,9,10,6]

print(list(map(square, numbers)))

for item in map(square, numbers):
     print(item)

# fonksiyon oluşturmadan:

print(list(map(lambda x: x**2, numbers)))    # lambda expression

square2 = lambda x: x**2

print(list(map(square2, numbers)))
print(square2(4))

# filter işlemi

def check_even(number): return number%2==0

result = list(filter(check_even, numbers))
print(result)

result = list(filter(lambda number: number%2==0, numbers))
print(result)

checkEven = lambda number: number%2==0

result = list(filter(checkEven, numbers))
print(result)

print(check_even(numbers[2]))

