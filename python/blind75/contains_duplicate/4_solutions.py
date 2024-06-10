# time complexity O(n2)
def contains_duplicate_bf(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

list_without_duplicates = [1,5,3,6,2,77]
list_with_duplicates = [1,5,3,6,2,77,4,3,2]

print(contains_duplicate_bf(list_without_duplicates))
print(contains_duplicate_bf(list_with_duplicates))

#time complexy O(nlogn)
def contains_duplicate_sort(numbers):
    numbers.sort()
    for i in range(1,len(numbers)):
        if numbers[i-1] == numbers[i]:
            return True
    return False


print(contains_duplicate_sort(list_without_duplicates))
print(contains_duplicate_sort(list_with_duplicates))

# def contains_duplicate_hashmap(numbers)

