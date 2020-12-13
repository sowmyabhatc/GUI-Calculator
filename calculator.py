from tkinter import *
from tkinter import ttk
from math import*
import csv


class Calculator:
  
    calc_value = 0.0
    div_ = False
    mult_ = False
    add_ = False
    sub_ = False
    asin_ = False
    acos_ = False
    atan_ = False
    alog_ =False
    aln_ =False
    aac_=False
    afact_=False
    asquare_=False
    acube_=False
    apovn_=False
    asqrt_=False
    acurt_=False
    apie_=False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)


    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False


    def math_button_press(self, value):
        if self.isfloat(str(self.number_entry.get())):
            self.add_ = False
            self.sub_ = False
            self.mult_ = False
            self.div_= False
            self.asin_ = False
            self.acos_ = False
            self.atan_ = False
            self.alog_ =False
            self.aln_=False
            self.aac_=False
            self.afact_=False
            self.asquare_=False
            self.acube_=False
            self.apovn_=False
            self.asqrt_=False
            self.acurt_=False
            self.apie_=False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                print("/ Pressed")
                self.div_ = True
            elif value == "*":
                print("* Pressed")
                self.mult_ = True
            elif value == "+":
                print("+ Pressed")
                self.add_ = True
            elif value == "sin":
                print("sin Pressed")
                self.asin_ = True 
            elif value == "cos":
                print("cos Pressed")
                self.acos_= True
            elif value == "tan":
                print("tan Pressed")
                self.atan_=True
            elif value== "log":
                print("log pressed")
                self.alog_=True
            elif value =="ln":
                print("ln pressed")
                self.aln_=True
            elif value=="AC":
                print("AC pressed")
                self.aac_=True    
            elif value=='n!':
                print("factorial pressed")
                self.afact_=True 
            elif value=='x^2':
                print("square pressed")
                self.asquare_=True
            elif value=='x^3':
                print("cube pressed")
                self.acube_=True
            elif value=='x^n':
                print("power n pressed")
                self.apovn_=True
            elif value=='√x':
                print("squareroot pressed")
                self.asqrt_=True 
            elif value=='∛x':
                print(" cuberoot pressed")
                self.acurt_=True
            elif value=='π':
                print(" pie pressed")
                self.apie_=True
            else:
                print("- Pressed")
                self.sub_ = True
            self.number_entry.delete(0, "end")
            



    def equal_button_press(self):  
        
        if self.add_ or self.sub_ or self.mult_ or self.div_ or self.asin_ or self.acos_  or self.atan_  or self.alog_  or self.aln_ or self.aac_ or  self.afact_ or self.asquare_ or self.acube_ or self.apovn_ or  self.apovn_ or self.acurt_:

            if self.add_:
                solution = self.calc_value + float(self.entry_value.get())
                self.resultlist.append(str(self.calc_value)+" + "+str(float(self.entry_value.get()))+" = "+str(solution))
            elif self.sub_:
                solution = self.calc_value - float(self.entry_value.get())
                self.resultlist.append(str(self.calc_value)+" - "+str(float(self.entry_value.get()))+" = "+str(solution))
            elif self.mult_:
                solution = self.calc_value * float(self.entry_value.get())
                self.resultlist.append(str(self.calc_value)+" * "+str(float(self.entry_value.get()))+" = "+str(solution))
            
            elif self.div_:
                solution = self.calc_value / float(self.entry_value.get())
                self.resultlist.append(str(self.calc_value)+" / "+str(float(self.entry_value.get()))+" = "+str(solution))
           
            elif self.asin_:
                solution = sin(float(self.calc_value))
                self.resultlist.append("Sin"+str((float(self.calc_value)))+" = "+str(solution))
            elif self.acos_:
                solution=cos(float(self.calc_value))
                self.resultlist.append("Cos"+str((float(self.calc_value)))+" = "+str(solution))
            elif self.atan_:
                solution=tan(float(self.calc_value))
                self.resultlist.append("tan"+str((float(self.calc_value)))+" = "+str(solution))
            elif self.alog_:
                solution=log(float(self.calc_value),10)
                self.resultlist.append("log"+str((float(self.calc_value)))+" = "+str(solution))
            elif self.aln_:
                solution=log(float(self.calc_value),2.7183)
                self.resultlist.append("ln"+str((float(self.calc_value)))+" = "+str(solution))
            elif self.aac_:
                solution=self.number_entry.delete(0, "end")
                
            elif self.afact_:
                solution=factorial(int(self.calc_value))
                self.resultlist.append(str((float(self.calc_value)))+"!"+" = "+str(solution))
            elif self.asquare_:
                solution=(float(self.calc_value))**2
                self.resultlist.append(str(self.calc_value)+"**2"+" = "+str(solution))
            elif self.acube_:
                solution=(float(self.calc_value))**3
                self.resultlist.append(str(self.calc_value)+"**3"+" = "+str(solution))
            elif self.apovn_:
                solution=(float(self.calc_value))**(float(self.entry_value.get()))
                self.resultlist.append(str(self.calc_value)+"**"+str(self.entry_value.get())+" = "+str(solution))
            elif self.asqrt_:
                solution=((float(self.calc_value))**0.5)
                self.resultlist.append(str((self.calc_value))+"**0.5"+" = "+str(solution))
                
            elif self.acurt_:
                solution=((float(self.calc_value))**(1/3))
                self.resultlist.append(str((self.calc_value))+"**(1/3)"+" = "+str(solution))
            
            else:
                solution = self.calc_value / float(self.entry_value.get())
            
            
           
            print(self.calc_value, " ",self.entry_value.get(), " ", solution)
        
            self.number_entry.delete(0, "end")

            self.number_entry.insert(0, solution)
            
    
            
    def save(self):
        print(self.resultlist)
        with open("d:\\calci.txt","a") as f:
            for i in self.resultlist:
                self.resultlist.remove(i)
                f.writelines(i+'\n')   
                
                
    def delete(self):
        file = open("d:\\calci.txt","r+")
        file.truncate(0)
        file.close()

            
        

    def __init__(self,root):
        self.resultlist = []
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("860x440")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        # Create the text entry box
        self.number_entry = ttk.Entry(root,
                        textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # ----- 1st Row -----

        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ----- 2nd Row -----

        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # ----- 3rd Row -----

        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # ----- 4th Row -----

        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.math_button_press('AC')).grid(row=4, column=0)

        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.button_apie = ttk.Button(root, text="π", command=lambda: self.button_press('3.14333')).grid(row=4, column=2)

        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

        #------- 5th Row -------
        self.button_asin = ttk.Button(root, text="sin", command=lambda: self.math_button_press('sin')).grid(row=5, column=0)
        
        self.button_acos = ttk.Button(root, text="cos", command=lambda: self.math_button_press('cos')).grid(row=5, column=1)
        
        self.button_atan = ttk.Button(root, text="tan", command=lambda: self.math_button_press('tan')).grid(row=5, column=2)
        
        self.button_alog = ttk.Button(root, text="log", command=lambda: self.math_button_press('log')).grid(row=5, column=3)

        #-------  6th Row-------
        self.button_aln = ttk.Button(root, text="ln", command=lambda: self.math_button_press('ln')).grid(row=6, column=0)
        
        self.button_afact = ttk.Button(root, text="n!", command=lambda: self.math_button_press('n!')).grid(row=6, column=1)
        
        self.button_asquare= ttk.Button(root, text="x^2", command=lambda: self.math_button_press('x^2')).grid(row=6, column=2)
         
        self.button_acube = ttk.Button(root, text="x^3", command=lambda: self.math_button_press('x^3')).grid(row=6, column=3)
          
        
        
        #--------  7th Row -------
        self.button_apovn = ttk.Button(root, text="x^n", command=lambda: self.math_button_press('x^n')).grid(row=7, column=0)   
        
        self.button_asqrt = ttk.Button(root, text="√x", command=lambda: self.math_button_press('√x')).grid(row=7, column=1)
            
        self.button_acurt = ttk.Button(root, text="∛x", command=lambda: self.math_button_press('∛x')).grid(row=7, column=2)
        
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=7, column=3)
        #--------  8th Row -------
        self.button_asave = ttk.Button(root, text="Save File", command=lambda: self.save()).grid(row=8, column=0)
        
        self.button_adel = ttk.Button(root, text="Clear File", command=lambda: self.delete()).grid(row=8, column=1)
      
       
        
            
    

root = Tk()
calc = Calculator(root)
root.mainloop()

   

