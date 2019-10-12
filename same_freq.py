def same_freq(string1,string2):
    
    listing=  [char for char in string1]
    countLetter={}
    countLetter1={}
    for char in string1:
        elem=listing.count(char)
        countLetter.update({char:elem})
    # print(countLetter)
    listing2=[char for char in string2]
    for char in string2:
        elem=listing2.count(char)
        countLetter1.update({char:elem})

    if countLetter==countLetter1:
        return True
    else:
        return False
    pass

print(same_freq('abcasd','dsacba'))