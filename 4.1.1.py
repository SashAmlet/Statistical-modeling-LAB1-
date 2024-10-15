import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x, p):
    return (x**p) / (1 + x)

def monte_carlo_integration(p, num_points=10000000):
    # Генеруємо випадкові точки (x, y)
    x_random = np.random.uniform(0, 1, num_points)  # случайные x в интервале [0, 1]
    y_random = np.random.uniform(0, 1, num_points)  # случайные y в интервале [0, 1]

    # Значення функції f(x) = x^p / (1 + x)
    f_x = f(x_random, p)

    # Кількість точок під графіком
    points_under_curve = np.sum(y_random < f_x)

    # Наближене значення інтеграла
    integral_estimate = points_under_curve / num_points  # співвідношення точок під графіком

    return x_random, y_random, f_x, integral_estimate

# Параметр p
p = 3

# Кількість точок для методу Монте-Карло
num_points = 100000000

# Наближено обчислюємо інтеграл
x_random, y_random, f_x, integral_value = monte_carlo_integration(p, num_points)

# Знаходимо справжнє значення, використовуючи бібліотеку scipy.integrate
result, error = quad(f, 0, 1, args=(p,))

print(f"Approximate value of the integral for p={p}: {integral_value:.6f}")
print(f"The real value of the integral for p={p}: {result:.6f}")

# Візуалізація методу Монте-Карло
# Обмежуємо кількість точок для відображення
max_display_points = 10000
indices = np.random.choice(num_points, size=min(max_display_points, num_points), replace=False)

# Отримуємо обмежену кількість точок
x_random_display = x_random[indices]
y_random_display = y_random[indices]
f_x_display = f_x[indices]

# Визначення кольорів для крапок (зелені під графіком, червоні над графіком)
colors = ['green' if y < fx else 'red' for y, fx in zip(y_random_display, f_x_display)]

# Візуалізація методу Монте-Карло
x = np.linspace(0, 1, 500)
f_x_curve = (x**p) / (1 + x)

plt.plot(x, f_x_curve, label=f'Function $f(x) = \\frac{{x^p}}{{1+x}}$, p={p}', color='blue')

# Побудова точок (обмежена кількість)
plt.scatter(x_random_display, y_random_display, c=colors, s=1)

# Область під графіком
plt.fill_between(x, f_x_curve, color='lightblue', alpha=0.4)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Monte Carlo method for integral')
plt.legend()
plt.show()