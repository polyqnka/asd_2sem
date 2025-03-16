def generate_max_test_case():
    n = 200000
    nodes = []
    for i in range(1, n + 1):
        key = i
        left = 0  # Нет левого потомка
        right = i + 1 if i < n else 0  # Правый потомок — следующий узел, кроме последнего
        nodes.append((key, left, right))

    with open('input_max.txt', 'w') as f:
        f.write(f"{n}\n")
        for node in nodes:
            f.write(f"{node[0]} {node[1]} {node[2]}\n")


generate_max_test_case()