class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # 1 2 2 3 3, limit = 3

        people.sort()
        left, right = 0, len(people)-1
        cnt = 0

        while left <= right:
            if left == right:
                cnt += 1
                break

            if people[left] + people[right] > limit:
                if people[right] <= limit :
                    cnt += 1
                    right -= 1
                    continue
                right -= 1
            elif people[left] + people[right] <= limit:
                cnt += 1
                left += 1
                right -= 1
            
        return cnt
            
        