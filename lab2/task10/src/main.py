def read_from_file(path):
    with open(path) as f:
        n = int(f.readline())
        nodes = [tuple(map(int, f.readline().split())) for _ in range(n)]
    return n, nodes

def write_to_file(result, path):
    with open(path, 'w') as f:
        f.write(str(result))

def check_tree(n, nodes):
    for i in range(n):
        key, left, right = nodes[i]
        if left!=0:
            if key<=nodes[left-1][0]:
                return "NO"
        if right!=0:
            if key>=nodes[right-1][0]:
                return "NO"
    return "YES"

def main(path):
    n, nodes = read_from_file(path+'/input.txt')
    result = check_tree(n, nodes)
    write_to_file(result, path+'/output.txt')

if __name__ == "__main__":
    main('../txtf')