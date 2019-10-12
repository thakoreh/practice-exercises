# find_greater_numbers([6,1,2,7]) # 4
# find_greater_numbers([5,4,3,2,1]) # 0
# find_greater_numbers([]) # 0


def find_greater_numbers(listing):
    maxNum=max(listing)
    count=0
    for index,item in enumerate(listing):
        
        print(index,item)
        # if i<maxNum:
        #     count=count+1
    pass
find_greater_numbers([4,5,6]) # 3 