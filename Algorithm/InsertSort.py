#coding=gbk
#插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序
def insert_sort(lists):
    #计算列表的长度
    count = len(lists)
    #遍历列表中除第一个元素之外的所有元素
    for i in range(1, count):
        #获取一个基数key
        key = lists[i]
        #将L[0，i]之内的数字进行排序，之后每次更新一个i，都将其插入到之前排序好的列表中
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
L = [20,100,7,10,9,90,4,199]
aa = insert_sort(L)
print(aa)