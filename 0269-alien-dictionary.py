# https://leetcode.com/problems/alien-dictionary/

from collections import *

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pre = defaultdict(set)
        suc = defaultdict(set)
        
        for i in range(len(words)-1):
            tlen = 0
            for a,b in zip(words[i], words[i+1]):
                if a != b:
                    pre[b].add(a)
                    suc[a].add(b)
                    break
                tlen+=1
            if tlen == min(len(words[i]), len(words[i+1])) and len(words[i]) > len(words[i+1]):
                return ''
            
        # top sort

        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''
        
        while free:
            a = free.pop()
            order += a
            
            for b in suc[a]:
                pre[b].remove(a)
                if not pre[b]:
                    free.add(b)
      
        return order if set(order) == chars else ''
    