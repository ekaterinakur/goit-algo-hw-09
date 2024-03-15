import timeit
from algorithms import find_coins_greedy, find_min_coins

def measure_time(search_function, amount):
    return timeit.timeit(lambda: search_function(amount), number=100)

def is_number(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False 

if __name__ == "__main__":
    amount = None

    while True:
        input_string = input("Введіть суму: ")
        if is_number(input_string):
            amount = int(input_string)
            break
        else:
            print("Сума має бути числом!")

    greedy_result = find_coins_greedy(amount)
    dynamic_result = find_min_coins(amount)

    greedy_time = measure_time(find_coins_greedy, amount)
    dynamic_time = measure_time(find_min_coins, amount)

    print('\n')
    print(f"Середній час виконання (сек) для суми {amount}")
    print(f"{'-'*80}")
    print(f"{'Aлгоритм':^35} | {'Час виконання':^13} | {'Результат':^}")
    print(f"{'-'*80}")
    print(f"{'Жадібний алгоритм':<35} | {greedy_time / 100:^13.10f} | {str(greedy_result)}")
    print(f"{'Алгоритм динамічного програмування':<35} | {dynamic_time / 100:^13.10f} | {str(dynamic_result)}")
    print('\n')
