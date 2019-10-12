def sum_pair(list,val):
    count=0
    for x in list:
        for y in list:
            if count==0:
                if y==x:
                    continue
                else:
                    if x+y==val:
                        listing=[]
                        listing.append(x)
                        listing.append(y)
                        print(listing)
                        if len(listing)==2:
                            count=1

                    else:continue
    if count==0:
        print("It is not possible to find such pair")
    pass


sum_pair([4,2,10,5,1], 100)