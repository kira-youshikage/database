# 插入界面类
import tkinter
import tkinter.messagebox
import gui
import pyodbc

class insert():
	def __init__(self,index,back):
		'''
		index取值：学院数据，专业数据，班级数据，教师数据，
				  教室数据，课程数据，学生数据
		back取值：管理员，学生，教师
		'''
		# 创建主窗口，用于容纳其它组件
		self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-L9H2RCK;DATABASE=教学管理系统;UID=sa;PWD=31354')
		self.cursor = self.cnxn.cursor()
		self.root = tkinter.Tk()
		# 给主窗口设置标题内容
		string = index + "插入界面"
		self.root.title(string)
		self.index = index
		self.back = back

	def gui_arrang(self):
		if self.index == "学院数据":
			self.root.geometry('450x200+400+200')
			self.label_college_id = tkinter.Label(self.root, text = '学院名称: ')
			self.input_college_id = tkinter.Entry(self.root, width = 30)
			self.label_college_abstract = tkinter.Label(self.root, text = '学院简介: ')
			self.input_college_abstract = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_college_id.place(x=60, y= 60)
			self.label_college_abstract.place(x=60, y= 85)
			self.input_college_id.place(x=130, y=60)
			self.input_college_abstract.place(x=130, y=85)
			self.button_ok.place(x=140, y=130)
			self.button_back.place(x=240, y=130)
		if self.index == "专业数据":
			self.root.geometry('450x200+400+200')
			self.label_major_no = tkinter.Label(self.root, text = '专业编号: ')
			self.input_major_no = tkinter.Entry(self.root, width = 30)
			self.label_major_depart = tkinter.Label(self.root, text = '专业所属学院: ')
			self.input_major_depart = tkinter.Entry(self.root, width = 30)
			self.label_major_name = tkinter.Label(self.root, text = '专业名称: ')
			self.input_major_name = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_major_no.place(x=60, y= 60)
			self.label_major_depart.place(x=38, y= 85)
			self.label_major_name.place(x=60, y= 110)
			self.input_major_no.place(x=130, y=60)
			self.input_major_depart.place(x=130, y=85)
			self.input_major_name.place(x=130, y=110)
			self.button_ok.place(x=140, y=150)
			self.button_back.place(x=240, y=150)
		if self.index == "班级数据":
			self.root.geometry('450x220+400+200')
			self.label_class_no = tkinter.Label(self.root, text = '班级编号: ')
			self.input_class_no = tkinter.Entry(self.root, width = 30)
			self.label_class_depart = tkinter.Label(self.root, text = '班级所属专业: ')
			self.input_class_depart = tkinter.Entry(self.root, width = 30)
			self.label_class_year= tkinter.Label(self.root, text = '班级入学年份: ')
			self.input_class_year = tkinter.Entry(self.root, width = 30)
			self.label_class_tutor= tkinter.Label(self.root, text = '班级班主任: ')
			self.input_class_tutor = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_class_no.place(x=60, y= 60)
			self.label_class_depart.place(x=38, y= 85)
			self.label_class_year.place(x=38, y= 110)
			self.label_class_tutor.place(x=45, y= 135)
			self.input_class_no.place(x=130, y=60)
			self.input_class_depart.place(x=130, y=85)
			self.input_class_year.place(x=130, y=110)
			self.input_class_tutor.place(x=130, y=135)
			self.button_ok.place(x=140, y=170)
			self.button_back.place(x=240, y=170)
		if self.index == "教师数据":
			self.root.geometry('450x350+400+200')
			self.label_teacher_no = tkinter.Label(self.root, text = '教师编号: ')
			self.input_teacher_no = tkinter.Entry(self.root, width = 30)
			self.label_teacher_name = tkinter.Label(self.root, text = '教师姓名: ')
			self.input_teacher_name = tkinter.Entry(self.root, width = 30)
			self.label_teacher_sex= tkinter.Label(self.root, text = '教师性别: ')
			self.input_teacher_sex = tkinter.Entry(self.root, width = 30)
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
			self.label_teacher_no.place(x=60, y= 30)
			self.label_teacher_name.place(x=60, y= 55)
			self.label_teacher_sex.place(x=60, y= 80)
			self.label_teacher_polistatus.place(x=38, y= 105)
			self.label_professional.place(x=60, y= 130)
			self.label_teacher_tel.place(x=60, y= 155)
			self.label_teacher_depart.place(x=60, y= 180)
			self.label_teacher_college.place(x=60, y= 205)
			self.label_teacher_entry.place(x=60, y= 230)
			self.label_teacher_pwd.place(x=60, y= 255)
			self.input_teacher_no.place(x=130, y=30)
			self.input_teacher_name.place(x=130, y=55)
			self.input_teacher_sex.place(x=130, y=80)
			self.input_teacher_polistatus.place(x=130, y=105)
			self.input_professional.place(x=130, y=130)
			self.input_teacher_tel.place(x=130, y=155)
			self.input_teacher_depart.place(x=130, y=180)
			self.input_teacher_college.place(x=130, y=205)
			self.input_teacher_entry.place(x=130, y=230)
			self.input_teacher_pwd.place(x=130, y=255)
			self.button_ok.place(x=140, y=295)
			self.button_back.place(x=240, y=295)
		if self.index == "教室数据":
			self.root.geometry('450x220+400+200')
			self.label_class_room_no = tkinter.Label(self.root, text = '教室编号: ')
			self.input_class_room_no = tkinter.Entry(self.root, width = 30)
			self.label_class_room_name = tkinter.Label(self.root, text = '教室名称: ')
			self.input_class_room_name = tkinter.Entry(self.root, width = 30)
			self.label_class_room_building = tkinter.Label(self.root, text = '教室所在教学楼: ')
			self.input_class_room_building = tkinter.Entry(self.root, width = 30)
			self.label_class_room_capacity = tkinter.Label(self.root, text = '教室可容纳人数: ')
			self.input_class_room_capacity = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_class_room_no.place(x=60, y= 60)
			self.label_class_room_name.place(x=60, y= 85)
			self.label_class_room_building.place(x=24, y= 110)
			self.label_class_room_capacity.place(x=24, y= 135)
			self.input_class_room_no.place(x=130, y=60)
			self.input_class_room_name.place(x=130, y=85)
			self.input_class_room_building.place(x=130, y=110)
			self.input_class_room_capacity.place(x=130, y=135)
			self.button_ok.place(x=140, y=175)
			self.button_back.place(x=240, y=175)
		if self.index == "课程数据":
			self.root.geometry('450x280+400+200')
			self.label_course_no = tkinter.Label(self.root, text = '课程编号: ')
			self.input_course_no = tkinter.Entry(self.root, width = 30)
			self.label_course_name = tkinter.Label(self.root, text = '课程名称: ')
			self.input_course_name = tkinter.Entry(self.root, width = 30)
			self.label_course_depart = tkinter.Label(self.root, text = '课程开设学院: ')
			self.input_course_depart = tkinter.Entry(self.root, width = 30)
			self.label_course_kind = tkinter.Label(self.root, text = '课程类型: ')
			self.input_course_kind = tkinter.Entry(self.root, width = 30)
			self.label_course_period = tkinter.Label(self.root, text = '课程课时: ')
			self.input_course_period = tkinter.Entry(self.root, width = 30)
			self.label_course_describe = tkinter.Label(self.root, text = '课程描述: ')
			self.input_course_describe = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_course_no.place(x=60, y= 60)
			self.label_course_name.place(x=60, y= 85)
			self.label_course_depart.place(x=38, y= 110)
			self.label_course_kind.place(x=60, y= 135)
			self.label_course_period .place(x=60, y= 160)
			self.label_course_describe.place(x=60, y= 185)
			self.input_course_no.place(x=130, y=60)
			self.input_course_name.place(x=130, y=85)
			self.input_course_depart.place(x=130, y=110)
			self.input_course_kind.place(x=130, y=135)
			self.input_course_period.place(x=130, y= 160)
			self.input_course_describe.place(x=130, y= 185)
			self.button_ok.place(x=140, y=225)
			self.button_back.place(x=240, y=225)
		if self.index == "学生数据":
			self.root.geometry('450x400+400+200')
			self.label_student_no = tkinter.Label(self.root, text = '学生学号: ')
			self.input_student_no = tkinter.Entry(self.root, width = 30)
			self.label_class_no = tkinter.Label(self.root, text = '所在班级: ')
			self.input_class_no= tkinter.Entry(self.root, width = 30)
			self.label_student_name = tkinter.Label(self.root, text = '学生姓名: ')
			self.input_student_name = tkinter.Entry(self.root, width = 30)
			self.label_student_sex= tkinter.Label(self.root, text = '学生性别: ')
			self.input_student_sex = tkinter.Entry(self.root, width = 30)
			self.label_student_birth = tkinter.Label(self.root, text = '学生出生年月日: ')
			self.input_student_birth = tkinter.Entry(self.root, width = 30)
			self.label_student_polistatus = tkinter.Label(self.root, text = '学生政治面貌: ')
			self.input_student_polistatus = tkinter.Entry(self.root, width = 30)
			self.label_student_nation = tkinter.Label(self.root, text = '民族: ')
			self.input_student_nation = tkinter.Entry(self.root, width = 30)
			self.label_student_home = tkinter.Label(self.root, text = '家庭住址: ')
			self.input_student_home = tkinter.Entry(self.root, width = 30)
			self.label_student_home_tel = tkinter.Label(self.root, text = '家庭电话: ')
			self.input_student_home_tel = tkinter.Entry(self.root, width = 30)
			self.label_student_spec = tkinter.Label(self.root, text = '所在专业: ')
			self.input_student_spec = tkinter.Entry(self.root, width = 30)
			self.label_student_entry = tkinter.Label(self.root, text = '入学年份: ')
			self.input_student_entry = tkinter.Entry(self.root, width = 30)
			self.label_student_pwd = tkinter.Label(self.root, text = '系统登入密码: ')
			self.input_student_pwd = tkinter.Entry(self.root, width = 30)
			self.button_ok = tkinter.Button(self.root, command = self.ok_interface,
			text = "确定", width = 10)
			self.button_back = tkinter.Button(self.root, command = self.back_interface,
			text = "返回上一步", width = 10)
			self.label_student_no.place(x=60, y= 30)
			self.label_class_no.place(x=60, y= 55)
			self.label_student_name.place(x=60, y= 80)
			self.label_student_sex.place(x=60, y= 105)
			self.label_student_birth.place(x=28, y= 130)
			self.label_student_polistatus.place(x=38, y= 155)
			self.label_student_nation.place(x=75, y= 180)
			self.label_student_home.place(x=60, y= 205)
			self.label_student_home_tel.place(x=60, y= 230)
			self.label_student_spec.place(x=60, y= 255)
			self.label_student_entry.place(x=60, y= 280)
			self.label_student_pwd.place(x=38, y= 305)
			self.input_student_no.place(x=130, y=30)
			self.input_class_no.place(x=130, y=55)
			self.input_student_name.place(x=130, y=80)
			self.input_student_sex.place(x=130, y=105)
			self.input_student_birth.place(x=130, y= 130)
			self.input_student_polistatus.place(x=130, y= 155)
			self.input_student_nation.place(x=130, y= 180)
			self.input_student_home.place(x=130, y= 205)
			self.input_student_home_tel.place(x=130, y= 230)
			self.input_student_spec.place(x=130, y= 255)
			self.input_student_entry.place(x=130, y= 280)
			self.input_student_pwd.place(x=130, y= 305)
			self.button_ok.place(x=140, y=345)
			self.button_back.place(x=240, y=345)

	def ok_interface(self):
		if self.index == "学院数据":
			string_college_id = self.input_college_id.get()
			string_college_abstract = self.input_college_abstract.get()
			if string_college_id == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '学院名称未输入')
				return None
			opr_string = "\
				insert into college\
				values('" + string_college_id + "','" \
				 + string_college_abstract + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "专业数据":
			string_major_no = self.input_major_no.get()
			string_major_depart = self.input_major_depart.get()
			string_major_name = self.input_major_name.get()
			if string_major_no == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '专业编号未输入')
				return None
			'''
			opr_string = "\
				insert into major\
				values(" + string_major_no + ",'"\
				+ string_major_depart + "','"\
				+ string_major_name + "')"
			'''
			opr_string = "\
				insert into major\
				values(" + string_major_no + ",'"\
				+ string_major_name + "','"\
				+ string_major_depart + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "班级数据":
			string_class_no = self.input_class_no.get()
			string_class_depart = self.input_class_depart.get()
			string_class_year = self.input_class_year.get()
			string_class_tutor = self.input_class_tutor.get()
			if (string_class_no == '') or (string_class_year):
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '输入不规范')
				return None
			opr_string = "\
				insert into class\
				values(" + string_class_no + ",'"\
				+ string_class_depart + "',"\
				+ string_class_year + ",'"\
				+ string_class_tutor + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "教师数据":
			string_teacher_no = self.input_teacher_no.get()
			string_teacher_name = self.input_teacher_name.get()
			string_teacher_sex = self.input_teacher_sex.get()
			string_teacher_polistatus = self.input_teacher_polistatus.get()
			string_professional = self.input_professional.get()
			string_teacher_tel = self.input_teacher_tel.get()
			string_teacher_depart = self.input_teacher_depart.get()
			string_teacher_college = self.input_teacher_college.get()
			string_teacher_entry = self.input_teacher_entry.get()
			string_teacher_pwd = self.input_teacher_pwd.get()
			if string_teacher_no == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '教师编号未输入')
				return None
			opr_string = "\
				insert into teacher\
				values(" + string_teacher_no + ",'"\
				+ string_teacher_name + "','"\
				+ string_teacher_sex + "','"\
				+ string_teacher_polistatus + "','"\
				+ string_professional + "',"\
				+ string_teacher_tel + ",'"\
				+ string_teacher_depart + "','"\
				+ string_teacher_college + "',"\
				+ string_teacher_entry + ",'"\
				+ string_teacher_pwd + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "教室数据":
			string_class_room_no = self.input_class_room_no.get()
			string_class_room_name = self.input_class_room_name.get()
			string_class_room_building = self.input_class_room_building.get()
			string_class_room_capacity = self.input_class_room_capacity.get()
			if string_class_room_no == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '教室编号未输入')
				return None
			opr_string = "\
				insert into class_room\
				values(" + string_class_room_no + ",'"\
				+ string_class_room_name + "','"\
				+ string_class_room_building + "','"\
				+ string_class_room_capacity + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "课程数据":
			string_course_no = self.input_course_no.get()
			string_course_name = self.input_course_name.get()
			string_course_depart = self.input_course_depart.get()
			string_course_kind = self.input_course_kind.get()
			string_course_period = self.input_course_period.get()
			string_course_describe = self.input_course_describe.get()
			if string_course_no == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '课程编号未输入')
				return None
			opr_string = "\
				insert into course\
				values(" + string_course_no + ",'"\
				+ string_course_name + "','"\
				+ string_course_depart + "','"\
				+ string_course_kind + "',"\
				+ string_course_period + ",'"\
				+ string_course_describe + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')
		if self.index == "学生数据":
			string_student_no = self.input_student_no.get()
			string_class_no = self.input_class_no.get()
			string_student_name = self.input_student_name.get()
			string_student_sex = self.input_student_sex.get()
			string_student_birth = self.input_student_birth.get()
			string_student_polistatus = self.input_student_polistatus.get()
			string_student_nation = self.input_student_nation.get()
			string_student_home = self.input_student_home.get()
			string_student_home_tel = self.input_student_home_tel.get()
			string_student_spec = self.input_student_spec.get()
			string_student_entry = self.input_student_entry.get()
			string_student_pwd = self.input_student_pwd.get()
			if string_student_no == '':
				tkinter.messagebox.showinfo(title = '教育管理系统', message = '学生学号未输入')
				return None
			opr_string = "\
				insert into student\
				values("\
				+ string_student_no + ","\
				+ string_class_no + ",'"\
				+ string_student_name + "','"\
				+ string_student_sex + "','"\
				+ string_student_birth + "','"\
				+ string_student_polistatus + "','"\
				+ string_student_nation + "','"\
				+ string_student_home + "','"\
				+ string_student_home_tel + "','"\
				+ string_student_spec + "',"\
				+ string_student_entry + ",'"\
				+ string_student_pwd + "')"
			self.cursor.execute(opr_string)
			self.cnxn.commit()
			tkinter.messagebox.showinfo(title = '教育管理系统', message = '插入成功')

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