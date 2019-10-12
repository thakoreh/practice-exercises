'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(listing):
    MaxNo=max(listing)
    listing.remove(MaxNo)
    SecondMax=max(listing)
    print(SecondMax,MaxNo)   
    pass

two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]