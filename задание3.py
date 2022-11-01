#O(1)
c = [1,2,3,4]
b = c[0]
print(b)

#O(logn)
def binary_search(lst,x):
    low=0 #начало отрезка, на котором ищется элемент
    high=len(lst)
    y=False
    c=0
    while low<=high and not y:
        middle=(low+high)//2 #средний элемент в массиве
        value=lst[middle]
        c+=1
        if value==x:
            y=True
            return y
        if value>x:
            high=middle-1
        else:
            low=middle+1
    return y

print(binary_search([14,12,5,32,17],5))

#O(n^2)
n = 3
for i in range(n):
    for j in range(n):
            print(i,j)
#O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
