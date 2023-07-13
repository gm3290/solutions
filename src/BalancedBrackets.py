def isBalanced(s):
    counter = [0, 0, 0]
    open_brackets = '{[('
    close_brackets = '}])'
    for i, c in enumerate(s):
        if c in open_brackets:
            counter[open_brackets.index(c)] += 1
        else:
            index = close_brackets.index(c)
            if counter[index] == 0 or (s[i - 1] in open_brackets and open_brackets.index(s[i - 1]) != index):
                return "NO"
            counter[index] -= 1
    if sum(counter):
        return "NO"
    return "YES"