# persons = {
#     'Игорь': {
#         'возраст': 49,
#         'рост': 173,
#         'вес': 95,
#         'велосипед': 'Merida'
#     },
#     'Митя': {
#         'возраст': 11,
#         'рост': 160,
#         'вес': 65,
#         'велосипед': 'Denna'
#     }
# }
# for userName, userInfo in persons.items():
#     age = userInfo['возраст']
#     circle = userInfo['велосипед']
#     print(f'Имя пользователя {userName}, возраст {age}, велосипед {circle}')
# person = {
#     'имя': 'Виктор',
#     'len': 175
# }
# print(person)
# print(persons.get("Митяq", 'нет такого'))
# print(person.setdefault('приправа', "magic"))
# print(person)
# person_copy = person.copy()
# print(person_copy)
# person.update({'профессия': 'слесарь-сантехник'})
# person.update({'стаж': '10 лет'})
# print(person)
# print(person.pop('професс', 'No Key'))
# print(person)
# print(person.popitem())
# print(person)

# persons = {
#     'Игорь': {
#         'Возраст': 49,
#         'Профессия': 'слесарь'
#     },
#     'Mitya': {
#         'Возраст': 12,
#         'Профессия': 'школьник'
#     }
# }
#
# for name, info in persons.items():
#     print(f"Мое имя {name}")
#     age = info['Возраст']
#     prof = info['Профессия']
#
# print(f"возраст {name} :{age} лет, профессия{prof}")
test_dict = {
    'вес': 100,
    'цвет': 'синий',
    'кол-во': 222
}
# print(test_dict.get('цветы', 'error'))
print(test_dict.setdefault('цена', 44))
print(test_dict)

# test_dict_copy = test_dict.copy()
# print(test_dict_copy)
test_dict.update({'made in': 'russia'})
print(test_dict)
print(test_dict.pop('made in'))
print(test_dict.pop('made in', 'No key'))
test_dict.update({'made in': 'russia'})
print(test_dict)
# print(test_dict.popitem())
# print(test_dict.popitem())
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())
# test_dict.clear()
print(test_dict)
# del test_dict['цена']
print(test_dict)