# 教育管理系统
import tkinter
import tkinter.messagebox
import insert
import delete
import select
import update
import update_user
import special
import pyodbc
import wx

class login():
	def __init__(self):
		# 创建主窗口,用于容纳其它组件
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		self.root.title("教学管理系统登陆界面")
		self.root.geometry('450x200+400+200')
		self.label_account = tkinter.Label(self.root, text = '学号/编号: ')
		#创建一个label名为Password:
		self.label_password = tkinter.Label(self.root, text = '登入密码 : ')  
		# 创建一个账号输入框,并设置尺寸
		self.input_account = tkinter.Entry(self.root, width = 30)
		# 创建一个密码输入框,并设置尺寸
		self.input_password = tkinter.Entry(self.root, show = '*',  width=30)
		# 创建一个登录系统的按钮
		self.login_button = tkinter.Button(self.root, command = self.backstage_interface,
			text = "登陆", width = 10)
		# 创建一个注册系统的按钮
		self.siginUp_button = tkinter.Button(self.root, command = self.exit,
			text = "退出", width = 10)
		self.master_account = '31354'
		self.master_password = '30333'

	# 完成布局
	def gui_arrang(self):
		self.label_account.place(x=60, y= 60)
		self.label_password.place(x=60, y= 85)
		self.input_account.place(x=130, y=60)
		self.input_password.place(x=130, y=85)
		self.login_button.place(x=140, y=130)
		self.siginUp_button.place(x=240, y=130)

	# 退出界面
	def exit(self):
		self.root.destroy()

	# 进行登录信息验证
	def backstage_interface(self):
		account = self.input_account.get()
		password = self.input_password.get()
		#对账户信息进行验证，普通用户返回user，管理员返回master，
		#账户错误返回noAccount，密码错误返回noPassword
		verifyResult = self.verifyAccount(account,password)
		if verifyResult == '管理员':
			self.root.destroy()
			m = master()
			# 进行布局
			m.gui_arrang()
		elif verifyResult == '学生':
			print(1)
			self.root.destroy()
			s = student(account)
			# 进行布局
			s.gui_arrang()
		elif verifyResult == '教师':
			self.root.destroy()
			t = teacher(account)
			# 进行布局
			t.gui_arrang()
		elif verifyResult == '输入有误':
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '输入有误请重新输入!')

	def verifyAccount(self,account,password):
		account = str(account)
		password = str(password)
		if (account == str(self.master_account)) and (password == str(self.master_password)):
			return '管理员'
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		cursor = cnxn.cursor()
		opr_string = "select teacher_no,teacher_pwd from teacher"
		cursor.execute(opr_string)
		row = cursor.fetchall()
		for i in range(len(row)):
			if (account == str(row[i][0]) and password == str(row[i][1])):
				return '教师'
		opr_string = "select student_no,student_pwd from student"
		cursor.execute(opr_string)
		row = cursor.fetchall()
		for i in range(len(row)):
			if (account == str(row[i][0]) and password == str(row[i][1])):
				return '学生'
		return '输入有误'

