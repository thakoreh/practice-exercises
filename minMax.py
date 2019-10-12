# min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]

def min_max_key_in_dictionary(dictionary):
    listing=[]
    Maximum=max(dictionary.keys())
    Minimum=min(dictionary.keys())
    listing.append(Maximum)
    listing.append(Minimum)
    listing=sorted(listing)
    print(listing)
    pass

min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})