import itertools


#O(3n)
def f(n):
    b = 0
    if n > 0:
        b += n*2
    return b
print(f(1),f(1),f(1))

#O(nlogn)
def merge(left_list, right_list):
    sorted_list = []
    lindex = rindex = 0
    llen, rlen = len(left_list), len(right_list)

    for _ in range(llen + rlen):
        if lindex < llen and rindex < rlen: # Сравниваем первые элементы в начале каждого списка
            if left_list[lindex] <= right_list[rindex]: # Если первый элемент левого подсписка меньше, добавляем его в отсортированный массив
                sorted_list.append(left_list[lindex])
                lindex += 1
            else: # Если первый элемент правого подсписка меньше, добавляем его в отсортированный массив
                sorted_list.append(right_list[rindex])
                rindex += 1
        elif lindex == llen: # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
            sorted_list.append(right_list[rindex])
            rindex += 1
        elif rindex == rlen: # Если достигнут конец правого списка, элементы левого списка добавляем в отсортированный массив
            sorted_list.append(left_list[lindex])
            lindex += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1: # Возвращаем список, если он состоит из одного элемента
        return nums

    mid = len(nums) // 2 # Для того чтобы найти середину списка, используем деление без остатка
    left_list = merge_sort(nums[:mid]) # Сортируем и объединяем подсписки
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list) # Объединяем отсортированные списки в результирующий

# Проверка
a = [60, 13, 34, 470, 135]
a = merge_sort(a)
print(a)

#O(n!)
print(list(itertools.permutations([1,2,3,4], 3)))

#O(n^3)
n = 10
for i in range(n):
    for j in range(n):
        for r in range(n):
            print(i,j,r)

# O(3log(n))
c = 0
m=10
while m > 0:
    m = m // 2
    c += 1 + m % 2
print(c)
