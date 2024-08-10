from collections import Counter


def intersection_of_two_lists(list1, list2):
    # Create counters for both lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # Find intersection of both counters
    intersection = []
    for element in counter1:
        if element in counter2:
            # Add the element the minimum number of times it appears in both lists
            intersection.extend([element] * min(counter1[element], counter2[element]))

    return intersection


def intersection_of_two_lists_dict(list1, list2):
    dict_intersection = {}

    for num in list1:
        if num in dict_intersection:
            dict_intersection[num] += dict_intersection[num]
        else:
            dict_intersection[num] = 1

    for num in list2:
        if num in dict_intersection:
            dict_intersection[num] -= dict_intersection[num]
        else:
            dict_intersection[num] = 1

    return dict_intersection

# Example usage:
list1 = [1, 2, 2, 1]
list2 = [2, 2]



result = intersection_of_two_lists(list1, list2)
print(result)  # Output should be [2, 2]

print(intersection_of_two_lists_dict(list1, list2))

def intersection_of_two_lists_dict(list1, list2):
    dict_intersection = {}

    # Count elements in list1
    for num in list1:
        if num in dict_intersection:
            dict_intersection[num] += 1
        else:
            dict_intersection[num] = 1

    intersection_result = []

    # Find intersection by comparing with list2
    for num in list2:
        if num in dict_intersection and dict_intersection[num] > 0:
            intersection_result.append(num)
            dict_intersection[num] -= 1

    return intersection_result

# Example usage:
list1 = [1, 2, 2, 1]
list2 = [2, 2]
result = intersection_of_two_lists_dict(list1, list2)
print(result)  # Output should be [2, 2]
