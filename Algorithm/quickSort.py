#快速排序
def parttion(list,left,right):   #left = 0,right = len(right) - 1
    key = list[left]    #先设置一个基数
    low = left          #设置左侧起始位置
    high = right        #设置右侧起始位置
    while low < high:   #判断 low和high的大小关系，直到low = high
        #high从右到左开始扫描，直到找到比基数大的一个数
        while (low < high) and (list[high] >= key):  #
            high -= 1
        list[low] = list[high]  #将low和high两个值交换位置
        #low从左到右开始扫描，知道找到比基数小的一个数
        while (low < high) and (list[low] <= key):
            low += 1
        list[high] = list[low]# 将low和high两个值交换位置
        #当low = high以后，在基数key左边的都比key小，右边的都比key大，之后进行递归
        list[low] = key
    return low

def quicksort(list,left,right):
    if left < right:
        p = parttion(list,left,right)
        quicksort(list,left,p - 1)
        quicksort(list,p + 1,right)
    return list

#验证
list = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
aa = quicksort(list,0,len(list)-1)
print(aa)
