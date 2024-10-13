import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm, kstest

# 1. Метод оберненої функції (Бокса-Мюллера)
def box_muller_method(n):
    u1 = np.random.rand(n)  # рівномірно розподілені величини на [0, 1]
    u2 = np.random.rand(n)
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    return z0  # нормально розподілена величина mu=0, sigma=1

# 2. Використання random.gauss()
def random_gauss_method(n, mu=0, sigma=1):
    return [random.gauss(mu, sigma) for _ in range(n)]

# Моделюємо нормальну величину X
n = 1000  # кількість експериментів

# Моделювання методом 
box_muller_data = box_muller_method(n)

# Моделювання з використанням random.gauss
random_gauss_data = random_gauss_method(n)

# Оцінка середнього та дисперсії для методу оберненої функції
mean_box_muller = np.mean(box_muller_data)
variance_box_muller = np.var(box_muller_data)

# Оцінка середнього та дисперсії для random.gauss
mean_random_gauss = np.mean(random_gauss_data)
variance_random_gauss = np.var(random_gauss_data)

print(f"Box-Muller method: Mean={mean_box_muller:.4f}, Dispersion = {variance_box_muller:.4f}")
print(f"Random.gauss() function: Mean ={mean_random_gauss:.4f}, Dispersion = {variance_random_gauss:.4f}")

# Перевірка гіпотези щодо нормальності розподілу за допомогою критерію Колмогорова-Смирнова
ks_stat_box_muller, p_value_box_muller = kstest(box_muller_data, 'norm')
ks_stat_random_gauss, p_value_random_gauss = kstest(random_gauss_data, 'norm')

print(f"Kolmogorov-Smirnov test for the Box-Muller method: p-value = {p_value_box_muller:.4f}")
print(f"Kolmogorov-Smirnov test for random.gauss: p-value = {p_value_random_gauss:.4f}")

# Побудова гістограм
plt.hist(box_muller_data, bins=30, alpha=0.6, label='Box-Muller Method', density=True)
plt.hist(random_gauss_data, bins=30, alpha=0.6, label='random.gauss()', density=True)

# Теоретична крива нормального розподілу
x = np.linspace(-4, 4, 1000)
plt.plot(x, norm.pdf(x), label='Theoretical normal distribution', color='black', lw=2)
plt.xlabel('The value of X')
plt.ylabel('Frequency')
plt.legend()
plt.title('Modeling the normal distribution')
plt.show()
