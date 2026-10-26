def custom_sort(arr):
    result = arr.copy()
    comparisons = 0

    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            comparisons += 1  # Count comparisons

            if result[j] > result[j + 1]:
                # Swap elements if they are in the wrong order
                result[j], result[j + 1] = result[j + 1], result[j]

    return result, comparisons