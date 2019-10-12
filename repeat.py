def repeat(string,count):
    listing=[]
    while count>0:
        listing.append(string)
        count=count-1
    print(''.join(listing))

    pass

repeat('x',3)
repeat('abc',4)