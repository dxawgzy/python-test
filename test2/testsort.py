#!/usr/bin/python
#coding=utf-8

# 排序算法

def sort_1(list):
    length = len(list)
    for i in range(length-1):
        for j in range(i+1, length):
            if list[j] < list[i]:
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp
        print list
    return list

# 冒泡排序
def sort_maopao(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length-1-i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
        print list
    return list

# 选择排序
def sort_xuanze(list):
    length = len(list)
    for i in range(length-1):
        index = i
        for j in range(i+1, length):
            if list[j] < list[index]:
                index = j
        tmp = list[i]
        list[i] = list[index]
        list[index] = tmp
        print list
    return list

# 插入排序
def sort_charu(list):
    length = len(list)
    for i in range(1, length):
        index = i - 1
        tmp = list[i]
        # if index >= 0 and list[index] > tmp: #此处不能用if，需要用while，原因是从后往前比较时，中间可能有些数据不满足 > 条件而跳出if循环
        while index >= 0 and list[index] > tmp:
            list[index+1] = list[index]
            index -= 1
        list[index+1] = tmp
        print list, index
    return list

# 计数排序
def sort_jishu(list):
    length = len(list)
    maxnum = max(list)
    tmplist = [0] * (maxnum+1)
    tmplength = len(tmplist)
    index = 0
    for i in range(length):
        if not tmplist[list[i]]:
            tmplist[list[i]] = 0
        tmplist[list[i]] += 1
    for i in range(tmplength):
        while tmplist[i] > 0:
            list[index] = i
            tmplist[i] -= 1
            index += 1
        print list, tmplist
    return list

# 基数排序

# 桶排序

# 快速排序

# 堆排序

# 希尔排序

# 归并排序

# a = [5, 2, 3, 1, 4]
a = [5, 8, 6, 3, 9, 2, 1, 7]
print "input: %s" % a
# a.sort()
# print a
# b = sort_1(a)
# b = sort_maopao(a)
# b = sort_xuanze(a)
# b = sort_charu(a)
b = sort_jishu(a)

print "output:", b
