class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def helper(a, b):
            if not b:
                return 1
            last = b.pop()
            part1 = pow(helper(a, b), 10, MOD)
            part2 = pow(a, last, MOD)
            return (part1 * part2) % MOD
        return helper(a, b)