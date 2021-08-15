# https://leetcode.com/problems/rle-iterator/submissions/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.map = []
        self.curIdx = 0
        
        for i in range(len(encoding)//2):
            i*=2
            if encoding[i]:
                self.map.append([encoding[i+1], encoding[i]])
            

    def next(self, n: int) -> int:
        while (n and self.curIdx < len(self.map)):        
            if self.map[self.curIdx][1] >= n:
                self.map[self.curIdx][1] -= n
                return self.map[self.curIdx][0]
            else:
                n -= self.map[self.curIdx][1]
                self.map[self.curIdx][1] = 0
                self.curIdx += 1
                
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)