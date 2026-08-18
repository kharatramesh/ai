def find_max(arr):
    return max(arr)


def find_min(arr):
    return min(arr)


def sum_array(arr):
    return sum(arr)


def average(arr):
    return sum(arr) / len(arr) if arr else 0


def reverse_array(arr):
    return arr[::-1]


def sort_array(arr, descending=False):
    return sorted(arr, reverse=descending)


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 9, 2, 7]

    print(f"Array: {numbers}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    print(f"Sum: {sum_array(numbers)}")
    print(f"Average: {average(numbers)}")
    print(f"Reversed: {reverse_array(numbers)}")
    print(f"Sorted ascending: {sort_array(numbers)}")
    print(f"Sorted descending: {sort_array(numbers, descending=True)}")

    target = 8
    index = linear_search(numbers, target)
    print(f"Index of {target}: {index}")
