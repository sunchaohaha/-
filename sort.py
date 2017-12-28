l = [23,45,21,56,354]

//直接插入排序
def insert_sort(l):
    count = len(l)
    if count == 0 or count == 1:
        return l
    for i in range(1,count):
        j = i -1
        while j >= 0:
            if l[i] <= l[j]:
                l[j+1] = l[j]
                l[j] = l[i]
            j -= 1
        return l
      
//归并排序
def merge_sort(l):
    count = len(l)
    if count == 1 or count == 0:
        return l
    def merge(l,s,m,e):
       
        left = l[s,m+1]
        right = l[m+1,e+1]
        while s < e:
            while len(left) and len(right):
                if left[0] > right[0]:
                    l[s] = left.pop(0)
                else:
                    l[s] = right.pop(0)
            while len(left):
                l[s] = left.pop(0)
                s += 1
            while len(right):
                l[s] = right.pop(0)
                s += 1
    if start < end:
        mid = int((end + start)/2)
        merge_sort(l,start,mid)
        merge_sort(l,mid+1,end)
        merge(l,start,mid,end)
    return l
    
//选择排序
def select_sort(l):
    count = len(l)
    if count == 1 or count == 0:
        return l
    for i in range(count):
        l[i] = min(l[i,])
    return l
 
 //冒泡
 def bubble_sort(l):
     count = len(l)
    if count == 1 or count == 0:
        return l
    for i in range(count):
        for j in range(i+1,count):
            if l[i] > l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
    return l
    
