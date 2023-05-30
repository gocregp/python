
# x = 50
#
#
# def func(x):
#     print('x равен', x)
#     x = 2
#     print('Замена локального x на', x)
#
#
# func(x)
# print('x по-прежнему', x)
# xy = 1
# print(f'xy = {xy}')
# def func_outer():
#
#     xy = 2
#     print('xy local outher равно', xy)
#
#     def func_inner():
#         nonlocal xy
#         xy = 5
#         print('x inner равно', xy)
#     func_inner()
#     print(' xy сменилось на', xy)
#
#     print(' xy outher сменилось на', xy)
#
# func_outer()
# print(' xy сменилось на', xy)


# def total(a, car='opel', *numbers, **phonebook):
#     print('a', a)
#     print('Машина', car)
#     print('-' * 50)
#
#     # проход по всем элементам кортежа
#     for item in numbers:
#         print('Элемент - ', item)
#     print('-' * 50)
#
#     # проход по всем элементам словаря
#     for k, v in phonebook.items():
#         print(f'Тел книга: {k} - {v}')
#     print('-' * 50)

# total(10, 1, 2, 3, 'BMW', Jack=1123, John=2231, Inge=1560)


def factor(n):
    if n != 0:
        return n * (factor(n - 1))
    else:
        return 1
print(factor(5))
