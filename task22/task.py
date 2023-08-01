n=int(input("Введите первое количество элементов: "))
m=int(input("Введите второе количество элементов: "))
list1=set()
list2=set()
for i in range(n):
    k=int(input("элемент 1-го набора чисел: "))
    list1.add(k)
for i in range(m):
    k=int(input("элемент 2-го набора чисел: "))
    list2.add(k)
alllist=list1.union(list2)
l=list()
l.append(alllist)
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]>l[j]:
            a=l[j]
            l[j]=l[i]
            l[i]=a
for i in range(len(l)):
    print(l[i], " ")