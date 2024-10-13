import numpy as np

def simulate_coin_flips(N, K):
    # Моделюємо K експериментів з N підкиданням монети
    # 0 – це решка, 1 – це герб
    results = np.random.randint(0, 2, size=(K, N))
    
    # Підраховуємо кількість гербів у кожному експерименті
    heads_per_experiment = np.sum(results, axis=1)
    
    # Підраховуємо загальну кількість гербів за всі експерименти
    total_heads = np.sum(heads_per_experiment)
    
    return heads_per_experiment, total_heads


N = 1000  # кількість підкидань в одному експерименті
K = 500   # кількість експериментів
heads_per_experiment, total_heads = simulate_coin_flips(N, K)

print(f"The total number of tosses: {N*K}")
print(f"Number of heads in each experiment: {heads_per_experiment}")
print(f"Total number of heads for all experiments: {total_heads}")
