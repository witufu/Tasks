def binary_search_game():
    print("Загадайте любое число от 0 до 1000.")
    lowest_number = 0
    highest_number = 1000

    while lowest_number < highest_number:
        mid = (lowest_number + highest_number) // 2
        while True:
            response = input(f"Больше ли ваше число чем {mid}? (да/нет): ").strip().lower()
            if response in ['да', 'нет']:
                break
            print("Пожалуйста, введите 'да' или 'нет'.")

        if response == "да":
            lowest_number = mid + 1
        else:
            highest_number = mid

    print(f'Вы загадали число {lowest_number}!')

binary_search_game()
            