#coding=gbk
#��������,��������Ļ����������ǽ�һ�����ݲ��뵽�Ѿ��ź�������������У��Ӷ��õ�һ���µġ�������һ���������ݣ��㷨�������������ݵ�����
def insert_sort(lists):
    #�����б�ĳ���
    count = len(lists)
    #�����б��г���һ��Ԫ��֮�������Ԫ��
    for i in range(1, count):
        #��ȡһ������key
        key = lists[i]
        #��L[0��i]֮�ڵ����ֽ�������֮��ÿ�θ���һ��i����������뵽֮ǰ����õ��б���
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