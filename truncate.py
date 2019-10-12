def truncate(string,val):
    logic='...'
    if val>=3 and not len(string)<val:
        val=val-3
        string=string[:val]
        finalstring=string+logic
        print(finalstring)
    elif len(string)<val:
        print(string)
    else:
        print("Truncation must be at least 3 characters.")
    pass

truncate('askjdasda',2)
truncate('askjdasda',106)


