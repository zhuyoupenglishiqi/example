# 1. 完成窗口创建，（1）
# 2. 路径输入框的创建（2）
# 3. ”选择按钮“的创建（3）
# 4. “上传按钮“学生自己创建（4）
# 5. 创建成功”上传按钮“后引出路径错误，然后到自己输入路径先检查（5），用到while循环，if，else（5）
# 6. 创建“识别按钮”（6）

#（1）
import tools
top = tools.Tk()
top.geometry('640x480')

# （2）
e = tools.route(top)

# （3）
submit_button = tools.button(top, e, "选择")
submit_button.pack()

# （4）
submit_button = tools.button(top, e, "上传")
submit_button.pack()

# （6）
submit_button = tools.button(top, e, "识别", l=[])
submit_button.pack()

# （5）
# route = input('请输入路径: ')
# check = tools.route_check(route)
# print(check)
# while True:
#     if check == 'routeError':
#         route = input('路径错误，请重新输入： ')
#         check = tools.route_check(route)
#     else:
#         print('路径正确，可以去测试颜值了！')
#         break

# （1）
top.mainloop()