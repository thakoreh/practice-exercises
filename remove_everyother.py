def remove_everyother(listing):
    newlist=[]
    count=1
    for l in listing:
        if count%2!=0:
            newlist.append(l)
            count=count+1
        else:
            count=count+1
            continue

    return newlist
    pass


print(remove_everyother([5,1,2,4,1]))