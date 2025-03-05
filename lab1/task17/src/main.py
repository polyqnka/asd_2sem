def count_numbers(n):
    module = 10 ** 9
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    # dp[i][j] - количество способов набрать номер длиной i, который заканчивается на j
    dp = [[0] * 10 for _ in range(n + 1)]

    # dp = [
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # dp[0]
    #    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],  # dp[1]
    #   [2, 1, 2, 1, 2, 0, 2, 2, 2, 2],  # dp[2]
    #   [4, 4, 4, 4, 5, 0, 5, 4, 2, 4], # dp[3]
    #    ...
    # ]

    for j in range(10):
        if j != 8 and j != 0:
            dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(10):
            for move in moves[j]:
                dp[i][j] = (dp[i][j] + dp[i - 1][move]) % module

    result = sum(dp[n][j] for j in range(10)) % module
    return result

def read_file(src):
    with open(src+'input.txt', 'r') as f:
        n = int(f.read().strip())
    return n

def write_answ(src, result):
    with open(src+'output.txt', 'w') as f:
        f.write(str(result))

def main(src):
    n = read_file(src)
    result = count_numbers(n)
    write_answ(src, result)

if __name__ == '__main__':
    main('../txtf/')
