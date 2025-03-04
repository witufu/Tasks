import re


def skob(exp):
    return exp.count('(') == exp.count(')')


def decode(exp):
    stack = []
    i = 0

    while i < len(exp):
        if exp[i].isdigit():
            num_start = i
            while i + 1 < len(exp) and exp[i + 1].isdigit():
                i += 1
            stack.append(int(exp[num_start:i + 1]))
        elif exp[i] == '(':
            stack.append(exp[i])
        elif exp[i] == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()

            repeat = stack.pop() if stack and isinstance(stack[-1], int) else 1
            stack.append("".join(reversed(temp)) * repeat)
        else:
            stack.append(exp[i])
        i += 1

    return "".join(stack)


def main():
    while True:
        user_input = input("Введите закодированную строку: ").strip()
        if not skob(user_input):
            print("Ошибка: количество открывающих и закрывающих скобок не совпадает. Попробуйте снова.")
            continue

        try:
            result = decode(user_input)
            print("Расшифрованная строка:", result)
            break
        except Exception as e:
            print("Ошибка при декодировании:", e)
            continue


main()