class master():
	def __init__(self):
		self.user = "管理员"
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		self.root.title("教学管理系统管理员界面")
		self.root.geometry('1100x500+200+200')
		# 创建按钮：学院数据
		self.college_insert_button = tkinter.Button(self.root, command = self.college_insert_interface,
			text = "学院数据插入", width = 15)
		self.college_detect_button = tkinter.Button(self.root, command = self.college_detect_interface,
			text = "学院数据删除", width = 15)
		self.college_update_button = tkinter.Button(self.root, command = self.college_update_interface,
			text = "学院数据修改", width = 15)
		self.college_select_button = tkinter.Button(self.root, command = self.college_select_interface,
			text = "学院数据查询", width = 15)
		# 创建按钮：专业数据
		self.major_insert_button = tkinter.Button(self.root, command = self.major_insert_interface,
			text = "专业数据插入", width = 15)
		self.major_detect_button = tkinter.Button(self.root, command = self.major_detect_interface,
			text = "专业数据删除", width = 15)
		self.major_update_button = tkinter.Button(self.root, command = self.major_update_interface,
			text = "专业数据修改", width = 15)
		self.major_select_button = tkinter.Button(self.root, command = self.major_select_interface,
			text = "专业数据查询", width = 15)
		# 创建按钮：班级数据
		self.class_insert_button = tkinter.Button(self.root, command = self.class_insert_interface,
			text = "班级数据插入", width = 15)
		self.class_detect_button = tkinter.Button(self.root, command = self.class_detect_interface,
			text = "班级数据删除", width = 15)
		self.class_update_button = tkinter.Button(self.root, command = self.class_update_interface,
			text = "班级数据修改", width = 15)
		self.class_select_button = tkinter.Button(self.root, command = self.class_select_interface,
			text = "班级数据查询", width = 15)
		# 创建按钮：教师数据
		self.teacher_insert_button = tkinter.Button(self.root, command = self.teacher_insert_interface,
			text = "教师数据插入", width = 15)
		self.teacher_detect_button = tkinter.Button(self.root, command = self.teacher_detect_interface,
			text = "教师数据删除", width = 15)
		self.teacher_update_button = tkinter.Button(self.root, command = self.teacher_update_interface,
			text = "教师数据修改", width = 15)
		self.teacher_select_button = tkinter.Button(self.root, command = self.teacher_select_interface,
			text = "教师数据查询", width = 15)
		# 创建按钮：教室数据
		self.class_room_insert_button = tkinter.Button(self.root, command = self.class_room_insert_interface,
			text = "教室数据插入", width = 15)
		self.class_room_detect_button = tkinter.Button(self.root, command = self.class_room_detect_interface,
			text = "教室数据删除", width = 15)
		self.class_room_update_button = tkinter.Button(self.root, command = self.class_room_update_interface,
			text = "教室数据修改", width = 15)
		self.class_room_select_button = tkinter.Button(self.root, command = self.class_room_select_interface,
			text = "教室数据查询", width = 15)
		# 创建按钮：课程数据
		self.course_insert_button = tkinter.Button(self.root, command = self.course_insert_interface,
			text = "课程数据插入", width = 15)
		self.course_detect_button = tkinter.Button(self.root, command = self.course_detect_interface,
			text = "课程数据删除", width = 15)
		self.course_update_button = tkinter.Button(self.root, command = self.course_update_interface,
			text = "课程数据修改", width = 15)
		self.course_select_button = tkinter.Button(self.root, command = self.course_select_interface,
			text = "课程数据查询", width = 15)
		# 创建按钮：学生数据
		self.student_insert_button = tkinter.Button(self.root, command = self.student_insert_interface,
			text = "学生数据插入", width = 15)
		self.student_detect_button = tkinter.Button(self.root, command = self.student_detect_interface,
			text = "学生数据删除", width = 15)
		self.student_update_button = tkinter.Button(self.root, command = self.student_update_interface,
			text = "学生数据修改", width = 15)
		self.student_select_button = tkinter.Button(self.root, command = self.student_select_interface,
			text = "学生数据查询", width = 15)
		# 特殊按钮
		self.special_select_button = tkinter.Button(self.root, command = self.special_select_interface,
			text = "连接查询", width = 15)
		self.special_count_button = tkinter.Button(self.root, command = self.special_master_interface,
			text = "SQL语句输入", width = 15)

	def gui_arrang(self):
		self.college_insert_button.place(x=30, y=30)
		self.college_detect_button.place(x=30, y=130)
		self.college_update_button.place(x=30, y=230)
		self.college_select_button.place(x=30, y=330)
		self.major_insert_button.place(x=180, y=30)
		self.major_detect_button.place(x=180, y=130)
		self.major_update_button.place(x=180, y=230)
		self.major_select_button.place(x=180, y=330)
		self.class_insert_button.place(x=330, y=30)
		self.class_detect_button.place(x=330, y=130)
		self.class_update_button.place(x=330, y=230)
		self.class_select_button.place(x=330, y=330)
		self.teacher_insert_button.place(x=480, y=30)
		self.teacher_detect_button.place(x=480, y=130)
		self.teacher_update_button.place(x=480, y=230)
		self.teacher_select_button.place(x=480, y=330)
		self.class_room_insert_button.place(x=630, y=30)
		self.class_room_detect_button.place(x=630, y=130)
		self.class_room_update_button.place(x=630, y=230)
		self.class_room_select_button.place(x=630, y=330)
		self.course_insert_button.place(x=780, y=30)
		self.course_detect_button.place(x=780, y=130)
		self.course_update_button.place(x=780, y=230)
		self.course_select_button.place(x=780, y=330)
		self.student_insert_button.place(x=930, y=30)
		self.student_detect_button.place(x=930, y=130)
		self.student_update_button.place(x=930, y=230)
		self.student_select_button.place(x=930, y=330)
		self.special_select_button.place(x=730-50, y=430)
		self.special_count_button.place(x=300 - 50, y=430)

	def special_select_interface(self):
		
		self.root.destroy()
		gui = special.ex_select(self.user)
		gui.gui_arrang()

	def special_master_interface(self):
		self.root.destroy()
		gui = special.ex_master(self.user)
		gui.gui_arrang()

	def college_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("学院数据",self.user)
		gui.gui_arrang()

	def college_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("学院数据",self.user)
		gui.gui_arrang()

	def college_update_interface(self):
		self.root.destroy()
		gui = update.update("学院数据",self.user)
		gui.gui_arrang()

	def college_select_interface(self):
		self.root.destroy()
		gui = select.select("学院数据",self.user)
		gui.gui_arrang()

	def major_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("专业数据",self.user)
		gui.gui_arrang()
	def major_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("专业数据",self.user)
		gui.gui_arrang()

	def major_update_interface(self):
		self.root.destroy()
		gui = update.update("专业数据",self.user)
		gui.gui_arrang()

	def major_select_interface(self):
		self.root.destroy()
		gui = select.select("专业数据",self.user)
		gui.gui_arrang()

	def class_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("班级数据",self.user)
		gui.gui_arrang()

	def class_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("班级数据",self.user)
		gui.gui_arrang()
	def class_update_interface(self):
		self.root.destroy()
		gui = update.update("班级数据",self.user)
		gui.gui_arrang()

	def class_select_interface(self):
		self.root.destroy()
		gui = select.select("班级数据",self.user)
		gui.gui_arrang()

	def teacher_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("教师数据",self.user)
		gui.gui_arrang()

	def teacher_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("教师数据",self.user)
		gui.gui_arrang()

	def teacher_update_interface(self):
		self.root.destroy()
		gui = update.update("教师数据",self.user)
		gui.gui_arrang()

	def teacher_select_interface(self):
		self.root.destroy()
		gui = select.select("教师数据",self.user)
		gui.gui_arrang()

	def class_room_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("教室数据",self.user)
		gui.gui_arrang()

	def class_room_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("教室数据",self.user)
		gui.gui_arrang()

	def class_room_update_interface(self):
		self.root.destroy()
		gui = update.update("教室数据",self.user)
		gui.gui_arrang()

	def class_room_select_interface(self):
		self.root.destroy()
		gui = select.select("教室数据",self.user)
		gui.gui_arrang()

	def course_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("课程数据",self.user)
		gui.gui_arrang()

	def course_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("课程数据",self.user)
		gui.gui_arrang()
	def course_update_interface(self):
		self.root.destroy()
		gui = update.update("课程数据",self.user)
		gui.gui_arrang()

	def course_select_interface(self):
		self.root.destroy()
		gui = select.select("课程数据",self.user)
		gui.gui_arrang()

	def student_insert_interface(self):
		self.root.destroy()
		gui = insert.insert("学生数据",self.user)
		gui.gui_arrang()

	def student_detect_interface(self):
		self.root.destroy()
		gui = delete.delete("学生数据",self.user)
		gui.gui_arrang()

	def student_update_interface(self):
		self.root.destroy()
		gui = update.update("学生数据",self.user)
		gui.gui_arrang()

	def student_select_interface(self):
		self.root.destroy()
		gui = select.select("学生数据",self.user)
		gui.gui_arrang()

