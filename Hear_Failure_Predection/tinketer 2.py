from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Heart_Failure:
    def __init__(self,window):
        self.window = window
        self.window.title('Heart Failure Prediction')
        self.window.geometry('1440x750+50+10')
        self.window.resizable(False,False)
        #====backgraound====#
        self.bg=ImageTk.PhotoImage(file=r'D:\yousef\term8\Project1\heart.jpg')
        self.bg_image= Label(self.window,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        main_Label = Label(self.window, text='HEART FAILURE PREDICTION', font=('Impact', 30)).place(x=500, y=10)

        #=======personal Data Frame====#
        frame_presonnel= Frame(self.window,bg='white')
        frame_presonnel.place(x=20,y=80,height=350,width=500)
        titel = Label(frame_presonnel,text='Perssonel Data',font=('Impact',20,'bold'),fg='#d77337',bg='white').place(x=30,y=20)
        age_label= Label(frame_presonnel,text='Age',font=('Goudy old style',20,'bold'),fg='gray',bg='white').place(x=30,y=80)
        self.age_entery = Entry(frame_presonnel,font=('time new roman',15),bg='lightgray')
        self.age_entery.place(x=30,y=120,width=250,height=25)

        time_label = Label(frame_presonnel, text='Time', font=('Goudy old style', 20, 'bold'), fg='gray',bg='white').place(x=30, y=150)
        self.time_entery = Entry(frame_presonnel, font=('time new roman', 15), bg='lightgray')
        self.time_entery.place(x=30,y=180,width=250,height=25)

        #gender
        gender = Label(frame_presonnel,text='Gender',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=320,y=80)
        self.sex = IntVar()
        C1 = Checkbutton(frame_presonnel, text="Mail", variable=self.sex, onvalue=1, offvalue=2).place(x=320, y=120)
        C2 = Checkbutton(frame_presonnel, text="Female", variable=self.sex, onvalue=0, offvalue=2).place(x=380, y=120)

        #somke
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
        high_blood_pressure = Label(frame_heart, text='High_Blood', font=('Goudy old style', 18, 'bold'), fg='gray',bg='white').place(x=320, y=80)
        self.HBP = IntVar()
        C9 = Checkbutton(frame_heart, text="Yes", variable=self.HBP, onvalue=1, offvalue=2).place(x=320, y=120)
        C10 = Checkbutton(frame_heart, text="No", variable=self.HBP, onvalue=0, offvalue=2).place(x=380, y=120)

        test_b=Button(self.window,text='test',command=self.predict,fg='white',bg='#d77337',font=('time new roman',15),width=8,height=1).place(x=670,y=620)

    def model(self,sample):
        pass

    # write model code here

    def delete(self):
        enterys = ['serum_sodium_entery', 'age_entery', 'creatinine_phosphokinase_entery',
                   'ejection_fraction_entery', 'platelets_entery', 'serum_creatinine_entery', 'time_entery']
        for entery in enterys:
            eval('self.'+entery).delete(0, END)

    def get_values(self):
        try:
            self.age_value = float(self.age_entery.get())
            self.creatinine_phosphokinase_value = float(self.creatinine_phosphokinase_entery.get())
            self.diabetes_value = int(self.diabetes.get())
            self.ejection_fraction_value = float(self.ejection_fraction_entery.get())
            self.platelets_value = float(self.platelets_entery.get())
            self.serum_creatinine_value = float(self.serum_creatinine_entery.get())
            self.time_value = float(self.time_entery.get())
            self.anaemia_value = int(self.yes.get())
            self.high_blood_pressure_value = int(self.HBP.get())
            self.serum_sodium_value = float(self.serum_sodium_entery.get())
            self.sex_value = int(self.sex.get())
            self.smoke_value = int(self.smoke.get())
            self.values = [self.age_value, self.anaemia_value, self.creatinine_phosphokinase_value, self.diabetes_value, self.ejection_fraction_value,self.high_blood_pressure_value, self.platelets_value, self.serum_creatinine_value, self.serum_sodium_value, self.sex_value,self.smoke_value, self.time_value]
            return self.values
        except:
            if all([self.age_entery.get(),self.creatinine_phosphokinase_entery.get(),self.ejection_fraction_entery.get(),self.platelets_entery.get(),self.serum_creatinine_entery.get(),self.serum_sodium_entery.get(),self.time_entery.get()])== False:
                messagebox.showerror('Error','All Fields Are Required',parent=self.window)
            else :
                messagebox.showerror('Error', 'Wrong Data Type', parent=self.window)

    def predict(self):
        sample = self.get_values()
        if sample is not None:
            self.delete()
            self.predict_frame = Frame(self.window)
            self.predict_frame.place(x=0,y=0,width=1440,height=750)
            self.bg1 = ImageTk.PhotoImage(file=r'D:\yousef\term8\Project1\heart.jpg')
            self.bg1_image = Label(self.predict_frame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
            main1_Label = Label(self.predict_frame, text='HEART FAILURE PREDICTION', font=('Impact', 30)).place(x=500, y=10)
            self.show_fram(self.predict_frame)
    def show_fram(self,fram):
        fram.tkraise




if __name__ == '__main__':
    window=Tk()
    win = Heart_Failure(window)
    mainloop()