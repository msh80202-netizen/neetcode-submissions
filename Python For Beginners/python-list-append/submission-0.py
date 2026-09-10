from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    i = 0
    length = len(elements)
    for i in range(length):
        my_list.append(elements[i])
        i += 1
    return my_list



# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
