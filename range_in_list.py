def range_in_list(listing,si=0,li=0):
    if li:
        li=li+1
        pass
    else:
        li=len(listing)
    return sum(listing[si:li])
    pass

print(range_in_list([1,2,3,4],0,3))