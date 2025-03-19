import sys


def in_order_traversal(tree, node, result):
    if node == -1:
        return
    in_order_traversal(tree, tree[node][1], result)
    result.append(tree[node][0])
    in_order_traversal(tree, tree[node][2], result)


def pre_order_traversal(tree, node, result):
    if node == -1:
        return
    result.append(tree[node][0])
    pre_order_traversal(tree, tree[node][1], result)
    pre_order_traversal(tree, tree[node][2], result)


def post_order_traversal(tree, node, result):
    if node == -1:
        return
    post_order_traversal(tree, tree[node][1], result)
    post_order_traversal(tree, tree[node][2], result)
    result.append(tree[node][0])


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        tree = {}

        for i in range(n):
            key, left, right = map(int, f.readline().split())
            tree[i] = (key, left, right)

    in_order_result = []
    pre_order_result = []
    post_order_result = []

    in_order_traversal(tree, 0, in_order_result)
    pre_order_traversal(tree, 0, pre_order_result)
    post_order_traversal(tree, 0, post_order_result)

    print(f'in order {in_order_result}')
    print(f'pre order {pre_order_result}')
    print(f'post order {post_order_result}')

    with open("output.txt", "w") as f:
        f.write(" ".join(map(str, in_order_result)) + "\n")
        f.write(" ".join(map(str, pre_order_result)) + "\n")
        f.write(" ".join(map(str, post_order_result)) + "\n")


if __name__ == "__main__":
    main()
