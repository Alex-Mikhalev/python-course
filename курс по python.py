print('базовые структуры данных')
print(5) #базовые структуры данных
print(type(5)) #int - integer
print(50 % 3)
print(type(2.0))
print(2.0 ** 2.0)
print(type('hello, world!'))
print('"hello world!"')
print('hello, ' + 'world!') # concatenate
print('1' + '1')
print(5 > 10, 10 > 5)
print(1, 2, 3, 4, 5, "hello world", True)
print(5 != 5 and 5 < 10)
print(5 == 5 or 5 > 10)
print(type(int('5'))) # принудительно перевести в другой класс
print('строки и индексация')

name = 'Alex'#строки и индексация
print('hello ' + name * 5)
print('hello ' * 5)
print(name[0:3])
print(name[-1])
print(name[0:3:2])
print(name[:3])
print(name[2:])
print(name[::-1])

print('переменные')
name = 'Alex' #переменные
print(name)
name = 'Banman'
print(name)
date_of_birth = "10 july" #Snake case
dateOfBirth = '10 july' #Camel case

print('динамическая типизация')
name = 'urban' #динамическая типизация
print(name, type(name))
name = 5
print(name, type(name))
name = 5.5
print(name, type(name))
name = [1, 2]
print(name, type(name))
age = 30
new_age = '30'
print(age + int(new_age))

print('организация программ и методы строк')
# name = input("Введите Ваше имя:") #организация программ и методы строк
# current_yaer = 2024
# data_of_birch = int(input('В каком году Вы родились? '))
# age = current_yaer - data_of_birch
# print("Здравствуйте,",name)
# print("В этом году Вам ", age, "лет")
#
# name = input("Введите Ваше имя:") #организация программ и методы строк
# current_yaer = 2024
# data_of_birch = input('В каком году Вы родились? ')
# age = current_yaer - int(data_of_birch)11
# print("Здравствуйте,",name)
# print("В этом году Вам ", age, "лет")

print('привет, я строка в нижнем регистре' .upper())
print("привет, я строка в верхнем регистре" .lower())
print('привет, я строка в нижнем регистре' .replace('привет',  "пока"))

print('Списки. Индексация и методы списков.')
food = ['apple', 'coconut', 'banana']
print(food[0])
food = ['apple', 'coconut', 'banana']
food[0] = 'peach'
print(food)
food.append(True) #добавить элемент в список
print(food)
food.extend(['string', 2]) #добавить элементы в список
print(food)
print('coconut' in food) #для проверки элемента в списке
print('coconut' not in food) #для проверки отсутствия элемента в списке
food = ['apple', 'coconut', 'banana']
food.remove('apple') #убрать элемент из списка
print(food)
print(food[0:2:2]) #использования срезов элементов в списке

print('Изменяемые и неизменяемые объекты. Кортежи.')
tuple_ = 1, 2, 3, 4
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple([1, 2, 3, 4])
tuple_4 = 1, 2, 3, True, "string"
print(type(tuple_))
print(tuple_2)
print(tuple_3)
print(tuple_4)
list_ = [1, 2, 3, True, "string"]
print(tuple_4.__sizeof__())
print(list_.__sizeof__())
tuple_5 = ([1, 2], 0) + (1, 2)
print(tuple_5)
tuple_5[0][0] = 3
print(tuple_5)
tuple_6 = (1, 2) * 3
print(tuple_6)

print('словари и множества') #словари
phone_book = {'Denis': 88005555757, 'Max': 89898898998}
print(phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 1234567890
phone_book['Anton'] = 3333333333
del phone_book['Max']
phone_book.update({'Sasha': 7575575775, 'Misha': 9859589526})
print(phone_book.get('Denis'))
print(phone_book.get('Kamila'))
print(phone_book.get('Kamila', 'Такого ключа нет'))
print(phone_book)
phone_book.pop('Anton')
print(phone_book)
a = phone_book.pop('Sasha')
print(a)
list_ = [1, 2, 3]
list_.pop(0)
print(list_)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'string', True, (1, 2, 3)} #множества
print(set_)
list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# print(set(list_))
# print(list_)
list_ = set(list_)
print(list_)
print(list_.discard(5))
print(list_)
print(list_.remove(1))
print(list_.add(5))
print(list_)

