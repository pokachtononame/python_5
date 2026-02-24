#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    nums = {
         1: 'first',
         2: 'second',
         3: 'third',
         4: 'fourth',
         5: 'fifth',
         6: 'sixth',
         7: 'seventh',
    }

    print(f"Исходный словарь: {nums}")

    dict_items = nums.items()
    swapped = {}
    for k, v in dict_items:
        swapped[v] = k

    print(f"\nСловарь, обратный исходному: {swapped}")

