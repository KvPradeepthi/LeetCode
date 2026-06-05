class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 0:
                return 0
            s = str(n)
            @cache
            def dp(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return (1, 0)
                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wave = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if not started and d == 0:
                        cnt, wave = dp(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10
                        )
                        total_cnt += cnt
                        total_wave += wave
                    else:
                        if not started:
                            cnt, wave = dp(
                                pos + 1,
                                ntight,
                                True,
                                10,
                                d
                            )
                            total_cnt += cnt
                            total_wave += wave
                        else:
                            add = 0

                            if prev2 != 10:
                                if (
                                    (prev2 < prev1 > d)
                                    or
                                    (prev2 > prev1 < d)
                                ):
                                    add = 1

                            nprev2 = prev1 if prev1 != 10 else 10
                            nprev1 = d
                            cnt, wave = dp(
                                pos + 1,
                                ntight,
                                True,
                                nprev2,
                                nprev1
                            )
                            total_cnt += cnt
                            total_wave += wave + add * cnt
                return total_cnt, total_wave
            return dp(0, True, False, 10, 10)[1]
        return solve(num2) - solve(num1 - 1)
        