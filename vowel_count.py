def vowel_count(string):
    listing=['a','e','i','o','u']
    letters=[]
    string=string.lower()
    for char in string:
        if char in listing:
            letters.append(char)
    letterCount={}
    for item in letters:
        if item in set(letters):
            letterCount.update({item:letters.count(item)})
    return letterCount

print(vowel_count('weiudhasjhh9dhdsdwoieowe9wefwheifwheffuhweifhwefhiwuefwieufhwiefWIEUH'))