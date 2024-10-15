import numpy as np
import matplotlib.pyplot as plt

# Визначаємо систему нерівностей
def is_inside_figure(x, y):
    cond1 = (-x <= y) & (y <= x)  # Умова: -x <= y <= x
    cond2 = (2 * x <= x**2 + y**2) & (x**2 + y**2 <= 4 * x)  # Умова: 2x <= x^2 + y^2 <= 4x
    return cond1 & cond2

def monte_carlo(x_min, x_max, y_min, y_max, num_points=10000000):
    # Генеруємо випадкові точки (x, y)
    x_random = np.random.uniform(x_min, x_max, num_points)
    y_random = np.random.uniform(y_min, y_max, num_points)

    # Перевіряємо, які точки задовольняють системі нерівностей
    points_inside = is_inside_figure(x_random, y_random)

    # Площа прямокутної області
    rect_area = (x_max - x_min) * (y_max - y_min)

    # Оцінка площі фігури
    figure_area = rect_area * np.sum(points_inside) / num_points

    return figure_area, x_random, y_random, points_inside


# Визначаємо межі прямокутної області (x от 0 до 2, y от -2 до 2)
x_min, x_max = 0, 4.5
y_min, y_max = -2.5, 2.5
num_points=10000000

figure_area, x_random, y_random, points_inside = monte_carlo(x_min, x_max, y_min, y_max, num_points=10000000)


print(f"Estimated figure area: {figure_area}")

# Візуалізація методу Монте-Карло
# Обмежуємо кількість точок для відображення
max_display_points = 100000
indices = np.random.choice(num_points, size=min(max_display_points, num_points), replace=False)

# Отримуємо обмежену кількість точок
x_random_display = x_random[indices]
y_random_display = y_random[indices]
points_inside_display = points_inside[indices]


plt.figure(figsize=(8, 8))
plt.scatter(x_random_display[points_inside_display], y_random_display[points_inside_display], color='green', s=1, label='Dots inside the figure')
plt.scatter(x_random_display[~points_inside_display], y_random_display[~points_inside_display], color='red', s=1, label='Points outside the figure')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Graphical visualization of the Monte Carlo method')
plt.show()

