A = list(map(int, input().split(' ')))  # ввести числа через пробел


def hoar_sort(A, level=1, part='left'): # для списка A, барьер - начальный элемент (я помню, что лучше рандом! но можно же)
    if len(A) > 1:
        barrier = A[0]
        left = []  # для тех, кто меньше барьера
        middle = []  # для равных
        right = []  # для больших
        for num in A:
            if num < barrier:
                left.append(num)
            elif num == barrier:
                middle.append(num)
            else:
                right.append(num)

        hoar_sort(left, level + 1)
        hoar_sort(right, level + 1, part='right')

        k = 0  # меняем исходный на отсортированный
        for x in left + middle + right:
            A[k] = x
            k += 1
    return A


print(hoar_sort(A))
