import numpy as np

result = np.array([1,3,5,7,9])          # => [1 3 5 7 9]
result = np.arange(1,10)                # => [1 2 3 4 5 6 7 8 9]
result = np.arange(50,100,3)            # => [50 53 56 59 62 65 68 71 74 77 80 83 86 89 92 95 98]
result = np.zeros(10)                   # => [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result = np.ones(10)                    # => [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result = np.linspace(0,100,5)           # => [  0.  25.  50.  75. 100.]
result = np.linspace(0,5,5)             # => [0.   1.25 2.5  3.75 5.  ]
result = np.random.randint(0,10)        # => 6  => 0  => 7  => 3  => 9  => 4
result = np.random.randint(20)          # => 2  => 13  => 0  => 5  => 17  => 19
result = np.random.randint(1,10,3)      # => [6 1 4]
result = np.random.rand(5)              # => [0.81545071 0.26527088 0.868322   0.94466961 0.55221275]    # 0-1 arası 5 sayı
result = np.random.randn(5)             # => [-0.16364713 -1.49357841 -0.6005502   1.29099129  0.69963179]

print(result)

np_array = np.arange(50)                # => [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
                                        #     24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
                                        #     48 49]
np_multi = np_array.reshape(5,10)       # => [[ 0  1  2  3  4  5  6  7  8  9]
                                        #     [10 11 12 13 14 15 16 17 18 19]
                                        #     [20 21 22 23 24 25 26 27 28 29]
                                        #     [30 31 32 33 34 35 36 37 38 39]
                                        #     [40 41 42 43 44 45 46 47 48 49]]
print(np_multi.sum(axis=1))             # => [ 45 145 245 345 445]    # satırların toplamı
print(np_multi.sum(axis=0))             # => [100 105 110 115 120 125 130 135 140 145]    # sütunların toplamı

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)                      # => [34 44 17 26 93 22 80 89 88 68]
print(rnd_numbers.max())                # => 93
print(rnd_numbers.min())                # => 17
print(rnd_numbers.mean())               # => 56.1   # ortalama
print(rnd_numbers.argmax())             # => 4      # max'ın indexi
print(rnd_numbers.argmin())             # => 2      # min'in indexi

