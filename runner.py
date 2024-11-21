import os

def run_lab1():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab1\\calculator.py')

def run_lab2():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab2\\main.py')

def run_lab3():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab3\\ASCII.py')

def run_lab4():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab4\\ASCII-2D.py')

def run_lab5():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab5\\main.py')

def run_lab6():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab6\\main.py')

def run_lab7():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab7\\api.py')

def run_lab8():
    os.system('python c:\\3.1\\СМП\\Lab9\\Lab8\\main.py')

def main():
    while True:
        print("\nВиберіть лабораторну роботу для запуску:")
        print("1. Лабораторна робота 1")
        print("2. Лабораторна робота 2")
        print("3. Лабораторна робота 3")
        print("4. Лабораторна робота 4")
        print("5. Лабораторна робота 5")
        print("6. Лабораторна робота 6")
        print("7. Лабораторна робота 7")
        print("8. Лабораторна робота 8")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            run_lab1()
        elif choice == '2':
            run_lab2()
        elif choice == '3':
            run_lab3()
        elif choice == '4':
            run_lab4()
        elif choice == '5':
            run_lab5()
        elif choice == '6':
            run_lab6()
        elif choice == '7':
            run_lab7()
        elif choice == '8':
            run_lab8()
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()