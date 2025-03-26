import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sum_ab = a + b
product_ab = a * b
difference_ab = a - b
quotient_ab = a / b
a_squared = a ** 2
a_plus_10 = a + 10
b_times_2_5 = b * 2.5

print("Suma:", sum_ab)
print("Iloczyn:", product_ab)
print("Różnica:", difference_ab)
print("Iloraz:", quotient_ab)
print("a do kwadratu:", a_squared)
print("a + 10:", a_plus_10)
print("b * 2.5:", b_times_2_5)

M = np.array([[1, 2], [3, 4]])
v = np.array([10, 20])
M_plus_v = M + v

print("M po dodaniu wektora v do każdego wiersza:")
print(M_plus_v)
