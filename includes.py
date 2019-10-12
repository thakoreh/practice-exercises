def includes(coll,val,osi=None):
    if type(coll)==list and osi==None:
        if val in coll:
            return True
        else:
            return False
    if type(coll)==list:
        coll=coll[osi:]
        if val in coll:
            return True
        else:
            return False
    if type(coll)==dict:
        osi=None
        if val in coll.values():
            return True
        else:
            return False
    if type(coll)==str:
        osi=None
        listing=[]
        for c in coll:
            listing.append(c)
        if val in listing:\
            return True
        else: 
            return False

    pass

print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False