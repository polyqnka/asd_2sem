def read_from_file(path):
    with open(path, 'r') as f:
        string = f.readline()
        return string

def write_to_file(result, path):
    with open(path, 'w') as f:
        f.write(result)

def decompose(st):
    n = len(st)
    if n == 0:
        return ""

    dp = [""] * (n + 1)
    dp[0] = ""

    for i in range(1, n + 1):
        if dp[i - 1]:
            if dp[i - 1][-1] in '0123456789':
                dp[i] = dp[i - 1] + "+" + st[i - 1]
            else:
                dp[i] = dp[i - 1] + st[i - 1]
        else:
            dp[i] = st[i - 1]

        for l in range(1, i):
            substring = st[i - l:i]
            count = 1
            j = i - l
            while j - l >= 0 and st[j - l:j] == substring:
                count += 1
                j -= l

            compressed = substring
            if count > 1:
                compressed += f"*{count}"

            if dp[j]:
                full_repr = dp[j] + "+" + compressed
            else:
                full_repr = compressed

            if len(full_repr) < len(dp[i]):
                dp[i] = full_repr

    return dp[n]

def main(path):
    string = read_from_file(path+'input.txt')
    result = decompose(string)
    write_to_file(result, path+'output.txt')

if __name__ == '__main__':
    main('../txtf/')