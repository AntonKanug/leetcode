# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {}
            self.data[key]['-timestamps'] = []
            
        self.data[key][timestamp] = value
        self.data[key]['-timestamps'].append(timestamp)

            

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            if timestamp in self.data[key]:
                return self.data[key][timestamp]
            else:
                time = self.binSearch(timestamp, self.data[key]['-timestamps'])
                if time != -1: return self.data[key][time] 
        return ''
    
    def binSearch(self,val, arr):
        l, r = 0, len(arr)-1
        while l<=r:
            mid = l + (r-l)//2
            if arr[mid] < val: l = mid+1
            elif arr[mid] > val: r = mid-1
        
        return arr[r] if r >= 0 else -1

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
