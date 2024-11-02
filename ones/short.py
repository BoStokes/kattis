import sys
for n in(int(s.strip())for s in sys.stdin.readlines()):
 a=1;d=1
 while a%n>0:a=a%n*10+1;d+=1
 print(d)