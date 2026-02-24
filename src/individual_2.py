#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    students = []

    while True:
        command = input(">>> ").strip().lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы студента: ")
            group = input("Номер группы: ")
            grades_list = input("Успеваемость (5 оценок через пробел): ").split()

            grades = []
            error = False
            for i in range(5):
                try:
                    grade = int(grades_list[i])
                    if grade < 1 or grade > 5:
                        print("\nОшибка: неправильный формат данных", file=sys.stderr)
                        error = True
                        break
                    grades.append(grade)
                except ValueError:
                    print("\nОшибка: неправильный тип данных", file=sys.stderr)
                    error = True
                    break

            if len(grades) < 5:
                print("\nОшибка: неправильное количество оценок", file=sys.stderr)
                error = True

            student = {
                'name': name,
                'group': group,
                'grades': grades
            }
            if not error:
                students.append(student)

        elif command == 'list':
            if len(students) > 1:
                students.sort(key=lambda item: sum(item.get('grades')) / len(item.get('grades')), reverse=True)

            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 20,
                '-' * 15,
                '-' * 12
            )
            print(line)
            print(
                '| {:^20} | {:^15} | {:^12} |'.format(
                    "Фамилия и инициалы",
                    "Номер группы",
                    "Успеваемость"
                )
            )
            print(line)

            for student in students:
                print(
                    '| {:<20} | {:<15} | {:>12} |'.format(
                        student.get('name', ''),
                        student.get('group', ''),
                        ' '.join(map(str, student.get('grades', [])))
                    )
                )

            print(line)

        elif command == 'select':
            count = 0
            for student in students:
                grades = student.get('grades', [])
                if 4 in grades or 5 in grades:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, student.get('name', ''))
                    )


        elif command == 'help':
            print("\nСписок команд:")
            print("add - добавить студента")
            print("list - вывести список студентов")
            print("select - запросить студентов с оценкой 4 или 5")
            print("help - отобразить справку")
            print("exit - завершить работу с программой\n")
        else:
            print(f"Неизвестная команда '{command}'", file=sys.stderr)
            print("Введите 'help' для списка команд")