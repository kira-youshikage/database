# 特殊界面类
import tkinter
import tkinter.messagebox
import gui
import pyodbc
import xlwt
import wx

class ex_select():
	def __init__(self,back):
		'''
		back取值：管理员，学生，教师
		'''
		# 创建主窗口，用于容纳其它组件
		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		self.cursor = self.cnxn.cursor()
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		string = "请输入连接查询条件"
		self.root.title(string)
		self.back = back

	def gui_arrang(self):
		self.root.geometry('630x350+400+200')
		e_1_1 = tkinter.StringVar()
		e_1_1.set("student.class_no")
		e_1_2 = tkinter.StringVar()
		e_1_2.set("student.student_entry")
		e_1_3 = tkinter.StringVar()
		e_1_3.set("student.class_no")
		e_1_4 = tkinter.StringVar()
		e_1_4.set("student.student_entry")
		e_1_5 = tkinter.StringVar()
		e_1_5.set("class.class_tutor")
		e_1_6 = tkinter.StringVar()
		e_1_6.set("student.student_spec")
		self.input_1_1 = tkinter.Entry(self.root, textvariable = e_1_1,width = 30)
		self.input_1_2 = tkinter.Entry(self.root, textvariable = e_1_2, width = 30)
		self.input_1_3 = tkinter.Entry(self.root, textvariable = e_1_3, width = 30)
		self.input_1_4 = tkinter.Entry(self.root, textvariable = e_1_4, width = 30)
		self.input_1_5 = tkinter.Entry(self.root, textvariable = e_1_5, width = 30)
		self.input_1_6 = tkinter.Entry(self.root, textvariable = e_1_6, width = 30)
		self.input_1_7 = tkinter.Entry(self.root, width = 30)
		self.input_1_8 = tkinter.Entry(self.root, width = 30)
		self.input_1_9 = tkinter.Entry(self.root, width = 30)
		self.input_1_10 = tkinter.Entry(self.root, width = 30)
		e_2_1 = tkinter.StringVar()
		e_2_1.set("=")
		e_2_2 = tkinter.StringVar()
		e_2_2.set("=")
		e_2_3 = tkinter.StringVar()
		e_2_3.set("=")
		e_2_4 = tkinter.StringVar()
		e_2_4.set("=")
		e_2_5 = tkinter.StringVar()
		e_2_5.set("=")
		e_2_6 = tkinter.StringVar()
		e_2_6.set("=")
		self.input_2_1 = tkinter.Entry(self.root, textvariable = e_2_1, width = 5)
		self.input_2_2 = tkinter.Entry(self.root, textvariable = e_2_2, width = 5)
		self.input_2_3 = tkinter.Entry(self.root, textvariable = e_2_3, width = 5)
		self.input_2_4 = tkinter.Entry(self.root, textvariable = e_2_4, width = 5)
		self.input_2_5 = tkinter.Entry(self.root, textvariable = e_2_5, width = 5)
		self.input_2_6 = tkinter.Entry(self.root, textvariable = e_2_6, width = 5)
		self.input_2_7 = tkinter.Entry(self.root, width = 5)
		self.input_2_8 = tkinter.Entry(self.root, width = 5)
		self.input_2_9 = tkinter.Entry(self.root, width = 5)
		self.input_2_10 = tkinter.Entry(self.root, width = 5)
		e_3_1 = tkinter.StringVar()
		e_3_1.set("1")
		e_3_2 = tkinter.StringVar()
		e_3_2.set("2015")
		e_3_3 = tkinter.StringVar()
		e_3_3.set("class.class_no")
		e_3_4 = tkinter.StringVar()
		e_3_4.set("class.class_year")
		e_3_5 = tkinter.StringVar()
		e_3_5.set("teacher.teacher_no")
		e_3_6 = tkinter.StringVar()
		e_3_6.set("class.class_depart")
		self.input_3_1 = tkinter.Entry(self.root, textvariable = e_3_1, width = 30)
		self.input_3_2 = tkinter.Entry(self.root, textvariable = e_3_2, width = 30)
		self.input_3_3 = tkinter.Entry(self.root, textvariable = e_3_3, width = 30)
		self.input_3_4 = tkinter.Entry(self.root, textvariable = e_3_4, width = 30)
		self.input_3_5 = tkinter.Entry(self.root, textvariable = e_3_5, width = 30)
		self.input_3_6 = tkinter.Entry(self.root, textvariable = e_3_6, width = 30)
		self.input_3_7 = tkinter.Entry(self.root, width = 30)
		self.input_3_8 = tkinter.Entry(self.root, width = 30)
		self.input_3_9 = tkinter.Entry(self.root, width = 30)
		self.input_3_10 = tkinter.Entry(self.root, width = 30)
		self.input_1_1.place(x=60, y=30)
		self.input_1_2.place(x=60, y=55)
		self.input_1_3.place(x=60, y=80)
		self.input_1_4.place(x=60, y=105)
		self.input_1_5.place(x=60, y=130)
		self.input_1_6.place(x=60, y=155)
		self.input_1_7.place(x=60, y=180)
		self.input_1_8.place(x=60, y=205)
		self.input_1_9.place(x=60, y=230)
		self.input_1_10.place(x=60, y=255)
		self.input_2_1.place(x=300, y=30)
		self.input_2_2.place(x=300, y=55)
		self.input_2_3.place(x=300, y=80)
		self.input_2_4.place(x=300, y=105)
		self.input_2_5.place(x=300, y=130)
		self.input_2_6.place(x=300, y=155)
		self.input_2_7.place(x=300, y=180)
		self.input_2_8.place(x=300, y=205)
		self.input_2_9.place(x=300, y=230)
		self.input_2_10.place(x=300, y=255)
		self.input_3_1.place(x=360, y=30)
		self.input_3_2.place(x=360, y=55)
		self.input_3_3.place(x=360, y=80)
		self.input_3_4.place(x=360, y=105)
		self.input_3_5.place(x=360, y=130)
		self.input_3_6.place(x=360, y=155)
		self.input_3_7.place(x=360, y=180)
		self.input_3_8.place(x=360, y=205)
		self.input_3_9.place(x=360, y=230)
		self.input_3_10.place(x=360, y=255)
		self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
		self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
		self.button_ok.place(x=180, y=300)
		self.button_back.place(x=380, y=300)
	def ok_interface(self):
		string_1_1 = self.input_1_1.get()
		string_1_2 = self.input_1_2.get()
		string_1_3 = self.input_1_3.get()
		string_1_4 = self.input_1_4.get()
		string_1_5 = self.input_1_5.get()
		string_1_6 = self.input_1_6.get()
		string_1_7 = self.input_1_7.get()
		string_1_8 = self.input_1_8.get()
		string_1_9 = self.input_1_9.get()
		string_1_10 = self.input_1_10.get()
		string_2_1 = self.input_2_1.get()
		string_2_2 = self.input_2_2.get()
		string_2_3 = self.input_2_3.get()
		string_2_4 = self.input_2_4.get()
		string_2_5 = self.input_2_5.get()
		string_2_6 = self.input_2_6.get()
		string_2_7 = self.input_2_7.get()
		string_2_8 = self.input_2_8.get()
		string_2_9 = self.input_2_9.get()
		string_2_10 = self.input_2_10.get()
		string_3_1 = self.input_3_1.get()
		string_3_2 = self.input_3_2.get()
		string_3_3 = self.input_3_3.get()
		string_3_4 = self.input_3_4.get()
		string_3_5 = self.input_3_5.get()
		string_3_6 = self.input_3_6.get()
		string_3_7 = self.input_3_7.get()
		string_3_8 = self.input_3_8.get()
		string_3_9 = self.input_3_9.get()
		string_3_10 = self.input_3_10.get()
		string = [string_1_1,string_1_2,string_1_3,
			string_1_4,string_1_5,string_1_6,
			string_1_7,string_1_8,string_1_9,
			string_1_10,string_3_1,string_3_2,string_3_3,
			string_3_4,string_3_5,string_3_6,
			string_3_7,string_3_8,string_3_9,
			string_3_10]
		select_list = []
		for i in range(len(string)):
			if string[i] != '':
				select = string[i].split('.')
				if len(select) == 2:
					select_list.append(select[0])
		select_list = list(set(select_list))
		dlg_1 = wx.TextEntryDialog(None,"请输入查找结果属性，如有多个属性请用“,”隔开","查找结果",
			"student.student_name,teacher.teacher_name,class.class_depart")
		# 如果按下确认
		if dlg_1.ShowModal() == wx.ID_OK:
			# 得到输入字符串
			respose = str(dlg_1.GetValue())
		respose_list = respose.split(',')
		string_select = "select distinct "
		for i in range(len(respose_list) - 1):
			string_select += respose_list[i] + ","
		string_select += respose_list[len(respose_list) - 1] + " from "
		for i in range(len(select_list) - 1):
			string_select += select_list[i] + ","
		string_select += select_list[len(select_list) - 1]
		string_where = "where("
		if string_2_1 == "x":
			string_where += string_1_1 + "=" + string_2_1
		if (string_2_1 == "=") or (string_2_1 == ">") or (string_2_1 == "<") or \
			(string_2_1 == ">=") or (string_2_1 == "<="):
			string_where += string_1_1 + string_2_1 + self.get_string(string_1_1,string_3_1)
		if string_2_2 == "x":
			string_where += " and " + string_1_2 + "=" + string_2_2
		if (string_2_2 == "=") or (string_2_2 == ">") or (string_2_2 == "<") or \
			(string_2_2 == ">=") or (string_2_2 == "<="):
			string_where += " and " + string_1_2 + string_2_2 + self.get_string(string_1_2,string_3_2)
		if string_2_3 == "x":
			string_where += " and " + string_1_3 + "=" + string_2_3
		if (string_2_3 == "=") or (string_2_3 == ">") or (string_2_3 == "<") or \
			(string_2_3 == ">=") or (string_2_3 == "<="):
			string_where += " and " + string_1_3 + string_2_3 + self.get_string(string_1_3,string_3_3)
		if string_2_4 == "x":
			string_where += " and " + string_1_4 + "=" + string_2_4
		if (string_2_4 == "=") or (string_2_4 == ">") or (string_2_4 == "<") or \
			(string_2_4 == ">=") or (string_2_4 == "<="):
			string_where += " and " + string_1_4 + string_2_4 + self.get_string(string_1_4,string_3_4)
		if string_2_5 == "x":
			string_where += " and " + string_1_5 + "=" + string_2_5
		if (string_2_5 == "=") or (string_2_5 == ">") or (string_2_5 == "<") or \
			(string_2_5 == ">=") or (string_2_5 == "<="):
			string_where += " and " + string_1_5 + string_2_5 + self.get_string(string_1_5,string_3_5)
		if string_2_6 == "x":
			string_where += " and " + string_1_6 + "=" + string_2_6
		if (string_2_6 == "=") or (string_2_6 == ">") or (string_2_6 == "<") or \
			(string_2_6 == ">=") or (string_2_6 == "<="):
			string_where += " and " + string_1_6  + ' collate Chinese_PRC_CS_AS' + string_2_6 + self.get_string(string_1_6,string_3_6)
		if string_2_7 == "x":
			string_where += " and " + string_1_7 + "=" + string_2_7
		if (string_2_7 == "=") or (string_2_7 == ">") or (string_2_7 == "<") or \
			(string_2_7 == ">=") or (string_2_7 == "<="):
			string_where += " and " + string_1_7 + string_2_7 + self.get_string(string_1_7,string_3_7)
		if string_2_8 == "x":
			string_where += " and " + string_1_8 + "=" + string_2_8
		if (string_2_8 == "=") or (string_2_8 == ">") or (string_2_8 == "<") or \
			(string_2_8 == ">=") or (string_2_8 == "<="):
			string_where += " and " + string_1_8 + string_2_8 + self.get_string(string_1_8,string_3_8)
		if string_2_9 == "x":
			string_where += " and " + string_1_9 + "=" + string_2_9
		if (string_2_9 == "=") or (string_2_9 == ">") or (string_2_9 == "<") or \
			(string_2_9 == ">=") or (string_2_9 == "<="):
			string_where += " and " + string_1_9 + string_2_9 + self.get_string(string_1_9,string_3_9)
		if string_2_10 == "x":
			string_where += " and " + string_1_10 + "=" + string_2_10
		if (string_2_10 == "=") or (string_2_10 == ">") or (string_2_10 == "<") or \
			(string_2_10 == ">=") or (string_2_10 == "<="):
			string_where += " and " + string_1_10 + string_2_10 + self.get_string(string_1_10,string_3_10)
		string_where += ")"
		opr_string = string_select +"\n"+ string_where
		print(opr_string)
		self.cursor.execute(opr_string)
		workbook = xlwt.Workbook(encoding = 'ascii')
		worksheet = workbook.add_sheet('查询结果')
		for i in range(len(respose_list)):
			worksheet.write(0,i,respose_list[i])
		row = self.cursor.fetchall()
		for i in range(len(row)):
			for j in range(len(row[i])):
				worksheet.write(i + 1,j,row[i][j])
		path = '查询结果.xls'
		workbook.save(path)
		#print(self.cursor.fetchall())

	def back_interface(self):
		self.root.destroy()
		if self.back == "管理员":
			m = gui.master()
			m.gui_arrang()
		elif self.back == "学生":
			s = gui.student()
			s.gui_arrang()
		elif self.back == "教师":
			t = gui.teacher()
			t.gui_arrang()

	def get_string(self,string_1,string_input):
		string = string_input.split('.')
		if len(string) == 2:
			return string_input
		if string_1 == "class.class_no":
			return string_input
		elif string_1 == "class.class_year":
			return string_input
		elif string_1 == "class.class_year":
			return string_input
		elif string_1 == "class_room.class_room_no":
			return string_input
		elif string_1 == "class_room.class_room_capacity":
			return string_input
		elif string_1 == "course.course_no":
			return string_input
		elif string_1 == "course.course_period":
			return string_input
		elif string_1 == "major.major_no":
			return string_input
		elif string_1 == "student.student_no":
			return string_input
		elif string_1 == "student.class_no":
			return string_input
		elif string_1 == "student.student_entry":
			return string_input
		elif string_1 == "teacher.teacher_no":
			return string_input
		elif string_1 == "teacher.teacher_entry":
			return string_input
		else:
			string = "'" + string_1 + "'"
			return string

