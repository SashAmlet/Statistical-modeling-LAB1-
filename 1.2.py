import numpy as np

def simulate_dice_rolls(N, K):
    # Моделюємо K експериментів з N підкидання кубика
    # Кубик має значення від 1 до 6
    results = np.random.randint(1, 7, size=(K, N))
    
    # Підраховуємо, скільки разів випала кожна цифра (1-6) у кожному експерименті
    counts_per_experiment = np.array([np.bincount(results[i], minlength=7)[1:] for i in range(K)])
    
    # Підраховуємо загальну кількість випадень кожної цифри за всі експерименти
    total_counts = np.sum(counts_per_experiment, axis=0)
    
    return counts_per_experiment, total_counts


N = 10  # кількість підкидань кубика в одному експерименті
K = 11  # кількість експериментів
counts_per_experiment, total_counts = simulate_dice_rolls(N, K)

print(f"The total number of tosses: {N*K}")
print(f"How many of each number should appear, in theory?: {N*K/6}")
print(f"The number of occurrences of each digit in each experiment:\n{counts_per_experiment}")
print(f"Total number of occurrences of each digit for all experiments: {total_counts}")
