# Задачи по Python
Этот репозиторий содержит три задачи, их описание, алгоритм и пример вводов и выводов.

## Требования
- Python 3.8+

## Задача 1: Нахождение простых чисел в заданном диапазоне

### Описание:

Задача, которая находит все простые числа в указанном диапазоне с использованием алгоритма решета Эратосфена.

**Алгоритм:**
1. Для каждого числа от 2 до корня из максимального числа отмечаем его как простое или составное.
2. Все составные числа, кратные этому числу, исключаем из списка.
3. В результате остаются только простые числа.

### Пример:
Вход: `1, 30`  
Выход: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`
---

## Задача 2: Декодирование строки

### Описание:

Программа для декодирования строки, закодированной с использованием повторений символов.

**Алгоритм:**
1. Программа находит число перед скобками.
2. Программа извлекает символы внутри скобок, и, учитывая найденные коэффициенты, повторяет символы указанное количество раз.
3. Программа меняет закодированную часть строки на расшифрованную.

### Пример:
Вход: `3(в)2(лп)`  
Выход: `вввлплп`
---

## Задача 3: "Угадай число"

### Описание:

Игра, где пользователь загадывает число, а программа его угадывает с помощью бинарного поиска.

**Принцип работы:**
1. Компьютер выбирает середину диапазона и спрашивает, больше ли ваше число.
2. В зависимости от вашего ответа, диапазон сужается, и компьютер делает новые попытки.
3. Алгоритм бинарного поиска позволяет с минимальными шагами угадать число за несколько попыток.

### Пример диалога:
 
Загадайте любое число от 0 до 1000.
Больше ли ваше число чем 500? (да/нет): да
Больше ли ваше число чем 750? (да/нет): нет
Больше ли ваше число чем 625? (да/нет): да
Больше ли ваше число чем 688? (да/нет): да
Больше ли ваше число чем 719? (да/нет): да
Больше ли ваше число чем 735? (да/нет): нет
Больше ли ваше число чем 727? (да/нет): нет
Больше ли ваше число чем 723? (да/нет): нет
Больше ли ваше число чем 721? (да/нет): да
Больше ли ваше число чем 722? (да/нет): да
Вы загадали число 723!

