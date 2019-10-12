
def list_check(listing):
    count=0
    for item in listing:
        if type(item)!=list:
            count=count+1
    return False if count>0 else True

    pass

print(list_check([1, True, [],[1],[2,3]]))