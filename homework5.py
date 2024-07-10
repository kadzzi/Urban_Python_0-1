immutable_var = ('jar', 15, False, ['cat', 'dog'])
print(f'Immutable tuple: {immutable_var}')
#immutable_var[1] = 16 # Вызвало ошибку. Кортеж - не изменяемый тип данных. TypeError: 'tuple' object does not support item assignment
immutable_var[3][0] = 'Very big dog!'
print(f'Mutable list inside tuple: {immutable_var}') # Получилось изменить, поскольку я обращался к списку внутри кортежа, а список - изменяемый тип данных.

mutable_list = ['boat', 'ship']
mutable_list.append('battleship')
mutable_list[1] = 'big ship'
print(f'Mutable list: {mutable_list}')

mutable_list.sort(key=len, reverse=True) #Сортировка по длине символов по убыванию
print(f'Sorted list: {mutable_list}')
