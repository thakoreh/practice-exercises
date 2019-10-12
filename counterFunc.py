'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(string):
    def counter(char):
        # self.string=string
        count=0
        for s in string.lower():
            if s==char:
                count=count+1
            else:
                continue
        print(count)
        return count
        pass

    return counter
    pass

counter = letter_counter('Amazing')
counter('a') # 2