class teacher():
	def __init__(self,account):
		self.account = account
		self.user = "教师"
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		self.root.title("教学管理系统教师界面")
		self.root.geometry('600x200+200+200')
		# 创建按钮：学院数据
		self.college_select_button = tkinter.Button(self.root, command = self.college_select_interface,
			text = "学院数据查询", width = 15)
		# 创建按钮：专业数据
		self.major_select_button = tkinter.Button(self.root, command = self.major_select_interface,
			text = "专业数据查询", width = 15)
		# 创建按钮：班级数据
		self.class_select_button = tkinter.Button(self.root, command = self.class_select_interface,
			text = "班级数据查询", width = 15)
		# 创建按钮：教师数据
		self.teacher_update_button = tkinter.Button(self.root, command = self.teacher_update_interface,
			text = "教师数据修改", width = 15)
		self.teacher_select_button = tkinter.Button(self.root, command = self.teacher_select_interface,
			text = "教师数据查询", width = 15)
		# 创建按钮：教室数据
		self.class_room_select_button = tkinter.Button(self.root, command = self.class_room_select_interface,
			text = "教室数据查询", width = 15)
		# 创建按钮：课程数据
		self.course_select_button = tkinter.Button(self.root, command = self.course_select_interface,
			text = "课程数据查询", width = 15)
		# 创建按钮：学生数据
		self.student_select_button = tkinter.Button(self.root, command = self.student_select_interface,
			text = "学生数据查询", width = 15)

	def gui_arrang(self):
		self.college_select_button.place(x = 30,y = 30)
		self.major_select_button.place(x = 230,y = 30)
		self.class_select_button.place(x = 430,y = 30)
		self.teacher_update_button.place(x = 30,y = 80)
		self.teacher_select_button.place(x = 230,y = 80)
		self.class_room_select_button.place(x = 430,y = 80)
		self.course_select_button.place(x = 30,y = 130)
		self.student_select_button.place(x = 230,y = 130)

	def college_select_interface(self):
		self.root.destroy()
		gui = select.select("学院数据",self.user)
		gui.gui_arrang()
	def major_select_interface(self):
		self.root.destroy()
		gui = select.select("专业数据",self.user)
		gui.gui_arrang()
	def class_select_interface(self):
		self.root.destroy()
		gui = select.select("班级数据",self.user)
		gui.gui_arrang()
	def teacher_update_interface(self):
		self.root.destroy()
		gui = update_user.update_teacher(self.account)
	def teacher_select_interface(self):
		self.root.destroy()
		gui = select.select("教师数据",self.user)
		gui.gui_arrang()
	def class_room_select_interface(self):
		self.root.destroy()
		gui = select.select("教室数据",self.user)
		gui.gui_arrang()
	def course_select_interface(self):
		self.root.destroy()
		gui = select.select("课程数据",self.user)
		gui.gui_arrang()
	def student_select_interface(self):
		self.root.destroy()
		gui = select.select("学生数据",self.user)
		gui.gui_arrang()
