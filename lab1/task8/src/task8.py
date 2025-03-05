import tracemalloc
import time


def schedule_lectures():
    tracemalloc.start()  # Начинаем отслеживание памяти
    start_time = time.time()  # Засекаем время выполнения

    # Чтение входных данных
    with open('/Users/polinamitrofanova/Desktop/asd/asd_2sem/lab1/task8/txtf/input.txt', 'r') as f:
        N = int(f.readline().strip())  # Читаем число N и удаляем лишние пробелы/перенос строки
        lectures = []
        for _ in range(N):
            line = f.readline().strip()  # Убираем лишние пробелы
            values = list(map(int, line.split()))  # Преобразуем в список чисел
            if len(values) != 2:
                raise ValueError(f"Неверный формат входных данных: {line}")  # Проверка корректности данных
            lectures.append(tuple(values))

    # Сортировка заявок по времени окончания
    lectures.sort(key=lambda x: x[1])

    # Динамическое программирование
    dp = [0] * (N + 1)  # Массив для хранения максимального числа лекций до каждой лекции
    # Заполнение массива dp
    for i in range(1, N + 1):
        # Для каждой лекции i
        si, fi = lectures[i - 1]

        # Поиск лекции, которая заканчивается до начала текущей
        last_non_conflicting = 0
        for j in range(i - 1, 0, -1):
            if lectures[j - 1][1] <= si:
                last_non_conflicting = j
                break

        # Рекуррентное соотношение: либо пропустить эту лекцию, либо взять её
        dp[i] = max(dp[i - 1], dp[last_non_conflicting] + 1)

    # Результат - максимальное количество лекций
    result = dp[N]

    # Запись результата
    with open('/Users/polinamitrofanova/Desktop/asd/asd_2sem/lab1/task8/txtf/output.txt', 'w') as f:
        f.write(str(result))

    # Замеры времени и памяти
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.6f} сек")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

    tracemalloc.stop()  # Останавливаем отслеживание памяти


# Вызов функции
schedule_lectures()