import timeit

# Набір доступних номіналів монет
coins = [50, 25, 10, 5, 2, 1]


# Функція для знаходження кількості монет за жадібним алгоритмом
def find_coins_greedy(amount):
    
    result = {}
    for coin in coins:
        if amount >= coin:
            # Визначаємо кількість монет поточного номіналу
            result[coin] = amount // coin
            # Зменшуємо залишок суми
            amount %= coin
    return result

# Функція для знаходження мінімальної кількості монет за методом динамічного програмування.
def find_min_coins(amount):
    
    # Таблиця для зберігання мінімальної кількості монет для кожної суми
    min_coins = [0] + [float("inf")] * amount
    # Список для зберігання кількості монет кожного номіналу для кожної суми
    coin_count = [{} for _ in range(amount + 1)]

    for coin in coins:
        for x in range(coin, amount + 1):
            # Оновлюємо мінімальну кількість монет для поточної суми
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                # Копіюємо словник монет для поточної суми
                coin_count[x] = coin_count[x - coin].copy()
                # Додаємо поточну монету до результату
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1

    return coin_count[amount]


# Список сум для тестування
amounts = [7, 28, 57, 113, 227, 555, 1129, 2269]
# Список для зберігання результатів
results = []

# Тестуємо кожну суму
for amount in amounts:
    # Вимірюємо час виконання жадібного алгоритму
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    # Вимірюємо час виконання алгоритму динамічного програмування
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    # Додаємо результати до списку
    results.append([amount, time_greedy, time_dp])

# Виводимо результати
print("Сума     | Жадібний алгоритм, сек | Динамічне програмування, сек")
for result in results:
    print(f"{result[0]:>6}   | {result[1]:>14.8f}         | {result[2]:>12.8f}")
