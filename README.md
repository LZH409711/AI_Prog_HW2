# 第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略
步骤1：先让AI写出Student类和ExamSystem框架，明确面向对象结构  
步骤2：再让AI实现读取文件、查询、随机点名功能  
步骤3：最后让AI实现生成文件、文件夹、异常处理，并按作业规范修改

## 2. 核心 Prompt 迭代记录
初代 Prompt：写一个学生管理系统  
AI 生成的问题：没有用面向对象、没有异常处理、不符合格式要求  

优化后的 Prompt：  
用Python面向对象写学生信息与考场管理系统，必须有Student类、ExamSystem类、静态方法、异常处理，只能用标准库，实现查询、随机点名、生成考场表、生成准考证文件夹，注释完整，适合初学者。

## 3. Debug 与异常处理记录
报错类型：FileNotFoundError  
解决过程：我自己看报错信息发现找不到txt文件，于是在代码中加了try-except捕获，并提示用户文件不存在，同时提供了测试用txt内容。

## 4. 人工代码审查 (Code Review)
```python
@staticmethod
def check_num(input_str):
    # 静态方法，校验输入是否为数字
    try:
        num = int(input_str)  # 尝试转成整数
        return num           # 成功则返回数字
    except ValueError:
        return -1            # 失败返回-1