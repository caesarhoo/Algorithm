# nums = [0,1,2,0,3]
# a=[]
# for i in nums:
#     if i!=0:
#         a.append(i)
# while len(a)<len(nums):
#     a.append(0)
# nums=a
# print nums

nums = [0,1,3,4,0,7,0,9,0]
nums.sort(cmp=lambda a,b:0 if b else -1)
print nums