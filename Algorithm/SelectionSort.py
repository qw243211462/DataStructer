#coding=gbk
#ѡ��������һ�ּ�ֱ�۵������㷨������ԭ����ÿһ�δӴ����������Ԫ����ѡ����С������󣩵�Ԫ�أ�������ʼλ��
L = [4,2,7,5,1,9,10,20,3]
def select_sort(lists):
    #�����б�ĳ���
    count = len(lists)
    #�������е�ÿһ��Ԫ��
    for i in range(0, count):
        #����һ��λ�����ó���СԪ�ص�λ��
        min = i
        #�ڶ���ѭ����������Ԫ����ѡ����С��ֵ
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        #������Сֵ
        temp = lists[min]
        lists[min] = lists[i]
        lists[i] = temp
    return lists
aa = select_sort(L)
print(aa)