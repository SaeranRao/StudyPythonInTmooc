# 修改之前的学生信息管理系统程序，实现添加菜单和选择菜单操作功能:
#     菜单:
        # +----------------------------------+
        # |   1)添加学生信息
        # |   2)查看所有学生信息
        # |   3)修改学生成绩
        # |   4)删除学生信息
        # |   q)退出
        # +----------------------------------+

# 写一个打印菜单的函数
def show_menu():
        print('# +----------------------------------+')
        print('# |   1)添加学生信息')
        print('# |   2)查看所有学生信息')
        print('# |   3)修改学生成绩')
        print('# |   4)删除学生信息')
        print('# |   q)退出')
        print('# +----------------------------------+')

# 输入学生信息
def input_student():
        name = input('请输入学生信息')
        age = input('请输入学生年龄')
        score = input('请输入学生成绩')

        student_list = []
        student = {'name':name,'age':age,'score':score}
        student_list.append(student)
        return(student_list)

def output_student(docs):
        print(docs)
        return

#定义主函数，实现功能选择功能
def main():
        docs = [] #存储学生信息的字典
        while True:
                show_menu()
                s = input("请选择")
                if s == '1':
                        docs += input_student()
                elif s == '2':
                        output_student(docs)
                elif s == '3':
                        pass
                elif s == '4':
                        pass
                elif s == 'q':
                        return

main()