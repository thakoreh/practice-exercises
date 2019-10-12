def sum_up_diagonals(lst):
    lr, lc = len(lst), len(lst[0])
    if lr == lc:
        diagsum_1 = sum(lst[r][c] for r in range(0,lr) for c in range(0,lc) if r == c)
        diagsum_2 = sum(lst[r][c] for r in range(0,lr) for c in range(0,lc) if r == lc - c - 1)
        return diagsum_1 + diagsum_2

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
sum_up_diagonals(list1)


 
# sum_up_diagonals(list1) # 10