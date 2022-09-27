
import matplotlib.pyplot as plt
import random

y_values = [random.randint(5,50) for _ in range(1000)]

plt.bar(range(1000),y_values)
plt.show()

for i in range(3,len(y_values)-3):
    y_values[i] = sum(y_values[i-3:i+3]) // 6

plt.bar(range(1000),y_values)
plt.show()

