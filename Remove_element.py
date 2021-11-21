def removeElement(nums,val): #done
    while val in nums:
        nums.remove(val)
    return len(nums)

p1 = [0,1,2,2,3,0,4,2]
p2 = 2
print(removeElement(p1,p2))

"""""
Runtime: 32 ms, faster than 78.01% of Python3 online submissions for Remove Element.
Memory Usage: 14.1 MB, less than 92.17% of Python3 online submissions for Remove Element.
"""""