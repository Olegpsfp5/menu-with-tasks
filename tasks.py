import math

def task():
    n = 18
    m = 3
    d = 15
    print(123 / d + 45 * m - 66 * (3 + n))
    input("Press Enter to leave")

def task2():
    n = 18
    print(2.3 + 106 * n)
    input("Press Enter to leave")

def task3():
    side1 = int(input("Enter 1st side: "))
    side2 = int(input("Enter 2nd side: "))
    side3 = int(input("Enter 3rd side: "))
    p = (side1 + side2 + side3) / 2
    result = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
    print(f"\nResult: {result}\n")
    input("Press Enter to leave")

def task4():
    print("Calculation of the area of ​​a right triangle\n\n")
    katet1 = float(input('Enter the length of the first leg in cm: \n'))
    katet2 = float(input('Enter the length of the second leg in cm: \n'))
    result = (katet1**2) + (katet2**2)
    p = result ** 0.5
    print(f"\nArea of right triangle: {p}")
    input("\nPress Enter to leave.\n")

def task5():
    print("Area of a circle")
    side1 = int(input("Enter 1st side: "))
    side2 = int(input("Enter 2nd side: "))
    side3 = int(input("Enter 3rd side: "))
    p = (side1 + side2 + side3) / 2
    result = round((p * (p - side1) * (p - side2) * (p - side3)) ** 0.5)
    r = int(input("Enter area of a circle:"))
    P = math.pi
    circlearea = round(2 * r * P)
    areacircle = round(r - result)
    print(f"Area of a triangle: {result}")
    print(f"Area of a circle: {circlearea}")
    print(f"Final area of a circle: {areacircle}")
    input("\nPress Enter to leave.\n")

def task6():
    print("Area of a triangle")
    side1 = int(input("Enter 1st side: "))
    side2 = int(input("Enter 2nd side: "))
    side3 = int(input("Enter 3rd side: "))
    p = (side1 + side2 + side3) / 2
    result = round((p * (p - side1) * (p - side2) * (p - side3)) ** 0.5)
    r = int(input("Enter area of a circle:"))
    P = math.pi
    circlearea = round(2 * r * P)
    areatriangle = round(result - r)
    print(f"Triangle Area: {result}")
    print(f"Circle Area: {circlearea}")
    print(f"Final area of a triangle:{areatriangle}")
    input("\nPress Enter to leave.\n")

def task7():
    tasks = {
        "question1": """\nЯкі переваги мають інтегрованісередовища програмування?""",
        "answer1": """Зручний інтерфейс: ІСП зазвичай надають зручний інтерфейс, що об'єднує різні елементи, такі як текстовий редактор, консоль виконання коду, дебагер і т.д. в єдиному середовищі.
Автоматизація задач: ІСП можуть надавати автоматизацію для багатьох аспектів розробки, таких як виправлення помилок, виконання тестів, підказки коду тощо.
Дебагінг і профілювання: Багато ІСП включають в себе зручні інструменти для дебагінгу, що полегшує виявлення та виправлення помилок у програмному коді. Також можуть бути вбудовані інструменти для профілювання продуктивності коду.""",
        "question2": "\nЯк класифікуються мови програмування за орієнтацією на клас задач?",
        "answer2": """Мови загального використання (General-purpose languages): Це мови, які призначені для вирішення різноманітних завдань. Приклади включають Python, Java, C++.
Мови спеціального призначення (Domain-specific languages - DSL): Це мови, які спеціально розроблені для вирішення конкретного класу завдань або задач у певній області. Приклади включають SQL для роботи з базами даних, HTML для веб-розробки."""
    }

    while True:
        try:
            print("\nQuestions and Answers: \n")
            print("\nPress (0) to leave")
            choose = input("Press 1/2 for questions and answers: ")
            

            if choose == "1":
                print(tasks["question1"])
                input("\nPress Enter to see the answer:\n")
                print(tasks["answer1"])
            elif choose == "2":
                print(tasks["question2"])
                input("\nPress Enter to see the answer:\n")
                print(tasks["answer2"])
            elif choose == "0":
                break
        except KeyError:
            print("Task not found")