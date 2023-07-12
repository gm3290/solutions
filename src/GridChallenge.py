def gridChallenge(grid):
    r_srted = [sorted(list(letters)) for letters in grid]
    return "NO" if any(sorted(col) != list(col) for col in zip(*r_srted)) else "YES"


print(gridChallenge(['abc', 'ade', 'efg']))
