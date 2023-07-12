def minimumBribes(q):
    bribes = 0
    w = [1, 2, 3]
    for i in range(len(q)-1):
        if q[i] in w:
            bribes += w.index(q[i])
            w.append(i+4)
            w.remove(q[i])
        else:
            print('Too chaotic')
            return
    print(bribes)
