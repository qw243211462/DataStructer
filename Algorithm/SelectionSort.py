#coding=gbk
#选择排序是一种简单直观的排序算法。工作原理是每一次从待排序的数据元素中选出最小（或最大）的元素，放在起始位置
L = [4,2,7,5,1,9,10,20,3]
def select_sort(lists):
    #计算列表的长度
    count = len(lists)
    #遍历其中的每一个元素
    for i in range(0, count):
        #将第一个位置设置成最小元素的位置
        min = i
        #第二层循环，在所有元素中选出最小的值
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        #交换最小值
        temp = lists[min]
        lists[min] = lists[i]
        lists[i] = temp
    return lists
aa = select_sort(L)
print(aa)