#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    set1 = set(s1)
    set2 = set(s2)

    common = set1.intersection(set2)

    if common:
        print(f"Common symbols: {''.join(common)}")
    else:
        print("There is no common symbols.")