nums = ["a","b","c","s","r","s"]
def x(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1
print xrange(3)

