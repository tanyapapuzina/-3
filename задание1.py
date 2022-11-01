n=int(input("Введите нужное кол-во чисел:"))
a=[]
k = 0
for i in range(n):
    a.append(int(input()))
print(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
