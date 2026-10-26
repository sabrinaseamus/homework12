def custom_sort(arr):
    # Создаем копию, чтобы не менять исходный список
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    comparisons = 0  # Счетчик сравнений

    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1): # (n - i - 1), потому что после каждого прохода самый большой элемент "всплывает" в конец
            comparisons += 1  
            
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Меняем местами, если текущий больше следующего
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
                
        # Если обменов не было, значит список уже отсортирован — выходим
        if not swapped:
            break

    return sorted_arr, comparisons

# --- Тестирование ---
if __name__ == "__main__":
    short_list = [5, 1, 4, 2, 8]
    long_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    print("Test 1:")
    res_short, comp_short = custom_sort(short_list)
    print(f"Initial: {short_list}")
    print(f"Result: {res_short}")
    print(f"How many times comparison was: {comp_short}\n")

    print("Test 2:")
    res_long, comp_long = custom_sort(long_list)
    print(f"Initial: {long_list}")
    print(f"Result: {res_long}")
    print(f"How many times comparison was: {comp_long}")