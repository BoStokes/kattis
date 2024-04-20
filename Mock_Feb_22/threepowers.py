while True:
  num = int(input())
  if num == 0:
    break
  print("{ ", end='')

  nums = []
  num-=1
  currPow = 0
  while num>0:
    if num&1==1:
      nums.append(str(3**currPow))
    currPow+=1
    num>>=1
  
  print(', '.join(nums), end='')
  print(' }')

'''
  nums = []
  i = 2
  j = 1
  while i < num:
    m = num % i
    if m == 0 or m >= i/2:
      nums.append(str(3 ** (j)))
    i *= 2
    j += 1
  '''
  

'''
_
1
3
1, 3
9
1, 9
3, 9
1, 3, 9
27
1, 27
3, 27
1, 3, 27
9, 27
1, 9, 27
'''

