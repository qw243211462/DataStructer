#coding=gbk
#ð������
L = [20,100,7,10,9,90,4,199]
def bubbleSort(list):
    length = len(list)
    # ��һ������
    for i in range(length):
        for j in range(1,length - i):
            if list[j -1] > list[j]:
                temp = list[j -1]
                list[j - 1] = list[j]
                list[j] = temp
    print(list)
bubbleSort(L)
