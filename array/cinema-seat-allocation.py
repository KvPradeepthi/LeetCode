class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)
        answer = 2 * n
        for row in rows:
            seats = rows[row]
            left = all(x not in seats for x in [2, 3, 4, 5])
            middle = all(x not in seats for x in [4, 5, 6, 7])
            right = all(x not in seats for x in [6, 7, 8, 9])
            if left and right:
                continue
            elif left or middle or right:
                answer -= 1
            else:
                answer -= 2
        return answer
        