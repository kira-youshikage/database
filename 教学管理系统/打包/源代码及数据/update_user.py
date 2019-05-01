import tkinter.messagebox
import gui
import pyodbc

class update_teacher():
	def __init__(self,account):
		'''
		index取值：学院数据，专业数据，班级数据，教师数据，
				  教室数据，课程数据，学生数据
		back取值：管理员，学生，教师
		'''
		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		self.cursor = self.cnxn.cursor()
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		string = "教师信息修改界面"
		self.root.title(string)
		self.account = account
		self.root.geometry('400x275+400+200')
		self.label_teacher_polistatus= tkinter.Label(self.root, text = '教师政治面貌: ')
		self.input_teacher_polistatus = tkinter.Entry(self.root, width = 30)
		self.label_professional= tkinter.Label(self.root, text = '教师职称: ')
		self.input_professional = tkinter.Entry(self.root, width = 30)
		self.label_teacher_tel= tkinter.Label(self.root, text = '联系方式: ')
		self.input_teacher_tel = tkinter.Entry(self.root, width = 30)
		self.label_teacher_depart= tkinter.Label(self.root, text = '所属院系: ')
		self.input_teacher_depart = tkinter.Entry(self.root, width = 30)
		self.label_teacher_college= tkinter.Label(self.root, text = '毕业学校: ')
		self.input_teacher_college = tkinter.Entry(self.root, width = 30)
		self.label_teacher_entry= tkinter.Label(self.root, text = '入职年份: ')
		self.input_teacher_entry = tkinter.Entry(self.root, width = 30)
		self.label_teacher_pwd= tkinter.Label(self.root, text = '登入密码: ')
		self.input_teacher_pwd = tkinter.Entry(self.root, width = 30)
		self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
		self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
		self.label_teacher_polistatus.place(x=38, y= 105 - 75)
		self.label_professional.place(x=60, y= 130 - 75)
		self.label_teacher_tel.place(x=60, y= 155 - 75)
		self.label_teacher_depart.place(x=60, y= 180 - 75)
		self.label_teacher_college.place(x=60, y= 205 - 75)
		self.label_teacher_entry.place(x=60, y= 230 - 75)
		self.label_teacher_pwd.place(x=60, y= 255 - 75)
		self.input_teacher_polistatus.place(x=130, y=105 - 75)
		self.input_professional.place(x=130, y=130 - 75)
		self.input_teacher_tel.place(x=130, y=155 - 75)
		self.input_teacher_depart.place(x=130, y=180 - 75)
		self.input_teacher_college.place(x=130, y=205 - 75)
		self.input_teacher_entry.place(x=130, y=230 - 75)
		self.input_teacher_pwd.place(x=130, y=255 - 75)
		self.button_ok.place(x=150-70, y=295 - 75)
		self.button_back.place(x=350-70, y=295 - 75)
	
	def ok_interface(self):
		string_teacher_polistatus = "'" + self.input_teacher_polistatus.get() + "'"
		string_professional = "'" + self.input_professional.get() + "'"
		string_teacher_tel = "'" + self.input_teacher_tel.get() + "'"
		string_teacher_depart = "'" + self.input_teacher_depart.get() + "'"
		string_teacher_college = "'" + self.input_teacher_college.get() + "'"
		string_teacher_entry = self.input_teacher_entry.get()
		string_teacher_pwd = "'" + self.input_teacher_pwd.get() + "'"
		if string_teacher_polistatus != "''":
			opr_string = " \
				update teacher\
				set teacher_polistatus = " + string_teacher_polistatus\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_professional != "''":
			opr_string = " \
				update teacher\
				set professional = " + string_professional\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_teacher_tel != "''":
			opr_string = " \
				update teacher\
				set teacher_tel = " + string_teacher_tel\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_teacher_depart != "''":
			opr_string = " \
				update teacher\
				set teacher_depart = " + string_teacher_depart\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_teacher_college != "''":
			opr_string = " \
				update teacher\
				set teacher_college = " + string_teacher_college\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_teacher_entry != "":
			opr_string = " \
				update teacher\
				set teacher_entry = " + string_teacher_entry\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_teacher_pwd != "''":
			opr_string = " \
				update teacher\
				set teacher_pwd = " + string_teacher_pwd\
				+ "where teacher_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		tkinter.messagebox.showinfo(title = '教育管理系统', message = '更新成功')

	def back_interface(self):
		self.root.destroy()
		t = gui.teacher(self.account)
		t.gui_arrang()

