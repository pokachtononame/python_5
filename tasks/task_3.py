#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    school = {
        '1а': 25,
        '1б': 28,
        '2а': 30,
        '2б': 27,
        '3а': 29,
        '4а': 31,
        '5а': 30,
        '6а': 29,
        '7а': 26,
        '8а': 31,
    }

    print("Исходное состояние школы:")
    for klass, count in school.items():
        print(f"{klass}: {count} учеников")

    cls_selection = input(
        "Выберите класс, количество учеников в котором будет изменено на 33: "
    )
    if cls_selection in school:
        school[cls_selection] = 33
    else:
        print("Класс не найден", file=sys.stderr)
        exit(1)

    cls_new = input("Напишите класс, который нужно добавить: ")
    if cls_new not in school:
        school[cls_new] = 26
    else:
        print("Класс уже существует", file=sys.stderr)
        exit(1)

    cls_delete = input("Выберите класс, который нужно удалить: ")
    if cls_delete in school:
        del school[cls_delete]
    else:
        print("Класс не найден", file=sys.stderr)
        exit(1)

    print(f"\nа) Количество учеников в классе {cls_selection} изменено на 33.")
    print(f"б) Добавлен новый класс {cls_new} с 26 учениками.")
    print(f"в) Класс {cls_delete} расформирован.")
    total_students = sum(school.values())

    print(f"\nОбщее количество учащихся в школе: {total_students}")