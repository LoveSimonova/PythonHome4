N=int(input("Введите количество кустов: "))
max=0
list1=list()
for i in range(N):
    k=int(input("количество ягод: "))
    list1.append(k)
max1=list1[0]+list1[N-1]+list1[N-2]
max2=list1[0]+list1[N-1]+list1[1]
max0n=0
if max1>max2:
    max0n=max1
else:
    max0n=max2
for i in range(N-2):
    if (list1[i]+list1[i+1]+list1[i+2])>max:
        max=list1[i]+list1[i+1]+list1[i+2]
if max0n>max:
    print(max0n)
else:
    print(max)