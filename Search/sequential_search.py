# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)
def sequential_search(li,key):
    length = len(li)
    for i in range(length):
        if li[i] == key:
            return i
    return None
li=[8,7,6,5,4,3,2,1,0]
print(sequential_search(li,8))
