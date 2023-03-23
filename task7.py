import random
import numpy as np
import time
import matplotlib.pyplot as plt


# Задание 1

mas1 = [random.randint(1, 10) for i in range(10**6)]
mas2 = [random.randint(1, 10) for i in range(10**6)]

time_start = time.perf_counter()
mas3 = [mas1[i]*mas2[i] for i in range(0, 10**6)]
all_time = time.perf_counter() - time_start
print(all_time)

mas1 = np.array(mas1)
mas2 = np.array(mas2)
time_start = time.perf_counter()
np.multiply(mas1, mas2)
all_time = time.perf_counter() - time_start
print(all_time)

# Задание 2, Вариант 9

arr = np.genfromtxt('data1.csv', delimiter=';')
time = arr[1:100, 0]
time = time[:, np.newaxis]
angle = arr[1:100, 9]
angle = angle[:, np.newaxis]
air_consumption = arr[1:100, 15]
air_consumption = air_consumption[:, np.newaxis]
correlation = np.subtract(air_consumption, angle)

plt.plot(time, angle, 'plum', label='angle(time)')
plt.plot(time, air_consumption, 'orange', label='air_consumption(time)')
plt.plot(time, correlation, 'slateblue', label='correlation')
plt.title('Графики для задания 2')
plt.xlabel('Время, с')
plt.ylabel('Угол опережения зажигания, °ПКВ\nМассовый расход воздуха, кг/ч')
plt.grid()
plt.legend(loc='lower right')
plt.show()

# Задание 3, Вариант 9

x = np.linspace(-5*np.pi, 5*np.pi)
y = x
z = y * np.cos(x)
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'forestgreen')
plt.title('График для задания 3')
plt.show()
