# range method

# liste = [1,2,3]

# for item in liste:
#      print(item)

# for item in range(10):
#      print(item)

# for item in range(5,10):
#      print(item)

# for item in range(50,100,10):
#      print(item)

# print(list(range(50,100,20)))


# enumarate method

# greeting = "Hello There"

# for letter in greeting:
#      print(letter)

# enumarate kullanmadan:

# index = 0

# for letter in greeting:
#      print(f"index: {index} letter: {letter}")
#      index += 1
 
# for item in enumerate(greeting):
#      print(item)

# for index,letter in enumerate(greeting):
#      print(f"index: {index} letter: {letter}")


# zip method

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
     print(item)

for a,b,c in zip(list1, list2, list3):
     print(c)

for a,b,c in zip(list1, list2, list3):
     print(a,b,c)

