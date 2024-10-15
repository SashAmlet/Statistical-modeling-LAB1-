import numpy as np
from scipy import integrate


# Перевірка приналежності точок перетину двох циліндрів
def is_inside_cylinder_intersection(x, y, z, r):
    cond1 = (x**2 + z**2 <= r**2)  # Крапки всередині першого циліндра
    cond2 = (y**2 + z**2 <= r**2)  # Крапки всередині другого циліндра
    return cond1 & cond2


def monte_carlo(r, num_points=10000000):
    # Генерація випадкових точок у кубі [-r, r] по x, y та z
    x_random = np.random.uniform(-r, r, num_points)
    y_random = np.random.uniform(-r, r, num_points)
    z_random = np.random.uniform(-r, r, num_points)

    # Перевіряємо, які точки перебувають усередині перетину
    points_inside = is_inside_cylinder_intersection(x_random, y_random, z_random, r)

    # Об'єм куба
    cube_volume = (2 * r)**3
    
    # Оцінка ймовірності попадання у фігуру
    p_estimate = np.sum(points_inside) / num_points

    # Оцінка обсягу фігури
    figure_volume = cube_volume * p_estimate

    # Оцінка стандартної помилки
    sigma_p = np.sqrt(p_estimate * (1 - p_estimate) / num_points)

    # Оцінка помилки обсягу
    std_error = sigma_p * cube_volume

    return figure_volume, std_error


# Радіус циліндрів
r = 1

figure_volume, std_error = monte_carlo(r)

print(f"Estimated volume of the figure: {figure_volume}")
print(f"Estimated error of the method: {std_error}")
