print("Підсумкове завдання з курсу 'Python Core' Олени Ляхович, вересень 2020 рік.")
print("Симулятор контрольної роботи з математики для початкових класів. Арифметичні дії.")
print("***")

import random

def base_arithmetic_operation():
    x = True
    while x:

        arithmetic_operations = (input("Оберіть математичну операцію, яку ви хочете виконати: + або - або * або /  --->  "))
        number_of_examples = int(input("На скількох прикладах Ви бажаєте потренуватись? "))
        great_mathematicians = ['Евклід? =)', 'Піфагор? =)', 'Архімед? =)', 'Рене Декарт? =)', \
    'Карл Фрідріх Гаусс? =)', 'Леонард Ейлер? =)', 'Карл Густав Якоб Якобі? =)', 'Бернхард Риман? =)', \
    'Жозеф-Луї Лагранж? =)', 'Готфрід Вільгельм Ляйбніц? =)', 'Ісаак Ньютон? =)', 'Ендрю Джон Уайлс? =)']


        if arithmetic_operations == '+':
            number_of_correct_answers_2 = 0
            number_of_wrong_answers_2 = 0

            for x in range (number_of_examples):
                first_digit = random.randint (1, 100)
                second_digit = random.randint (1, 100)
                correct_answer = first_digit + second_digit
                print ("Скільки буде, якщо", first_digit ,"+", second_digit,"?")
                user_response = int(input("Ваша відповідь:  " ))
                who_user = random.choice(great_mathematicians)
                if user_response == correct_answer:
                    print("Так, правильно! А ви часом не", who_user)
                    number_of_correct_answers_2 += 1
                if user_response != correct_answer:
                    print("Упс, неправильно =( Насправді вираз дорівнює", correct_answer )
                    number_of_wrong_answers_2 += 1

            print("У вас", number_of_correct_answers_2, "правильних та", number_of_wrong_answers_2, "неправильних відповідей.")

            percent = number_of_correct_answers_2 / number_of_examples * 100
            print(int(percent),"% зі 100 можливих!")
            # if percent >= 90:
            #     print("Ваша оцінка 5!")
            # elif percent >= 80:
            #     print("Ваша оцінка 4!")
            # elif percent >= 70:
            #     print("Ваша оцінка 3!")
            # elif percent >= 60:
            #     print("Ваша оцінка 2!")
            # else:
            #     print("Ваша оцінка 1!")

        if arithmetic_operations == '*':
                number_of_correct_answers_4 = 0
                number_of_wrong_answers_4 = 0

                for x in range (number_of_examples):
                    first_digit = random.randint (1, 20)
                    second_digit = random.randint (1, 20)
                    correct_answer = first_digit * second_digit
                    print ("Скільки буде, якщо", first_digit ,"*", second_digit,"?")
                    user_response = int(input("Ваша відповідь:  " ))
                    who_user = random.choice(great_mathematicians)
                    if user_response == correct_answer:
                        print("Так, правильно! А ви часом не", who_user)
                        number_of_correct_answers_4 += 1
                    if user_response != correct_answer:
                        print("Упс, неправильно =( Насправді вираз дорівнює", correct_answer )
                        number_of_wrong_answers_4 += 1

                print("У вас", number_of_correct_answers_4, "правильних та", number_of_wrong_answers_4, "неправильних відповідей.")

                percent = number_of_correct_answers_4 / number_of_examples * 100
                print(int(percent),"% зі 100 можливих!")
                # if percent >= 90:
                #     print("Ваша оцінка 5!")
                # elif percent >= 80:
                #     print("Ваша оцінка 4!")
                # elif percent >= 70:
                #     print("Ваша оцінка 3!")
                # elif percent >= 60:
                #     print("Ваша оцінка 2!")
                # else:
                #     print("Ваша оцінка 1!")

        if arithmetic_operations == '-':
            number_of_correct_answers_3 = 0
            number_of_wrong_answers_3 = 0

            for x in range (number_of_examples):
                first_digit = random.randint (50, 100)
                second_digit = random.randint (1, 50)
                correct_answer = first_digit - second_digit
                print ("Скільки буде, якщо", first_digit ,"-", second_digit,"?")
                user_response = int(input("Ваша відповідь:  " ))
                who_user = random.choice(great_mathematicians)
                if user_response == correct_answer:
                    print("Так, правильно! А ви часом не", who_user)
                    number_of_correct_answers_3 += 1
                if user_response != correct_answer:
                    print("Упс, неправильно =( Насправді вираз дорівнює", correct_answer )
                    number_of_wrong_answers_3 += 1

            print("У вас", number_of_correct_answers_3, "правильних та", number_of_wrong_answers_3, "неправильних відповідей.")

            percent = number_of_correct_answers_3 / number_of_examples * 100
            print(int(percent),"% зі 100 можливих!")
            # if percent >= 90:
            #     print("Ваша оцінка 5!")
            # elif percent >= 80:
            #     print("Ваша оцінка 4!")
            # elif percent >= 70:
            #     print("Ваша оцінка 3!")
            # elif percent >= 60:
            #     print("Ваша оцінка 2!")
            # else:
            #     print("Ваша оцінка 1!")

        if arithmetic_operations == '/':
            number_of_correct_answers_1 = 0
            number_of_wrong_answers_1 = 0
            for x in range (number_of_examples):
                first_digit = random.randint (50, 100)
                second_digit = random.randint (1, 50)
                correct_answer = round(first_digit / second_digit, 1)
                print ("Скільки буде, якщо", first_digit ,"/", second_digit, "? (округліть до десятих)")
                user_response = round(float(input("Ваша відповідь: " )),1)
                who_user = random.choice(great_mathematicians)
                if user_response == correct_answer:
                    print("Так, правильно! А ви часом не", who_user)
                    number_of_correct_answers_1 += 1
                if user_response != correct_answer:
                    print("Упс, неправильно =( Насправді вираз дорівнює", correct_answer )
                    number_of_wrong_answers_1 += 1
            print("У вас", number_of_correct_answers_1, "правильних та", number_of_wrong_answers_1, "неправильних відповідей.")
            percent = number_of_correct_answers_1 / number_of_examples * 100
            print(int(percent),"% зі 100 можливих!")
            # if percent >= 90:
            #     print("Ваша оцінка 5!")
            # elif percent >= 80:
            #     print("Ваша оцінка 4!")
            # elif percent >= 70:
            #     print("Ваша оцінка 3!")
            # elif percent >= 60:
            #     print("Ваша оцінка 2!")
            # else:
            #     print("Ваша оцінка 1!")


try:
    base_arithmetic_operation()
except (TypeError, ValueError):
    print('Ви ввели некоректний тип даних. Спробуйте ввести числову відповідь ще раз.')
