
def solution(A):
    B = [1 if a == 0 else -1 for a in A]
    C = [0]
    for i in range(1, len(B)):
        C.append(C[i-1] + B[i])

    min_curr = 10000000
    min_i = best_L = best_R = best = 0
    for i in range(len(C)):
        gap = C[i] - min_curr
        if gap > best:
            best = gap
            best_L, best_R = min_i, i
        if C[i] < min_curr:
            min_curr, min_i = C[i], i

    return best_L+1, best_R


A = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0]
# A = [1, 0, 0, 1, 0, 0, 1, 0]

L, R = solution(A)
print(A)
print(L, R)
