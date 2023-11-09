from tasks import task,task2,task3,task4,task5,task6,task7
import os 


def menu():
    while True:
        print("Press (1) for Task 1")
        print("Press (2) for Task 2")
        print("Press (3) for Task 3")
        print("Press (4) for Task 4")
        print("Press (5) for Task 5")
        print("Press (6) for Task 6")
        print("Press (7) for Answers on the questions")

        choice = input("\nChoose the task: \n")
        if choice == "1":
            task()
        elif choice =="2":
            task2()
        elif choice =="3":
            task3()
        elif choice =="4":
            task4()
        elif choice =="5":
            task5()
        elif choice =="6":
            task6()
        elif choice =="7":
            task7()
        


if __name__ == "__main__":
    menu()

