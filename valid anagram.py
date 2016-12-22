dic = {"a":1,"b":2}
for item in dic:
    dic[item] = dic.get(item, 0) + 1
    print dic[item]
print dic.get("c",0)+1

s="apple"
dic = [0]*26
print dic
for item in s:
    dic[ord(item)-ord("a")]+=1
print dic
