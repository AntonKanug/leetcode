# https://leetcode.com/problems/web-crawler-multithreaded/submissions/

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import concurrent.futures as cf

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        output = set([startUrl])
        q = [startUrl]
        
        startUrlHost = startUrl.split('/')[2]
       
        while(q):
            
            with cf.ThreadPoolExecutor(max_workers=8) as executor:
                tempQ = set()
                
                for lists in executor.map(htmlParser.getUrls, q):
                    for i in lists:
                        if i not in output and startUrlHost == i.split('/')[2]:
                            tempQ.add(i)
                            output.add(i)
                            
                q = list(tempQ)
                
        return list(output)

        