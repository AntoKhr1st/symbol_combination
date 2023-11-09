from itertools import product

digits = list(range(9, -1, -1))  # Создаем список цифр от 9 до 0
operators = ['+', '-', '']  # Возможные операторы

# Генерируем все возможные сочетания операторов между цифрами
expressions = product(operators, repeat=len(digits)-1)
for expression in expressions:
    # Собираем выражение вместе с цифрами
    expr = ''.join('{}{}'.format(digit, op) for digit, op in zip(digits, expression)) + str(digits[-1])
    # Вычисляем результат полученного выражения
    result = eval(expr)
    if result == 200:
        print(expr, '=', result)
