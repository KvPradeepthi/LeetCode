from bisect import bisect_left, insort
class Solution:
    def getResults(self, queries):
        MAXX = 50000
        tree = [0] * (4 * (MAXX + 1))
        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            return max(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            )

        obstacles = [0, MAXX]

        update(1, 0, MAXX, MAXX, MAXX)

        ans = []

        for q in queries:

            if q[0] == 1:
                x = q[1]

                i = bisect_left(obstacles, x)

                left = obstacles[i - 1]
                right = obstacles[i]

                update(1, 0, MAXX, right, right - x)
                update(1, 0, MAXX, x, x - left)

                insort(obstacles, x)

            else:
                _, x, sz = q

                i = bisect_left(obstacles, x)

                best = query(1, 0, MAXX, 0, x)

                left = obstacles[i - 1]
                best = max(best, x - left)

                ans.append(best >= sz)

        return ans