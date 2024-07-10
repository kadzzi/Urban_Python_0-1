my_dict = {'James': 1985, 'Igor': 1991, 'Mia': 2000}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Igor')}')
print(f'Not existing value: {my_dict.get('Liz')}')
my_dict.update({'JoJo': 1914, 'Samura': 1959})
print(f'Deleted value: {my_dict.pop('JoJo')}')
print(f'Modified dictionary: {my_dict}\n')

my_set = {'cat', 157, 'dodo', 168, 'cat', 157}
print(f'Set: {my_set}')
my_set.update({'Polly', 84})
my_set.remove('dodo')
print(f'Modified set: {my_set}')
