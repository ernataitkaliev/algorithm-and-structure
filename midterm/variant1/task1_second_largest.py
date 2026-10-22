# Variant 1 - Task 1. Arrays - Find the Second Largest Element
def second_largest(arr):
    largest = None
    second = None
    for x in arr:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second

for data in ([12, 5, 8, 12, 9, 7], [5, 5, 5], [7]):
    result = second_largest(data)
    if result is None:
        print(data, "-> no second largest distinct element")
    else:
        print(data, "->", result)
