#stub merge_sort
def merge_sort(alist):
    start = 0
    end = len(alist)
    if end - start > 1 :
        mid = (end - start)//2
        blist = alist[start:mid]
        clist = alist[mid:end]
        alist = merge_list(merge_sort(blist), merge_sort(clist))
    return(alist)


#stub merge_lists
def merge_list(blist, clist):
    alist = []
    j = 0
    k = 0
    while j < (len(blist)) and k < (len(clist)):
        if blist[j] < clist[k]:
            alist.append(blist[j])
            j = j + 1
        else :
            alist.append(clist[k])
            k = k + 1

    if j < (len(blist)) :
        alist.extend(blist[j:])
    else:
        alist.extend(clist[k:])
    return(alist)

unsorted_list = [3, 2, 1, 4, 4, 6, 3,10, 3, 8, 9, 0, 2, 1, 3]
print(merge_sort(unsorted_list))