class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        T = [[0] * size for _ in range(size)]
        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1
        for v in range(m):
            row = m + v
            for u in range(v + 1, m):
                T[row][u] = 1
        def mat_mul(A, B):
            n1 = len(A)
            n2 = len(B[0])
            k = len(B)
            C = [[0] * n2 for _ in range(n1)]
            for i in range(n1):
                for t in range(k):
                    if A[i][t] == 0:
                        continue
                    a = A[i][t]
                    Bt = B[t]
                    for j in range(n2):
                        if Bt[j]:
                            C[i][j] = (C[i][j] + a * Bt[j]) % MOD
            return C

        def mat_pow(M, p):
            sz = len(M)
            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        # Initial state for length = 2
        init = [[0] for _ in range(size)]

        for v in range(m):
            init[v][0] = v              # up[v]
            init[m + v][0] = m - 1 - v # down[v]

        if n == 2:
            return m * (m - 1) % MOD

        P = mat_pow(T, n - 2)
        final_state = mat_mul(P, init)

        ans = 0
        for i in range(size):
            ans = (ans + final_state[i][0]) % MOD

        return ans
        