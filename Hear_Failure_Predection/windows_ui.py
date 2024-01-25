from tkinter import *
import requests
import pandas as pd
from PIL import ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
import tkinter as ttk
import numpy as np
from matplotlib.figure import Figure
from tkinter import messagebox, filedialog
from ttkbootstrap import Style

from ttkbootstrap.widgets import Meter

#report generation file
import report_gen as rep_gen









class Heart_Failure:

	def __init__(self,window):
		self.window = window
		self.window.title('Heart Failure Prediction')
		self.window.geometry('1440x750+50+10')
		self.window.resizable(True,True)
		#====Label====#
		main1_Label = Label(self.window, text='HEART FAILURE PREDICTIOR', font=('Impact', 30)).place(x=500, y=10)

		
		#=======personal Data Frame====#
		frame_presonnel= Frame(self.window,bg='white')
		frame_presonnel.place(x=20,y=80,height=350,width=500)
		titel = Label(frame_presonnel,text='Personal Data',font=('Impact',20,'bold'),fg='#d77337',bg='white').place(x=30,y=20)
		age_label= Label(frame_presonnel,text='Age',font=('Goudy old style',20,'bold'),fg='gray',bg='white').place(x=30,y=80)
		self.age_entery = Entry(frame_presonnel,font=('time new roman',15),bg='lightgray')
		self.age_entery.place(x=30,y=120,width=250,height=25)

		time_label = Label(frame_presonnel, text='Time', font=('Goudy old style', 20, 'bold'), fg='gray',bg='white').place(x=30, y=150)
		self.time_entery = Entry(frame_presonnel, font=('time new roman', 15), bg='lightgray')
		self.time_entery.place(x=30,y=180,width=250,height=25)

		#gender
		gender = Label(frame_presonnel,text='Gender',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=320,y=80)
		self.sex = IntVar()
		C1 = Checkbutton(frame_presonnel, text="Male", variable=self.sex, onvalue=1, offvalue=2).place(x=320, y=120)
		C2 = Checkbutton(frame_presonnel, text="Female", variable=self.sex, onvalue=0, offvalue=2).place(x=380, y=120)

		#smoke
		smoke_label = Label(frame_presonnel, text='Smoke', font=('Goudy old style', 15, 'bold'), fg='gray',bg='white').place(x=320, y=150)
		self.smoke = IntVar()
		C3 = Checkbutton(frame_presonnel, text="Yes", variable=self.smoke, onvalue=1, offvalue=2).place(x=320, y=180)
		C4 = Checkbutton(frame_presonnel, text="No", variable=self.smoke, onvalue=0, offvalue=2).place(x=380, y=180)

		#diabetes
		diabetes_label = Label(frame_presonnel, text='Diabetes', font=('Goudy old style', 15, 'bold'), fg='gray', bg='white').place(x=320, y=210)
		self.diabetes = IntVar()
		C5 = Checkbutton(frame_presonnel, text="Yes", variable=self.diabetes, onvalue=1, offvalue=2).place(x=320, y=240)
		C6 = Checkbutton(frame_presonnel, text="No", variable=self.diabetes, onvalue=0, offvalue=2).place(x=380, y=240)

		# =======blood Data Frame====#
		frame_blood = Frame(self.window, bg='white')
		frame_blood.place(x=900, y=80, height=350, width=500)
		blood_titel = Label(frame_blood,text='Blood Sample Data',font=('Impact',20,'bold'),fg='#d77337',bg='white').place(x=30,y=20)

		#creatinine_phosphokinase
		creatinine_phosphokinase_label = Label(frame_blood,text='Creatinine Phosphokinase',font=('Goudy old style',20,'bold'),fg='gray',bg='white').place(x=30,y=80)
		self.creatinine_phosphokinase_entery = Entry(frame_blood, font=('time new roman', 15), bg='lightgray')
		self.creatinine_phosphokinase_entery.place(x=30, y=120, width=250, height=25)

		#platelets
		platelets_label = Label(frame_blood, text='Platelets',font=('Goudy old style', 20, 'bold'), fg='gray', bg='white').place(x=30,y=150)
		self.platelets_entery = Entry(frame_blood, font=('time new roman', 15), bg='lightgray')
		self.platelets_entery.place(x=30, y=180, width=250, height=25)

		#serum_creatinine
		serum_creatinine_label = Label(frame_blood, text='Serum Creatinine', font=('Goudy old style', 20, 'bold'), fg='gray',bg='white').place(x=30, y=205)
		self.serum_creatinine_entery = Entry(frame_blood, font=('time new roman', 15), bg='lightgray')
		self.serum_creatinine_entery.place(x=30, y=240, width=250, height=25)

		#serum_sodium
		serum_sodium_label = Label(frame_blood, text='Serum Sodium', font=('Goudy old style', 20, 'bold'),fg='gray', bg='white').place(x=30, y=270)
		self.serum_sodium_entery = Entry(frame_blood, font=('time new roman', 15), bg='lightgray')
		self.serum_sodium_entery.place(x=30, y=310, width=250, height=25)

		#anaemia
		anaemia = Label(frame_blood, text='Anaemia', font=('Goudy old style', 15, 'bold'), fg='gray',bg='white').place(x=350, y=80)
		self.yes = IntVar()
		C7 = Checkbutton(frame_blood, text="Yes", variable=self.yes, onvalue=1, offvalue=2).place(x=350, y=120)
		C8 = Checkbutton(frame_blood, text="No", variable=self.yes, onvalue=0, offvalue=2).place(x=410, y=120)



		# =======Heart Condition Frame====#
		frame_heart = Frame(self.window, bg='white')
		frame_heart.place(x=460, y=450, height=190, width=500)
		heart_titel = Label(frame_heart, text='Heart Condition Data', font=('Impact', 20, 'bold'), fg='#d77337',bg='white').place(x=30, y=20)

		#ejection_fraction
		ejection_fraction_label = Label(frame_heart, text='Ejection Fraction', font=('Goudy old style', 20, 'bold'), fg='gray',bg='white').place(x=30, y=80)
		self.ejection_fraction_entery = Entry(frame_heart, font=('time new roman', 15), bg='lightgray')
		self.ejection_fraction_entery.place(x=30, y=120, width=250, height=25)

		#HBP
		high_blood_pressure = Label(frame_heart, text='High Blood', font=('Goudy old style', 18, 'bold'), fg='gray',bg='white').place(x=320, y=80)
		self.HBP = IntVar()
		C9 = Checkbutton(frame_heart, text="Yes", variable=self.HBP, onvalue=1, offvalue=2).place(x=320, y=120)
		C10 = Checkbutton(frame_heart, text="No", variable=self.HBP, onvalue=0, offvalue=2).place(x=380, y=120)

		test_b=Button(self.window,text='Calculate',command=self.predict,fg='white',bg='#d77337',font=('time new roman',15),width=8,height=1).place(x=670,y=620)
		
		

	#calling the API and returning the predicition
	def modelCall(self, sample):
		response = requests.put("http://127.0.0.1:5000/pred/1", sample)
		response = requests.get("http://127.0.0.1:5000/pred/1")
		return response.json()[1:len(response.json())-1]

	#clear the fields
	def delete(self):
		enterys = ['serum_sodium_entery', 'age_entery', 'creatinine_phosphokinase_entery',
					 'ejection_fraction_entery', 'platelets_entery', 'serum_creatinine_entery', 'time_entery']
		for entery in enterys:
			eval('self.'+entery).delete(0, END)

	#get all values from the text fields
	def get_values(self):
		try:
			self.age_value = int(self.age_entery.get())
			self.creatinine_phosphokinase_value = int(self.creatinine_phosphokinase_entery.get())
			self.diabetes_value = int(self.diabetes.get())
			self.ejection_fraction_value = int(self.ejection_fraction_entery.get())
			self.platelets_value = float(self.platelets_entery.get())
			self.serum_creatinine_value = float(self.serum_creatinine_entery.get())
			self.time_value = int(self.time_entery.get())
			self.anaemia_value = int(self.yes.get())
			self.high_blood_pressure_value = int(self.HBP.get())
			self.serum_sodium_value = int(self.serum_sodium_entery.get())
			self.sex_value = int(self.sex.get())
			self.smoke_value = int(self.smoke.get())
			self.values = self.values = {
							"age": self.age_value,
							"anaemia": self.anaemia_value,
							"creatinine_phosphokinase": self.creatinine_phosphokinase_value,
							"diabetes":self.diabetes_value,
							"ejection_fraction": self.ejection_fraction_value,
							"high_blood_pressure": self.high_blood_pressure_value,
							"platelets": self.platelets_value,
							"serum_creatinine": self.serum_creatinine_value,
							"serum_sodium": self.serum_sodium_value,
							"sex": self.sex_value,
							"smoking": self.smoke_value,
							"time": self.time_value
							}
			return self.values
		except:
			if all([self.age_entery.get(),self.creatinine_phosphokinase_entery.get(),self.ejection_fraction_entery.get(),self.platelets_entery.get(),self.serum_creatinine_entery.get(),self.serum_sodium_entery.get(),self.time_entery.get()])== False:
				messagebox.showerror('Error','All Fields Are Required',parent=self.window)
			else :
				messagebox.showerror('Error', 'Wrong Data Type', parent=self.window)


	
				



	# get all values and generate result page
	def predict(self):
		sample = self.get_values()
		if sample is not None:
			statues = messagebox.askyesno('Data Checking', 'Want to edit the data ? ', parent=self.window)
			if statues == False:
				self.delete()
				self.prediction_result = float(self.modelCall(sample))
				self.prediction_result = round(self.prediction_result * 100, 2)
				self.predict_frame = Frame(self.window)
				self.predict_frame.place(x=0,y=0,width=1440,height=750)
				self.show_fram(self.predict_frame)
				self.m2 = Meter(metersize=170, padding=20, amountused=self.prediction_result, amounttotal=100, labeltext='Heart failure chance', textappend='%',
					 meterstyle='info.TMeter', stripethickness=10, interactive=False)
				self.m2.grid(row=0, column=3, padx=580, pady=190)
				main1_Label = Label(self.predict_frame, text='HEART FAILURE PREDICTION', font=('Impact', 30)).place(x=480, y=10)
				generate_full_report = Button(self.predict_frame,text='Generate Report',command= self.report,fg='white',bg='#d77337',font=('time new roman',15),width=15,height=1).place(x=540,y=620) 
				back_boutton = Button(self.predict_frame,text='Back',command= self.destroyFrame,fg='white',bg='#d77337',font=('time new roman',15),width=8,height=1).place(x=730,y=620)
				
	
	#destroy results page
	def destroyFrame(self):
		self.predict_frame.destroy()
		self.m2.destroy()





		
		
		

	

	#show resluts page
	def show_fram(self,fram):
		fram.tkraise


	#generate report
	def report(self):
		file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF file", ".pdf"),("All Files", ".pdf") ))
		if file_path:
			rep_gen.generate_report(self.prediction_result, self.age_value, self.ejection_fraction_value, self.serum_creatinine_value, self.platelets_value, self.serum_sodium_value, file_path)
			messagebox.showinfo("Operation Status", "Report Has Been Generated", parent=self.predict_frame)
		else:
			pass





if __name__ == '__main__':
	style = Style('solar')
	window = style.master
	win = Heart_Failure(window)
	mainloop()