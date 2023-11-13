from tkinter import * #Import Tkinter
import tkinter.messagebox

class loancal: #Create Class

    def __init__(self):

        #size and title
        global root 
        root = Tk()
        root.title("Loan Calculator")
        root.geometry("550x400")

        #add labels
        Label(root,text="LOAN CALCULATOR",font=20,fg="white",bg="gray").place(x=175,y=5)
        Label(root,text="Loan Amount",font=10).place(x=65,y=50)
        Label(root,text="Interest Rate",font=10).place(x=65,y=80)
        Label(root,text="Loan Term",font=10).place(x=65,y=110)
        Label(root,text="% per year",font=5).place(x=400,y=80)
        Label(root,text="years",font=5).place(x=295,y=110)
        Label(root,text="months",font=5).place(x=390,y=110)
        
        Label(root,text="Total Payment :  ",font=10,fg="Blue").place(x=80, y=200)
        Label(root,text="Monthly Payment :  ",font=10,fg="Blue").place(x=80,y=225)
        Label(root,text="Total Interest :  ",font=10,fg="Blue").place(x=80,y=250)
        Label(root,text="Annual Payment :  ",font=10,fg="Blue").place(x=80,y=275)
        
        #add entry block
        self.a = StringVar()
        self.r = StringVar()
        self.y = StringVar()
        self.m = StringVar()
        self.amount = Entry(root,textvariable=self.a)
        self.amount.place(x=260,y=50)
        self.ir = Entry(root,textvariable=self.r)
        self.ir.place(x=260,y=80)
        self.years = Entry(root,textvariable=self.y,width=5)
        self.years.place(x=260,y=115)
        self.months = Entry(root,textvariable=self.m,width=5)
        self.months.place(x=350,y=115)
        
        #result label
        self.resultTotalPay = StringVar()
        Label(root,textvariable=self.resultTotalPay,font=10,fg="Red").place(x=250,y=200)
        self.resultMonthlyPay = StringVar()
        Label(root,textvariable=self.resultMonthlyPay,font=10,fg="Red").place(x=250,y=225)
        self.resultInterest = StringVar()
        Label(root,textvariable=self.resultInterest,font=10,fg="Red").place(x=250,y=250)
        self.resultAnnual = StringVar()
        Label(root,textvariable=self.resultAnnual,font=10,fg="Red").place(x=250,y=275)
        
        #add button & command
        calculate = Button(root,text="Calculate",fg="light blue",bg="gray",command=self.cal_total_pay).place(x=250, y=160)
        reset = Button(root,text="Reset",fg="light blue",bg="gray",command=self.reset).place(x=200, y=160)
        calamount = Button(root,text="Cal",fg="white", bg="gray",command=self.cal_amount).place(x=400,y=50)

        #add menu
        Mymenu = Menu()
        root.config(menu=Mymenu)

        menuitem1 = Menu()
        menuitem1.add_command(label="Save",command=self.save)
        Mymenu.add_cascade(label="File",menu=menuitem1)

        root.mainloop()

    ###function
    
    # function that calculate payment 
    def cal_total_pay(self):
        try:
            afloat = float(self.a.get())
            rfloat = float(self.r.get())
            years = int(self.y.get())
            months = int(self.m.get())
            a = afloat
            r = rfloat /1200 #rate/100*12
            t = years*12 + months #term(month) = year*12 + month
            if a < 0 or r < 0 or t < 0:
                tkinter.messagebox.showinfo("Warning", "Please enter non-negative values.")
                return

            self.monthlyPayment = round(a * ( (r*((1+r)**t)) / (((1+r)**t)-1)),2) # monthly loan payment equation
            self.totalPayment = round(float(self.monthlyPayment) * int(t),2) # total loan payment equation
            self.totalinterest = round(self.totalPayment - a,2) # total interest equation
            self.annualpayment = round(self.monthlyPayment * 12,2) # annual payment equation
        except:
            tkinter.messagebox.showinfo("Warning", f"Please enter a valid value.")
        # set the result to the label
        self.resultTotalPay.set(self.totalPayment) 
        self.resultMonthlyPay.set(self.monthlyPayment)
        self.resultInterest.set(self.totalinterest)
        self.resultAnnual.set(self.annualpayment)

    # function that calculate loan amount from property price and down payment
    def cal_amount(self):
        global window1
        window1 = Toplevel(root) # create new window
        window1.title("Calculate Loan Amount")
        window1.geometry("600x300")
        
        #labels
        Label(window1,text="Property Price",font=10).grid(column=0,row=0)
        Label(window1,text="Down Payment",font=10).grid(column=0,row=1)
        
        #entry
        self.price = DoubleVar()
        Entry(window1,textvariable=self.price).grid(column=2,row=0)
        self.down = DoubleVar()
        Entry(window1,textvariable=self.down).grid(column=2,row=1)
        
        #result label
        self.resultAmount = StringVar()
        Label(window1,textvariable=self.resultAmount,font=10,fg="Red").grid(column=1,row=3)
        
        #botton & command
        ok = Button(window1,text="Ok",fg="white",bg="gray",command=self.Ok).grid(column=1,row=2)
        
    # function for calculate loan amount
    def Ok(self):
        if self.price.get() < 0 or self.down.get() < 0:
            tkinter.messagebox.showinfo("Warning", "Please enter non-negative values.")
            return
        a = self.price.get() - self.down.get() # loan amount = property price - down payment(%)
        #label
        Label(window1,text="Your Loan amount is ",font=10,fg="Blue").grid(column=0,row=3)
        self.resultAmount.set(a)

        #delete old amount in main window and insert new amount calculated from this function.
        self.amount.delete(0,END)
        self.amount.insert(0,a)

    # function that reset all the amount in main window's entry
    def reset(self):
        self.amount.delete(0,END)
        self.ir.delete(0,END)
        self.years.delete(0,END)
        self.months.delete(0,END)
        
    # function for save menu
    def save(self):
        with open("LoanHistory.txt", "a", encoding="utf-8") as f:
        
            f.write("Loan Amount = "+str(self.a.get())+"\n")
            f.write("Interest Rate = "+str(self.r.get())+" % per year"+"\n")
            f.write("Loan Term = "+str(self.y.get())+" year "+str(self.m.get())+" month"+"\n")
            f.write("The result are"+"\n")
            f.write("Total Payment : "+str(self.totalPayment)+"\n")
            f.write("Monthly Payment : "+str(self.monthlyPayment)+"\n")
            f.write("Total Interest : "+str(self.totalinterest)+"\n")
            f.write("Annual Payment : "+str(self.annualpayment)+"\n")
            f.write("\n")
        
        
        
loancal()