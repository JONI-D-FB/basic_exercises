# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names: 
    print(i, end='\n')


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(f'{i}: {len(i)}', end='\n')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in is_male:
    print(f'{i}: {is_male[i]}')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]


len_dict = len(groups)
group_numbers=[]

t_p = len_dict

while t_p > 0 :
    group_numbers.append(t_p)
    t_p=t_p-1

group_numbers.reverse()
#print(new_dict)

general_dict=dict(zip(group_numbers,groups))
#print(general_dict)

print(f'Всего {len_dict} группы.', end='\n')
for i in group_numbers:
    print(f'Группа {i}: {len(general_dict[i])} ученика')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

len_dict = len(groups)
group_numbers=[]

t_p = len_dict

while t_p > 0 :
    group_numbers.append(t_p)
    t_p=t_p-1

group_numbers.reverse()
#print(new_dict)

general_dict=dict(zip(group_numbers,groups))
#print(general_dict)

#a=tuple(general_dict[1])
#print(a)

print(f'Всего {len_dict} группы.', end='\n')
for i in group_numbers:
    print(f'Группа {i}: {general_dict[i]} ')

