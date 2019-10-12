def find_the_duplicate(array):
    count=0
    listing=[]
    for arr in array:
        if array.count(arr)>1:
            count=1
            listing.append(arr)
    return listing[-1] if count==1 else False    
    pass

print(find_the_duplicate([1,2,1,4,3,12]))
