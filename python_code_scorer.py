#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:22:08 2025

@author: macbook
"""

def python_code_scorer(code_content):
    score = {
        'lines': 0,
        'comments': 0,
        'functions': 0,
        'error_handling': 0,
        'style': 0,
        'complexity': 0,
        'total': 0
    }
    
    lines = code_content.split('\n')
    total_lines = len(lines)
    non_empty_lines = [line.strip() for line in lines if line.strip() != '']
    
    # 1. 代码行数评分 (10分)
    if 20 <= total_lines <= 100:
        score['lines'] = 10
    elif 10 <= total_lines < 20 or 100 < total_lines <= 200:
        score['lines'] = 7
    elif 5 <= total_lines < 10 or 200 < total_lines <= 300:
        score['lines'] = 4
    else:
        score['lines'] = 2
    
    # 2. 注释比例评分 (20分)
    comment_lines = 0
    for line in lines:
        if line.strip().startswith('#') or '"""' in line or "'''" in line:
            comment_lines += 1
    
    if total_lines > 0:
        comment_ratio = comment_lines / total_lines
        if 0.15 <= comment_ratio <= 0.3:
            score['comments'] = 20
        elif 0.1 <= comment_ratio < 0.15 or 0.3 < comment_ratio <= 0.4:
            score['comments'] = 15
        elif 0.05 <= comment_ratio < 0.1 or 0.4 < comment_ratio <= 0.5:
            score['comments'] = 10
        else:
            score['comments'] = 5
    
    # 3. 函数使用评分 (20分)
    function_count = 0
    has_main = False
    for line in non_empty_lines:
        if line.startswith('def ') and line.endswith(':'):
            function_count += 1
        if 'if __name__ == "__main__":' in line or "if __name__ == '__main__':" in line:
            has_main = True
    
    if function_count >= 2:
        score['functions'] = 15
        if has_main:
            score['functions'] += 5
    elif function_count == 1:
        score['functions'] = 10
        if has_main:
            score['functions'] += 3
    else:
        score['functions'] = 5 if has_main else 2
    
    # 4. 错误处理评分 (15分)
    error_handling_keywords = ['try', 'except', 'finally', 'raise']
    error_handling_count = 0
    for line in non_empty_lines:
        for keyword in error_handling_keywords:
            if keyword in line and not line.strip().startswith('#'):
                error_handling_count += 1
    
    if error_handling_count >= 3:
        score['error_handling'] = 15
    elif error_handling_count == 2:
        score['error_handling'] = 10
    elif error_handling_count == 1:
        score['error_handling'] = 5
    else:
        score['error_handling'] = 0
    
    # 5. 代码风格评分 (20分)
    style_points = 0
    
    # 检查缩进 (4分)
    indent_consistent = True
    indent_sizes = []
    for line in non_empty_lines:
        if not line.startswith('#'):
            leading_spaces = len(line) - len(line.lstrip())
            if leading_spaces > 0:
                indent_sizes.append(leading_spaces)
    
    if indent_sizes:
        first_indent = indent_sizes[0]
        if all(indent % first_indent == 0 for indent in indent_sizes):
            style_points += 4
    
    # 检查变量命名 (4分)
    good_naming = True
    for line in non_empty_lines:
        if '=' in line and not line.strip().startswith('#'):
            var_name = line.split('=')[0].strip()
            if var_name.islower() or '_' in var_name:
                style_points += 1
                break
    
    # 检查函数命名 (4分)
    for line in non_empty_lines:
        if line.startswith('def ') and line.endswith(':'):
            func_name = line[4:-1].strip().split('(')[0]
            if '_' in func_name:
                style_points += 2
                break
    
    # 检查导入规范 (4分)
    import_lines = [line for line in non_empty_lines if line.startswith('import') or line.startswith('from')]
    if import_lines:
        style_points += 2
        # 检查是否有通配符导入
        if not any('*' in line for line in import_lines):
            style_points += 2
    
    # 检查行长度 (4分)
    long_lines = [line for line in lines if len(line) > 80]
    if len(long_lines) == 0:
        style_points += 4
    elif len(long_lines) <= 2:
        style_points += 2
    
    score['style'] = min(20, style_points)
    
    # 6. 代码复杂度评分 (15分) - 简单评估
    complexity_points = 15
    
    # 减少嵌套深度
    max_indent = 0
    for line in non_empty_lines:
        if not line.startswith('#'):
            indent_level = (len(line) - len(line.lstrip())) // 4  # 假设4空格缩进
            max_indent = max(max_indent, indent_level)
    
    if max_indent > 5:
        complexity_points -= 5
    elif max_indent > 3:
        complexity_points -= 2
    
    # 减少长函数
    function_lines = {}
    current_func = None
    for i, line in enumerate(lines):
        if line.startswith('def ') and line.endswith(':'):
            current_func = line[4:-1].strip().split('(')[0]
            function_lines[current_func] = 1
        elif current_func and line.strip() != '' and not line.startswith(' ' * 4):
            # 函数结束
            current_func = None
        elif current_func:
            function_lines[current_func] += 1
    
    for func_name, line_count in function_lines.items():
        if line_count > 30:
            complexity_points -= 3
        elif line_count > 20:
            complexity_points -= 1
    
    score['complexity'] = max(0, complexity_points)
    
    # 计算总分
    score['total'] = (
        score['lines'] + score['comments'] + score['functions'] +
        score['error_handling'] + score['style'] + score['complexity']
    )
    
    return score

def display_score_report(score):
    print("=" * 50)
    print(f"代码行数评分: {score['lines']}/10")
    print(f"注释比例评分: {score['comments']}/20")
    print(f"函数使用评分: {score['functions']}/20")
    print(f"错误处理评分: {score['error_handling']}/15")
    print(f"代码风格评分: {score['style']}/20")
    print(f"代码复杂度评分: {score['complexity']}/15")
    print("-" * 50)
    print(f"总分: {score['total']}/100")
    print("-" * 50)
    if score['total'] >= 90:
        grade = "A+ (卓越)"
    elif score['total'] >= 80:
        grade = "A (优秀)"
    elif score['total'] >= 70:
        grade = "B+ (良好)"
    elif score['total'] >= 60:
        grade = "B (合格)"
    elif score['total'] >= 50:
        grade = "C+ (需改进)"
    else:
        grade = "C (较差)"
    
    print(f"评级: {grade}")
    print("=" * 50)

# 示例
if __name__ == "__main__":
    try:
        with open('examples/example.py', 'r', encoding='utf-8') as file:
            code_to_score = file.read()
        
        # 评分并显示报告
        score = python_code_scorer(code_to_score)
        display_score_report(score)
        
    except FileNotFoundError:
        print("错误：找不到文件 'examples/example.py.py'")
        print("请将要评分的代码保存为 'examples/example.py.py' 文件")