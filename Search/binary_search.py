# 针对有序查找表的二分查找算法
# 时间复杂度O(log(n))
def binary_search(li,key):
    low = 0
    high = len(li) - 1
    while(low <= high):
        mid = (low + high) // 2
        if key < li[mid]:
            high = mid - 1
        if li[mid] < key:
            low = mid + 1
        if li[mid] == key:
            return mid
    return None
li=[0,1,2,3,4,5,6,7,8]
print(binary_search(li,8))
