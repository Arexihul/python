import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75,85])

result = numbers              # => [ 0  5 10 15 20 25 50 75 85]
result = numbers[5]           # => 25
result = numbers[-1]          # => 85
result = numbers[0:3]         # => [ 0  5 10]
result = numbers[:3]          # => [ 0  5 10]
result = numbers[3:]          # => [15 20 25 50 75 85]
result = numbers[::]          # => [ 0  5 10 15 20 25 50 75 85]
result = numbers[::-1]        # => [85 75 50 25 20 15 10  5  0]
result = numbers[::3]         # => [ 0 15 50]
result = numbers[::-2]        # => [85 50 20 10  0]

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers2             # => [[ 0  5 10]
                              #     [15 20 25]
                              #     [50 75 85]]
result = numbers2[0]          # => [ 0  5 10]
result = numbers2[2]          # => [50 75 85]
result = numbers2[0,2]        # => 10
result = numbers2[2,1]        # => 75
result = numbers2[:,2]        # => [10 25 85]
result = numbers2[:,0]        # => [ 0 15 50]
result = numbers2[:,0:2]      # => [[ 0  5]
                              #     [15 20]
                              #     [50 75]]
result = numbers2[-1,:]       # => [50 75 85]
result = numbers2[:2,:2]      # => [[ 0  5]
                              # =>  [15 20]]

print(result)


arr1 = np.arange(0,10)        # => [0 1 2 3 4 5 6 7 8 9]

# arr2 = arr1   # referans      # => arr2: [0 1 2 3 4 5 6 7 8 9]

# arr2[0] = 20

# print(arr1)                   # => [20  1  2  3  4  5  6  7  8  9]
# print(arr2)                   # => [20  1  2  3  4  5  6  7  8  9]

arr2 = arr1.copy()            # => arr2: [0 1 2 3 4 5 6 7 8 9]

arr2[0] = 20

print(arr1)                   # => [0 1 2 3 4 5 6 7 8 9]
print(arr2)                   # => [20  1  2  3  4  5  6  7  8  9]

