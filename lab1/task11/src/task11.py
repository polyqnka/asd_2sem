import tracemalloc
import time

def knapsack():
    # Запуск измерений
    tracemalloc.start()
    start_time = time.time()

    # Чтение входных данных
    with open('/Users/polinamitrofanova/Desktop/asd/asd_2sem/lab1/task11/txtf/input.txt', 'r') as f:
        W, n = map(int, f.readline().split())
        weights = list(map(int, f.readline().split()))

    # DP массив, где dp[j] — максимальный вес при вместимости j
    dp = [0] * (W + 1)

    # Перебираем все слитки
    for w in weights:
        # Итерируем по вместимости рюкзака *в обратном порядке*
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + w)

    # Ответ — максимальный возможный вес в рюкзаке
    result = dp[W]

    # Запись в файл
    with open('/Users/polinamitrofanova/Desktop/asd/asd_2sem/lab1/task11/txtf/output.txt', 'w') as f:
        f.write(str(result))

    # Измерение памяти и времени
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.6f} сек")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

    tracemalloc.stop()

if __name__ == "__main__":
    knapsack()