class update_student():
	def __init__(self,account):
		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		self.cursor = self.cnxn.cursor()
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		string = "学生信息修改界面"
		self.root.title(string)
		self.account = account
		self.root.geometry('400x275+400+200')
		self.label_student_birth = tkinter.Label(self.root, text = '学生出生年月日: ')
		self.input_student_birth = tkinter.Entry(self.root, width = 30)
		self.label_student_polistatus= tkinter.Label(self.root, text = '学生政治面貌: ')
		self.input_student_polistatus = tkinter.Entry(self.root, width = 30)
		self.label_student_nation= tkinter.Label(self.root, text = '民族: ')
		self.input_student_nation = tkinter.Entry(self.root, width = 30)
		self.label_student_home= tkinter.Label(self.root, text = '家庭住址: ')
		self.input_student_home = tkinter.Entry(self.root, width = 30)
		self.label_student_home_tel = tkinter.Label(self.root, text = '家庭电话: ')
		self.input_student_home_tel = tkinter.Entry(self.root, width = 30)
		self.label_student_pwd= tkinter.Label(self.root, text = '系统登入密码: ')
		self.input_student_pwd = tkinter.Entry(self.root, width = 30)
		self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
		self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
		self.label_student_birth.place(x=60-32, y= 105 - 75)
		self.label_student_polistatus.place(x=60-16, y= 130 - 75)
		self.label_student_nation.place(x=60+12, y= 155 - 75)
		self.label_student_home.place(x=60, y= 180 - 75)
		self.label_student_home_tel.place(x=60, y= 205 - 75)
		self.label_student_pwd.place(x=60-16, y= 230 - 75)
		self.input_student_birth.place(x=130, y=105 - 75)
		self.input_student_polistatus.place(x=130, y=130 - 75)
		self.input_student_nation.place(x=130, y=155 - 75)
		self.input_student_home.place(x=130, y=180 - 75)
		self.input_student_home_tel.place(x=130, y=205 - 75)
		self.input_student_pwd.place(x=130, y=230 - 75)
		self.button_ok.place(x=150-70, y=295 - 100)
		self.button_back.place(x=350-70, y=295 - 100)
	
	def ok_interface(self):
		string_student_birth = "'" + self.input_student_birth.get() + "'"
		string_student_polistatus = "'" + self.input_student_polistatus.get() + "'"
		string_student_nation = "'" + self.input_student_nation.get() + "'"
		string_student_home = "'" + self.input_student_home.get() + "'"
		string_student_home_tel = "'" + self.input_student_home_tel.get() + "'"
		string_student_pwd = "'" + self.input_student_pwd.get() + "'"
		if string_student_birth != "''":
			opr_string = " \
				update student\
				set student_birth = " + string_student_birth\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_student_polistatus != "''":
			opr_string = " \
				update student\
				set student_polistatus = " + string_student_polistatus\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_student_nation != "''":
			opr_string = " \
				update student\
				set student_nation = " + string_student_nation\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_student_home != "''":
			opr_string = " \
				update student\
				set student_home = " + string_student_home\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_student_home_tel != "''":
			opr_string = " \
				update student\
				set student_home_tel = " + string_student_home_tel\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		if string_student_pwd != "''":
			opr_string = " \
				update student\
				set student_pwd = " + string_student_pwd\
				+ "where student_no = " + str(self.account)
			self.cursor.execute(opr_string)
			self.cnxn.commit()
		tkinter.messagebox.showinfo(title = '教育管理系统', message = '更新成功')
		
	def back_interface(self):
		self.root.destroy()
		s = gui.student(self.account)
		s.gui_arrang()