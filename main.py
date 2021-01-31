import time
from time import sleep


"""list_of_string = []
massive = []
massivetmp = []
str1 = ''
i_max = 0
j_max = 0
string = input()
if string == 'end':
    print('')
else:
    while string != "end":
        list_of_string.append(string)
        string = input()

    # print(list_of_string)

    for i, item in enumerate(list_of_string):
        massive.append(item.split())
        massivetmp.append(item.split())

    for i in range(len(massive)):
        for j in range(len(massive)):
            if j > j_max:
                j_max = j
        if i > i_max:
            i_max = i

    for i in range(len(massive)):
        for j in range(len(massive)):
            if i - 1 == -1:
                a = int(massive[i_max][j])
            else:
                a = int(massive[i - 1][j])
            if i + 1 == len(massive):
                b = int(massive[0][j])
            else:
                b = int(massive[i + 1][j])

            if j - 1 == -1:
                c = int(massive[i][j_max])
            else:
                c = int(massive[i][j - 1])
            if j + 1 == len(massive):
                d = int(massive[i][0])
            else:
                d = int(massive[i][j + 1])
            massivetmp[i][j] = int(a + b + c + d)

    # print(massivetmp)

    for i in range(len(massivetmp)):
        for j in range(len(massivetmp)):
            str1 = str1 + ' ' + str(massivetmp[i][j])
        str1 = str1 + '\n'
    print(str1)"""

"""d = {}
input_string = 'aabbgccdefddf'
for i, item in enumerate(input_string):
    here_more_then_one = False
    for j, itemj in enumerate(input_string):
        if j != i:
            if item == itemj:
                here_more_then_one = True
                break
    if not here_more_then_one:
        d.update({item:i})

for key, value in d.items():
    if min(d[key] for key in d) == value:
        print(key)"""

"""Написать декоратор, который принимает два параметра:
1. Количество секунд
2. Количество попыток
Декоратор вызывает функцию указанное число раз и ждет указанное время между каждым вызовом функции."""


"""def print_in_time(f, secs, count):
    def wrapper():
        for i in range(count):
            print('Идет выполнение функции {0}-й раз'.format(i+1))
            f()
            print('Ждем {0} секунд до следующего вызова функции\n'.format(secs))
            time.sleep(secs)
    return wrapper


def func():
    print("Выполнение функции")


func = print_in_time(func,3,10)
func()"""


"""def f(x):
    return x*2

d = {}
k = []
n = int(input())
for i in range(n):
    k.append(int(input()))
s = set(k)
for i,item in enumerate(s):
    d.update({item:f(item)})

for i,item in enumerate(k):
    for key,value in d.items():
        if item == key:
            print(value)"""


class User_comments:
    def __init__(self, user_id, comment_id):
        self._user_id = user_id
        self._comment_id=comment_id

    def print_user_id(self):
        return self._user_id

    def print_comment_id(self):
        return self._comment_id

users =[
    User_comments(1,1),
    User_comments(2,2),
    User_comments(3,3),
    User_comments(4,4),
    User_comments(5, 5),
    User_comments(1,6),
    User_comments(1, 7),
    User_comments(2, 8),
]

d = {}
for i,item in enumerate(users):
    comment_count = 0
    k = i.print_user_id()
    c = i.print_comment_id()
    for j, itemj in enumerate(users):
        k1 = j.print_user_id()
        c1 = i.print_comment_id()
        if k > k1 and k == k1:
            if c != c1:
                comment_count += 1
                d.update({k:comment_count})

print(d)
"""Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the"""