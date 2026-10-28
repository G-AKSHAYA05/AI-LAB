def alphabeta(d, i, maxp, v, a, b):
    if d == 0:
        return v[i]

    if maxp:
        best = float('-inf')
        for j in range(2):
            val = alphabeta(d-1, i*2+j, False, v, a, b)
            best = max(best, val)
            a = max(a, best)
            if b <= a:
                break
        return best
    else:
        best = float('inf')
        for j in range(2):
            val = alphabeta(d-1, i*2+j, True, v, a, b)
            best = min(best, val)
            b = min(b, best)
            if b <= a:
                break
        return best

v = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", alphabeta(3, 0, True, v, float('-inf'), float('inf')))