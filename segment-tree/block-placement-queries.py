from bisect import bisect_left, insort
class Solution:
    def getResults(self, queries):
        mx = max(q[1] for q in queries)

        tree = [0] * (4 * (mx + 2))
        obstacles = [0, mx]

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
            if ql > r or qr < l:
                return 0

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            return max(
                query(node * 2, l, mid, ql, qr),
                query(node * 2 + 1, mid + 1, r, ql, qr)
            )

        update(1, 0, mx, mx, mx)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                pos = bisect_left(obstacles, x)

                left = obstacles[pos - 1]
                right = obstacles[pos]

                update(1, 0, mx, x, x - left)
                update(1, 0, mx, right, right - x)

                insort(obstacles, x)

            else:
                _, x, sz = q

                pos = bisect_left(obstacles, x)

                best = query(1, 0, mx, 0, x)

                left = obstacles[pos - 1]
                best = max(best, x - left)

                ans.append(best >= sz)

        return ans