class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, i = 0, 0
        temp, j = limit - people[0], len(people) - 1
        while i < j:
            if people[j] > temp:
                ans += 1
                j -= 1
            elif people[j] <= temp:
                ans += 1
                j -= 1
                i += 1
                temp = limit - people[i]
        if i == j:
            ans += 1
        return ans
