n=int(input())
# print(n)
r1=list(map(str,input().split()))
# print(r1)
r2=list(map(str,input().split()))
# print(r2)
# results=list(map(int,input().split()))

match=0



for i in range (len(r1)):
  if r1[i] == r2[i]:
        match= match+1
        maxright=n+match
        print(maxright)
  else:
    if r1!=r:
      print(len(r2)-n)