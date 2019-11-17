class Solution:
    def climbStairs(self, n: int) -> int:
        self.stairs_record = dict()
        return self.stairs(n)

    def stairs(self, n):
        if n in self.stairs_record:
            return self.stairs_record[n]
        if n == 1:
            self.stairs_record[n] = 1
            return 1
        if n == 2:
            self.stairs_record[n] = 2
            return 2
        self.stairs_record[n] = self.stairs(n - 1) + self.stairs(n - 2)
        return self.stairs_record[n]
