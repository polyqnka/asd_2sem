def read_from_file(path):
    with open(path, 'r') as f:
        N = int(f.readline())
        d, v = map(int, f.readline().split())
        R = int(f.readline())
        routes = []
        for _ in range(R):
            route = list(map(int, f.readline().split()))
            routes.append(route)
        return (N, d, v, R, routes)

def write_to_file(result, path):
    with open(path, 'w') as f:
        f.write(str(result) if result != float('inf') else "-1")

def find_min_time(cnt_vill, start, finish, cnt_flights, routes):
    min_time = [float('inf')] * (cnt_vill + 1)
    min_time[start] = 0

    # Алгоритм Беллмана-Форда
    updated = True
    for _ in range(cnt_vill):
        if not updated:
            break
        updated = False
        for route in routes:
            departure, dep_time, arrival, arr_time = route
            if dep_time >= min_time[departure] and arr_time < min_time[arrival]:
                min_time[arrival] = arr_time
                updated = True

    res = min_time[finish]
    if res != float('inf'):
        return str(res)
    else:
        return '-1'

def main(path):
    cnt_vill, start, finish, cnt_flights, routes = read_from_file(path+'input.txt')
    result = find_min_time(cnt_vill, start, finish, cnt_flights, routes)
    write_to_file(result, path+'output.txt')

if __name__ == '__main__':
    main('../txtf/')