class ex_master():
	def __init__(self,back):
		'''
		back取值：管理员，学生，教师
		'''
		# 创建主窗口，用于容纳其它组件
		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		self.cursor = self.cnxn.cursor()
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		string = "请输入SQL语句"
		self.root.title(string)
		self.back = back

	def gui_arrang(self):
		self.root.geometry('570x380+400+200')
		self.label = tkinter.Label(self.root, text = 'SQL语句: ')
		self.text = tkinter.Text(self.root, width=50, height=20)
		self.label.place(x=30, y=130)
		self.text.place(x=100, y=50)
		self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
		self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
		self.button_ok.place(x=80, y=330)
		self.button_back.place(x=380, y=330)
	def ok_interface(self):
		opr_string = self.text.get(0.0,tkinter.END)
		self.cursor.execute(opr_string)
		try:
			workbook = xlwt.Workbook(encoding = 'ascii')
			worksheet = workbook.add_sheet('查询结果')
			row = self.cursor.fetchall()
			for i in range(len(row)):
				for j in range(len(row[i])):
					worksheet.write(i,j,row[i][j])
			path = '查询结果.xls'
			workbook.save(path)
		except:
			print("请忽略")
		self.cnxn.commit()

	def back_interface(self):
		self.root.destroy()
		if self.back == "管理员":
			m = gui.master()
			m.gui_arrang()
		elif self.back == "学生":
			s = gui.student()
			s.gui_arrang()
		elif self.back == "教师":
			t = gui.teacher()
			t.gui_arrang()