# 导入Python标准库
import os   # 用于文件/文件夹操作
import random  # 用于随机打乱、随机点名
import time    # 用于获取当前时间


class Student:
    # 初始化学生对象
    def __init__(self, student_id, name, gender, cls, college):
        self.student_id = student_id  # 学号
        self.name = name              # 姓名
        self.gender = gender          # 性别
        self.cls = cls                # 班级
        self.college = college        # 学院


    def __str__(self):
        return f"学号：{self.student_id} 姓名：{self.name} 性别：{self.gender} 班级：{self.cls} 学院：{self.college}"


class ExamSystem:
    # 构造方法：加载学生文件
    def __init__(self, filename):
        self.student_list = []  # 存放所有学生对象
        self.read_from_file(filename)  # 启动时读取文件

    # 静态方法：校验输入是否为数字
    @staticmethod
    def check_num(input_str):
        try:
            num = int(input_str)
            return num
        except ValueError:
            return -1

    # 读取学生名单txt文件
    def read_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # 跳过第一行标题，从第二行开始读
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    # 按空格拆分信息
                    parts = line.split()
                    stu = Student(parts[0], parts[1], parts[2], parts[3], parts[4])
                    self.student_list.append(stu)
            print(f"成功加载 {len(self.student_list)} 名学生")
        except FileNotFoundError:
            print("错误：找不到学生名单文件")
            exit()

    # 1. 根据学号查找学生
    def find_student(self, student_id):
        for stu in self.student_list:
            if stu.student_id == student_id:
                return stu
        return None

    # 2. 随机点名
    def random_call(self, count):
        if count < 1 or count > len(self.student_list):
            return []
        return random.sample(self.student_list, count)

    # 3. 生成考场安排表
    def make_exam_table(self):
        # 随机打乱所有学生
        shuffled = random.sample(self.student_list, len(self.student_list))
        try:
            with open("考场安排表.txt", "w", encoding="utf-8") as f:
                # 第一行写生成时间
                f.write(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*30 + "\n")
                # 写入座位、姓名、学号
                for idx, stu in enumerate(shuffled, 1):
                    f.write(f"座位{idx:02d}：{stu.name} {stu.student_id}\n")
            print("考场安排表已生成：考场安排表.txt")
            return shuffled
        except Exception as e:
            print(f"生成失败：{e}")
            return []

    # 4. 生成准考证文件夹与文件
    def make_tickets(self, student_list):
        try:
            # 创建文件夹
            if not os.path.exists("准考证"):
                os.mkdir("准考证")
            # 逐个生成文件
            for idx, stu in enumerate(student_list, 1):
                path = f"准考证/{idx:02d}.txt"
                with open(path, "w", encoding="utf-8") as f:
                    f.write(f"座位号：{idx:02d}\n")
                    f.write(f"姓名：{stu.name}\n")
                    f.write(f"学号：{stu.student_id}\n")
            print("准考证文件夹与文件已生成")
        except Exception as e:
            print(f"生成准考证失败：{e}")


def main():
    system = ExamSystem("人工智能编程语言学生名单.txt")
    # 先保存打乱后的学生，用于生成准考证
    arranged_stus = []

    while True:
        print("\n===== 学生信息与考场管理系统 =====")
        print("1. 按学号查询学生")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证")
        print("0. 退出")
        choice = input("请输入编号：")

        if choice == "1":
            sid = input("请输入学号：")
            stu = system.find_student(sid)
            print(stu if stu else "该学号不存在")

        elif choice == "2":
            s = input("请输入点名人数：")
            num = ExamSystem.check_num(s)
            if num == -1:
                print("请输入数字")
            elif num > len(system.student_list):
                print(f"不能超过总人数{len(system.student_list)}")
            else:
                res = system.random_call(num)
                print("\n随机点名结果：")
                for i, stu in enumerate(res, 1):
                    print(f"{i}. {stu.name} {stu.student_id}")

        elif choice == "3":
            arranged_stus = system.make_exam_table()

        elif choice == "4":
            if not arranged_stus:
                print("请先生成考场安排表")
            else:
                system.make_tickets(arranged_stus)

        elif choice == "0":
            print("退出系统")
            break
        else:
            print("输入无效")

if __name__ == "__main__":
    main()