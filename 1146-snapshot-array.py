# https://leetcode.com/problems/snapshot-array/submissions/

class SnapshotArray:

    def __init__(self, length: int):
        # idx : [ids:[id0, id1..], {snapid: value}...]
        self.snaparray = {}
        self.snapID = 0
        for i in range(length): self.set(i,0)
            
    def set(self, index: int, val: int) -> None:            
        if index in self.snaparray:
            self.snaparray[index][self.snapID] = val
            if self.snaparray[index]['ids'][-1] != self.snapID:
                self.snaparray[index]['ids'].append(self.snapID)
        else:
            self.snaparray[index] = {'ids':[self.snapID], self.snapID: val}
            
    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1
    
    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snaparray[index]:
            snap_id = self.binSearch(snap_id, self.snaparray[index]['ids'])
            
        return self.snaparray[index][snap_id]
    
    def binSearch(self,val, arr):
        l, r = 0, len(arr)-1
        while l<=r:
            mid = l + (r-l)//2
    
            if arr[mid] == val: return mid
            elif arr[mid] > val: r = mid - 1
            else: l = mid + 1
        
        return arr[r]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
