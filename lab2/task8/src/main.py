import sys
sys.setrecursionlimit(1 << 25)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(n, nodes):
    tree = [None] * (n + 1)
    for i in range(1, n + 1):
        key, left, right = nodes[i-1]
        if tree[i] is None:
            tree[i] = TreeNode(key)
        if left != 0:
            tree[left] = TreeNode(nodes[left-1][0])
            tree[i].left = tree[left]
        if right != 0:
            tree[right] = TreeNode(nodes[right-1][0])
            tree[i].right = tree[right]

    if n>0:
        return tree[1]
    else:
        return None

def tree_height(node):
    if node is None:
        return 0
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return max(left_height, right_height) + 1

def read_from_file(path):
    with open(path) as f:
        n = int(f.readline())
        nodes = [tuple(map(int, f.readline().split())) for _ in range(n)]
    return n, nodes

def write_to_file(result, path):
    with open(path, 'w') as f:
        f.write(str(result))

def find_height(n, nodes):
    tree = build_tree(n, nodes)
    return tree_height(tree)

def main(path):
    n, nodes = read_from_file(path+'/input.txt')
    result = find_height(n, nodes)
    write_to_file(result, path+'/output.txt')

if __name__ == "__main__":
    main('../txtf')