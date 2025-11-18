#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:42:16 2025

@author: macbook
"""

from python_code_scorer import *

if __name__ == "__main__":
    try:
        with open('examples/example.py', 'r', encoding='utf-8') as file:
            code_to_score = file.read()
        score = python_code_scorer(code_to_score)
        display_score_report(score)
    except FileNotFoundError:
        print("错误：找不到文件 'examples/example.py.py'")