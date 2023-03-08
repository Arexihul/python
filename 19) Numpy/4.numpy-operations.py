import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)                         # => [39 47 10 52 28 49]
print(numbers2)                         # => [61 28 69 60 89 16]

print(numbers1 + numbers2)              # => [100  75  79 112 117  65]
print(numbers1 + 10)                    # => [49 57 20 62 38 59]
print(numbers1 - numbers2)              # => [-22  19 -59  -8 -61  33]
print(numbers1 - 10)                    # => [29 37  0 42 18 39]
print(numbers1 * numbers2)              # => [2379 1316  690 3120 2492  784]
print(numbers1 * 10)                    # => [390 470 100 520 280 490]
print(numbers1 / numbers2)              # => [0.63934426 1.67857143 0.14492754 0.86666667 0.31460674 3.0625    ]
print(numbers1 / 10)                    # => [3.9 4.7 1.  5.2 2.8 4.9]

print(np.sin(numbers1))   # sayıların sinüsü           # =>  [ 0.96379539  0.12357312 -0.54402111  0.98662759  0.27090579 -0.95375265]
print(np.cos(numbers1))   # sayıların cosinüsü         # =>  [ 0.26664293 -0.99233547 -0.83907153 -0.16299078 -0.96260587  0.30059254]
print(np.sqrt(numbers1))  # sayıların karekökü         # =>  [6.244998   6.8556546  3.16227766 7.21110255 5.29150262 7.        ]
print(np.log(numbers1))   # sayıların logaritması      # =>  [3.66356165 3.8501476  2.30258509 3.95124372 3.33220451 3.8918203 ]

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)                        # => [[39 47 10]
                                        #     [52 28 49]]
print(mnumbers2)                        # => [[61 28 69]
                                        #     [60 89 16]]

print(np.vstack((mnumbers1,mnumbers2))) # Matrisleri dikeyde birleştirir   # => [[39 47 10]
                                                                           #     [52 28 49]
                                                                           #     [61 28 69]
                                                                           #     [60 89 16]]
print(np.hstack((mnumbers1,mnumbers2))) # Matrisleri yatayda birleştirir   # =>  [[39 47 10 61 28 69]
                                                                           #      [52 28 49 60 89 16]]              

print(numbers1 >= 50)                   # => [False False False  True False False]
ciftMi = numbers1 %2 == 0

print(ciftMi)                           # => [False False  True  True  True False]
print(numbers1[ciftMi])                 # => [10 52 28]

