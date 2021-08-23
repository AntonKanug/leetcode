# https://leetcode.com/problems/search-suggestions-system/submissions/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        idx = 0
        lenW = 0
        word = ''
        output = []
        
        for letter in searchWord:
            word += letter
            lenW +=1
            temp = []

            for j, prod in enumerate(products[idx:]):
                j += idx
                if word == prod[:lenW]: 
                    idx = j
                    while j < idx+3 and j < len(products) and word == products[j][:lenW]:
                        temp.append(products[j])
                        j+=1
                    break
                    
            output.append(temp)
            
        return output