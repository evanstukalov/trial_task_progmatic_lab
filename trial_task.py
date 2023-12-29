def insert_operators(num_str: str, operators: list, pos: int = 0) -> None:
    """
    :param num_str: str
    :param operators: list
    :param pos: int
    """
    # Если функция достигла 9-й позиции в списке operators (то есть разместила операторы между всеми цифрами в num_str),
    if pos == 9:
        # то формируется выражение
        expression = "".join([num_str[i] + operators[i] for i in range(9)] + [num_str[9]])
        # и если выражение при вычислении равно 200, то оно выводится на печать.
        if eval(expression) == 200:
            print(expression)
    else:
        # В противном случае для каждого оператора из ['+', '-', ''],
        for operator in ['+', '-', '']:
            # текущий оператор назначается на текущую позицию в operators,
            operators[pos] = operator
            # и функция вызывается рекурсивно для следующей позиции.
            insert_operators(num_str, operators, pos + 1)


# Создается строка чисел.
num_str = "9876543210"
# Создается список operators из 9 элементов, все изначально равны 0.
operators = [0] * 9
# Вызывается функция insert_operators с num_str и operators в качестве аргументов.
insert_operators(num_str, operators)
