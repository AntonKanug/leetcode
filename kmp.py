# Knuth-Morris-Pratt

# Create kmp table array
# Keep i(0), j(1) pointers
# If match table[j] = i+1  i++ j++
# Else j == 0 => i++
# Else i = table[i-1] 

# KMP
# Iterate over main string
# If s[i] == k[j] i++; k++; check if j == len(k) => count+=1; j = kmptable[j-1] 
# Else j == 0 => i++
# Else j = kmptable[j-1] 

def kmp(s: str, k: str):

    # a a b a a b c
    # [0, 1, 0, 1, 2, 3, 0]

    # j is going through string
    # i is starting from beginning
    def makeTable(k):
        arr = [0] * len(k)
        i, j = 0, 1

        while(j < len(k)):
            if k[i] == k[j]:
                arr[j] = i+1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = arr[i-1]
        return arr

    kmp_table = makeTable(k)

    count = 0
    j = 0
    i = 0
    while i < len(s):
        if s[i] == k[j]:
            j += 1
            i += 1
            if j == len(k):
                count += 1
                j = kmp_table[j-1]
        elif j == 0:
            i += 1
        else:
            j = kmp_table[j-1]

    return count


print(kmp("aabaabaaababa", "aaba"))
