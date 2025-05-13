N=int(input())
p=2
while 1:
  if N==1: break
  if N%p: p+=1
  else: print(p); N//=p