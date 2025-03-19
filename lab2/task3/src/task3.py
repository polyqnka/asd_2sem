class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(key)
                    return
            elif key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(key)
                    return
            else:
                return  # Уже есть, пропускаем

    def find_min_greater_than(self, key):
        current = self.root
        candidate = None

        while current:
            if current.key > key:
                candidate = current
                current = current.left
            else:
                current = current.right

        return candidate.key if candidate else 0


def process_queries(input_file="input.txt", output_file="output.txt"):
    tree = BST()
    results = []

    with open(input_file, "r") as file:
        for line in file:
            action, number = line.split()
            number = int(number)

            if action == "+":
                tree.insert(number)
            elif action == ">":
                results.append(str(tree.find_min_greater_than(number)))

    with open(output_file, "w") as file:
        file.write("\n".join(results) + "\n")

    print("Простейшее BST:")
    print("\n".join(results) + "\n")


if __name__ == "__main__":
    process_queries()