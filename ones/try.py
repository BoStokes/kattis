try:
 while 1:
  n=int(input())
  a=1;d=1
  while a%n>0:a=a%n*10+1;d+=1
  print(d)
except:a