# Python-Code-Scorer（自用）

---

## 核心功能
- **多维度评分**
- **PEP8基础体检**
- **复杂度扫描**

---

## 调用方法
```bash
from python_code_scorer import *

with open('example.py', 'r', encoding='utf-8') as file:
    code_to_score = file.read()
score = python_code_scorer(code_to_score)
display_score_report(score)
```
---

## 试用
```bash
python try.py
```

---

## 评分标准
| 维度         | 权重 |
|--------------|------|
| 代码行数     | 10%  |
| 注释比例     | 20%  |
| 函数模块化   | 20%  |
| 错误处理     | 15%  |
| 代码风格     | 20%  |
| 复杂度控制   | 15%  |

---

## 开源协议

本项目采用 MIT 协议开源，详见 [LICENSE](LICENSE) 文件。

---

**Made with ❤️ for Byron**  
By Byron | [GitHub](https://github.com/byronwang2005/Python-Code-Scorer)
