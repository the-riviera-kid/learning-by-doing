 
def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))
     
# Driver Code
lst = [2, 3, 1, 4, 6]
print(checkConsecutive(lst))