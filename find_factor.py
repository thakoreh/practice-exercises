

def find_factor(num):
    listOfindex=[]
    for index in (range(1,num+1)):
        if (num%index) ==0:
            listOfindex.append(index)
        else:
                continue
    return(listOfindex)

print(find_factor(321421))