class student():
	def __init__(self,account):
		self.account = account
		self.user = "学生"
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		self.root.title("教学管理系统学生界面")
		self.root.geometry('600x200+200+200')
		# 创建按钮：学院数据
		self.college_select_button = tkinter.Button(self.root, command = self.college_select_interface,
			text = "学院数据查询", width = 15)
		# 创建按钮：专业数据
		self.major_select_button = tkinter.Button(self.root, command = self.major_select_interface,
			text = "专业数据查询", width = 15)
		# 创建按钮：班级数据
		self.class_select_button = tkinter.Button(self.root, command = self.class_select_interface,
			text = "班级数据查询", width = 15)
		# 创建按钮：教师数据
		self.teacher_select_button = tkinter.Button(self.root, command = self.teacher_select_interface,
			text = "教师数据查询", width = 15)
		# 创建按钮：教室数据
		self.class_room_select_button = tkinter.Button(self.root, command = self.class_room_select_interface,
			text = "教室数据查询", width = 15)
		# 创建按钮：课程数据
		self.course_select_button = tkinter.Button(self.root, command = self.course_select_interface,
			text = "课程数据查询", width = 15)
		# 创建按钮：学生数据
		self.student_update_button = tkinter.Button(self.root, command = self.student_update_interface,
			text = "学生数据修改", width = 15)
		self.student_select_button = tkinter.Button(self.root, command = self.student_select_interface,
			text = "学生数据查询", width = 15)

	def gui_arrang(self):
		self.college_select_button.place(x = 30,y = 30)
		self.major_select_button.place(x = 230,y = 30)
		self.class_select_button.place(x = 430,y = 30)
		self.teacher_select_button.place(x = 30,y = 80)
		self.class_room_select_button.place(x = 230,y = 80)
		self.course_select_button.place(x = 430,y = 80)
		self.student_update_button.place(x = 30,y = 130)
		self.student_select_button.place(x = 230,y = 130)
	def college_select_interface(self):
		self.root.destroy()
		gui = select.select("学院数据",self.user)
		gui.gui_arrang()
	def major_select_interface(self):
		self.root.destroy()
		gui = select.select("专业数据",self.user)
		gui.gui_arrang()
	def class_select_interface(self):
		self.root.destroy()
		gui = select.select("班级数据",self.user)
		gui.gui_arrang()
	def teacher_select_interface(self):
		self.root.destroy()
		gui = select.select("教师数据",self.user)
		gui.gui_arrang()
	def class_room_select_interface(self):
		self.root.destroy()
		gui = select.select("教室数据",self.user)
		gui.gui_arrang()
	def course_select_interface(self):
		self.root.destroy()
		gui = select.select("课程数据",self.user)
		gui.gui_arrang()
	def student_update_interface(self):
		self.root.destroy()
		gui = update_user.update_student(self.account)
	def student_select_interface(self):
		self.root.destroy()
		gui = select.select("学生数据",self.user)
		gui.gui_arrang()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	# 初始化对象
	L = login()
	# 进行布局
	L.gui_arrang()
	# 主程序执行
	tkinter.mainloop()
