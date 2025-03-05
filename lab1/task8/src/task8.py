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

    # Жадный алгоритм
    count = 0
    last_end_time = 0

    for si, fi in lectures:
        if si >= last_end_time:
            count += 1
            last_end_time = fi

    # Запись результата
    with open('/Users/polinamitrofanova/Desktop/asd/asd_2sem/lab1/task8/txtf/output.txt', 'w') as f:
        f.write(str(count))

    # Замеры времени и памяти
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time:.6f} сек")
    print(f"Использовано памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")

    tracemalloc.stop()  # Останавливаем отслеживание памяти

# Вызов функции
schedule_lectures()