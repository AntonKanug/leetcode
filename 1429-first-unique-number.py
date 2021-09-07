# https://leetcode.com/problems/first-unique-number/submissions/

from collections import deque

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = {}
        self.q = deque()

        for i in nums:
            self.add(i)
                
    def showFirstUnique(self) -> int:
        while self.q:
            x = self.q.popleft()
            if self.count[x] == 1:
                self.q.appendleft(x)
                return x
        return -1

    def add(self, value: int) -> None:
        if value in self.count: 
            self.count[value] +=1
            return
        
        self.count[value] = 1
        self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)