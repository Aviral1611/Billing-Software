#tkinter and pandas
import tkinter as tk                 
from tkinter import *
from tkinter import ttk
from pandas import DataFrame

#writing the items and quantities
items={"101A":['brownrice',50,45.50,41.25],"102B":["whole wheat",30,27.45,21.50],"102B":[ "Whole wheat",30,27.45,21.50], "102C":["Tomato sauce", 25.50,20.25,18.70], "103D":["Mustard",40,39.45,37],
       "104E":["Barbecue sauce",45,43,41.50], "105F":["Red-wine vinegar",4000,3800,3750], "106G":["Salsa",200,189.50,170], "107H":["Extra virgin olive oil",500,478.50,455.70],
       "108I":["canola oil",200,180,118], "109J":["Hot pepper sauce",100,98.50,91.25], "110K":["Bananas",60,55,50], "111L":["Apples",300,250,120], "112M":["Oranges",200,140,110],
       "113N":["Mangoes",100,80,50], "114O":["Strawberries",100,90,80], "115P":["Blueberries",95,80,7], "116Q":["Green teas" ,50,225,200], "117R":["Sparkling water",20,14.50,11],
       "118S":["Dried apricots",270,250,230], "119T":["Dried figs",100,95,90], "120U":["Dried prunes",90,85,80], "121V":["Almonds",900,870,850], "122W":["Cashews",1000,950,910], "123X":["Walnuts",800,770,720], "124Y":["Peanuts",400,380,360], "125Z":["Pecans",350,320,300],
       "201A":["Pistachos",1200,1180,1160],"202B":["sunflower seeds",150,112.50,103.45],
       "203C":["sesame seeds",120.50,110.25,101.40],"204D":["Whole flaxseeds",95.20,90.45,89.20]}
customers={'AAA1001':['surian',950012345],'AAA1002':['nila',9500023456],'AAA1003':['arivazhagan',9712300078],'AAA1004':['nithin Kumar',9586233333],'AAA1005':['aravind',6931245872]}
item=[items[i][0] for i in items]
Scaffold1=tk.Tk()
Scaffold1.title("BILLING SOFTWARE")
Scaffold1.geometry('600x500')
frame1=tk.Frame(Scaffold1,bg='yellow')
frame1.place(relwidth=1,relheight=1)
labelITEM=tk.Label(frame1,text="BILLING SOFTWARE" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
labelITEM.place(relwidth=0.3, relheight=0.07, relx=0.15,rely=0.085)
labelITEM=tk.Label(frame1,text="ENTER ITEM" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
labelITEM.place(relwidth=0.22, relheight=0.05, relx=0.02,rely=0.25)
Item=ttk.Combobox(frame1,values=item)
Item.place(relwidth=0.27, relheight=0.05, relx=0.27,rely=0.25)
labelq=tk.Label(frame1,text="ENTER QUALITY" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
labelq.place(relwidth=0.22, relheight=0.05, relx=0.02,rely=0.33)
Quality=ttk.Combobox(frame1,values=[])
Quality.place(relwidth=0.15, relheight=0.05, relx=0.27,rely=0.33)
CP=1
def quality(event):
    s,t=[],Item.get()
    for i in items:
        if items[i][0]==t:
            s=items[i][1:]
            break
    Quality['values']=s
    Quality.set(s[1])
labelqa=tk.Label(frame1,text="ENTER QUANTITY" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
labelqa.place(relwidth=0.24, relheight=0.045, relx=0.016,rely=0.4)
Quantity=tk.Entry(frame1,bd=1.5,font=('Times',13,'bold'), fg='black', bg='snow')
Quantity.place(relwidth=0.2, relheight=0.05, relx=0.27,rely=0.4)
Item.bind('<<ComboboxSelected>>',quality)
l=[]
s=0
frame21=tk.Frame(frame1,bg='yellow')
frame21.place(relheight=0.735,relwidth=0.44,relx=0.55,rely=0.05)
frame2=tk.Frame(frame1,bg='yellow')
frame2.place(relwidth=0.44,relheight=0.15,relx=0.55,rely=0.8)
def fullscreen():
    Scaffold1.attributes("-fullscreen", False)
def Enter():
    global l
    global s
    global frame22
    global Scaffold1
    global frame21
    global frame2
    global CP
    if CP%2!=0:
        for widgets in frame2.winfo_children(): 
            widgets.destroy()
        for widgets in frame21.winfo_children():
            widgets.destroy()
    else:
        frame21=tk.Frame(frame1,bg='yellow')
        frame21.place(relheight=0.735,relwidth=0.44,relx=0.55,rely=0.05)
        frame2=tk.Frame(frame1,bg='yellow')
        frame2.place(relwidth=0.44,relheight=0.15,relx=0.55,rely=0.8)
        CP=1
    TRY="INVALID"
    Scaffold1.attributes("-fullscreen", True)
    for i in items:
        if items[i][0]==Item.get():
            TRY=i
            break
    ic_q=[TRY,Quality.get(),Quantity.get()]
    l.append(ic_q)
    Item.delete(0,"end")
    Quality.delete(0,"end")
    Quantity.delete(0,"end")
    cusitems=[]
    for i in l:
        s+=float(items[i[0]][1])*float(i[2])
        cusitems.append([i[0],i[2],float(items[i[0]][1])*float(i[2])])
    cursor=[]
    for i in cusitems:
        cursor.append([i[0],items[i[0]][0],i[1],float(i[2])/float(i[1]),i[2]])
    frame211=tk.Frame(frame21,bg="pale green",)
    frame211.place(relheight=1,relwidth=1)
    global buttoner
    canvas=tk.Canvas(frame21,bg="pale green")
    canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
    scrollbar=ttk.Scrollbar(frame21,orient=VERTICAL,command=canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar2=ttk.Scrollbar(frame21,orient=HORIZONTAL,command=canvas.xview)
    scrollbar2.pack(side=BOTTOM,fill=X)
    canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
    frame3=tk.Frame(canvas,bg="pale green")
    canvas.create_window((0,0),window=frame3,anchor="nw")
    label1=tk.Label(frame3,text="Code" ,font=('Times',9,'bold'),width=16,relief=RAISED, fg="green",bd=4)
    label1.grid(row=0,column=0)
    label2=tk.Label(frame3,text="Item" ,font=('Times',9,'bold'),width=16,relief=RAISED, fg="green",bd=4)
    label2.grid(row=0,column=1)
    label3=tk.Label(frame3,text="Quantity" ,font=('Times',9,'bold'),width=16,relief=RAISED, fg="green",bd=4)
    label3.grid(row=0,column=2)
    label3=tk.Label(frame3,text="Quality" ,font=('Times',9,'bold'),width=16,relief=RAISED, fg="green",bd=4)
    label3.grid(row=0,column=3)
    label3=tk.Label(frame3,text="Price" ,font=('Times',9,'bold'),width=16,relief=RAISED, fg="green",bd=4)
    label3.grid(row=0,column=4)
    x=1
    for i in cursor:
        for j in range(5):
            if j<5:
                e=tk.Entry(frame3,font=('Times',9,'bold'),width=16, fg='blue',relief=RAISED,bd=4) 
                e.grid(row=x, column=j) 
                e.insert(END, i[j])
                label=tk.Label(frame3,font=('Times',9,'bold'),width=16, fg='blue',relief=RAISED,bd=4)
                label.grid(row=x, column=j)
                y=e.get()
                label['text']=y
        x+=1
    label32=tk.Label(frame3,text="TOTAL AMOUNT: "+str(round(s,2)),font=('Times',10,'bold'),width=33, fg='blue',relief=RAISED,bd=4)
    label32.grid(row=x,columnspan=2)
    Scaffold1.after(500,fullscreen)
    def ClearPurchase():
        global l
        global s
        global frame21
        global frame2
        global CP
        l=[]
        s=0
        for widgets in frame2.winfo_children():
            widgets.destroy()
        for widgets in frame21.winfo_children():
            widgets.destroy()
    frame20=tk.Frame(frame2,bg='yellow')
    frame20.place(relwidth=1,relheight=1)
    buttonEn=tk.Button(frame20,text='ConfirmPurchase',command=ConfirmPurchase, font=('Times',10,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
    buttonEn.place(relwidth=0.43, relheight=0.4,relx=0.0,rely=0.09)
    buttonEn=tk.Button(frame20,text='ClearPurchase',command=ClearPurchase, font=('Times',10,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
    buttonEn.place(relwidth=0.38, relheight=0.4,relx=0.61,rely=0.09)
    Scaffold1.after(5,fullscreen)
buttonEn=tk.Button(frame1,text='ADD',command=Enter, font=('Times',10,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
buttonEn.place(relwidth=0.087, relheight=0.05,relx=0.45,rely=0.47)

def ConfirmPurchase():
    global CP
    for widgets in frame2.winfo_children():
        widgets.destroy()
    for widgets in frame21.winfo_children():
        widgets.destroy()
    CP+=1
    labelITEM=tk.Label(frame21,text="Enter Name" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
    labelITEM.place(relwidth=0.3, relheight=0.075, relx=0.03,rely=0.35)
    labelITEM=tk.Label(frame21,text="Enter Mobile-Number" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
    labelITEM.place(relwidth=0.5, relheight=0.075, relx=0.03,rely=0.45)
    Sname=tk.Entry(frame21, bd=3, relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
    Sname.place(relwidth=0.44, relheight=0.065, relx=0.38,rely=0.35)
    cm=tk.Entry(frame21, bd=3, relief=RAISED,font=('Times',13,'bold'), fg='black', bg='snow')
    cm.place(relwidth=0.38, relheight=0.065, relx=0.57,rely=0.45)
    def OK():
        global customers
        global l
        global s
        global frame21
        S,M=Sname.get(),cm.get()
        for widgets in frame21.winfo_children():
            widgets.destroy()
        Scaffold1=tk.Tk()
        Scaffold1.title("BILL")
        Scaffold1.geometry('399x600')
        cusitems=[]
        for i in l:
            cusitems.append([i[0],i[2],float(items[i[0]][1])*float(i[2])])
        cursor=[]
        for i in cusitems:
            cursor.append([i[0],items[i[0]][0],i[1],float(i[2])/float(i[1]),i[2]])
        frame21=tk.Frame(Scaffold1,bg="pale green",)
        frame21.place(relheight=1,relwidth=1)
        global buttoner
        canvas=tk.Canvas(frame21,bg="pale green")
        canvas.place(relheight=0.96,relwidth=0.977,relx=0,rely=0)
        scrollbar=ttk.Scrollbar(frame21,orient=VERTICAL,command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar2=ttk.Scrollbar(frame21,orient=HORIZONTAL,command=canvas.xview)
        scrollbar2.pack(side=BOTTOM,fill=X)
        canvas.configure(xscrollcommand=scrollbar2.set,yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        frame3=tk.Frame(canvas,bg="pale green")
        canvas.create_window((0,0),window=frame3,anchor="nw")
        label1=tk.Label(frame3,text="Code" ,font=('Times',15,'bold'),width=15,relief=RAISED, fg="green",bd=4)
        label1.grid(row=0,column=0)
        label2=tk.Label(frame3,text="Item" ,font=('Times',15,'bold'),width=15,relief=RAISED, fg="green",bd=4)
        label2.grid(row=0,column=1)
        label3=tk.Label(frame3,text="Quantity" ,font=('Times',15,'bold'),width=15,relief=RAISED, fg="green",bd=4)
        label3.grid(row=0,column=2)
        label3=tk.Label(frame3,text="Quality" ,font=('Times',15,'bold'),width=15,relief=RAISED, fg="green",bd=4)
        label3.grid(row=0,column=3)
        label3=tk.Label(frame3,text="Price" ,font=('Times',15,'bold'),width=15,relief=RAISED, fg="green",bd=4)
        label3.grid(row=0,column=4)
        x=1
        for i in cursor:
            for j in range(5):
                if j<5:
                    e=tk.Entry(frame3,font=('Times',15,'bold'),width=15, fg='blue',relief=RAISED,bd=4) 
                    e.grid(row=x, column=j) 
                    e.insert(END, i[j])
                    label=tk.Label(frame3,font=('Times',15,'bold'),width=15, fg='blue',relief=RAISED,bd=4)
                    label.grid(row=x, column=j)
                    y=e.get()
                    label['text']=y
            x+=1   
        r=True

        for i in customers:
            if (customers[i][0]).lower()==S and str(customers[i][1])==M:
                if s>=10000:
                    cash=(s-(0.012*s))
                    label31=tk.Label(frame3,text="CASH: "+str(round((0.012*s),2)),font=('Times',15,'bold'),width=31, fg='blue',relief=RAISED,bd=4)
                    label31.grid(row=x, columnspan=2)
                    label3=tk.Label(frame3,text="TOTAL AMOUNT: "+str(round(cash,2)),font=('Times',15,'bold'),width=31, fg='blue',relief=RAISED,bd=4)
                    label3.grid(row=x+1, columnspan=2)
                    r=False
        if s>=10000 and r:
            discount=(s-(0.01*s))
            label31=tk.Label(frame3,text="DISCOUNT: "+str(round((0.01*s),2)),font=('Times',15,'bold'),width=31, fg='blue',relief=RAISED,bd=4)
            label31.grid(row=x,columnspan=2)
            label3=tk.Label(frame3,text="TOTAL AMOUNT: "+str(round(discount,2)),font=('Times',15,'bold'),width=31, fg='blue',relief=RAISED,bd=4)
            label3.grid(row=x+1,columnspan=2)
        if s<10000:
            label3=tk.Label(frame3,text="TOTAL AMOUNT: "+str(round(s,2)),font=('Times',15,'bold'),width=31, fg='blue',relief=RAISED,bd=4)
            label3.grid(row=x,columnspan=2)
        l=[]
        s=0
    labelqa=tk.Label(frame21,text="Enter Customer Details" ,bg="snow",font=('Times',10,'bold'),width=10,relief=RAISED, fg="black",bd=4)
    labelqa.place(relwidth=0.6, relheight=0.08, relx=0.2,rely=0.2)
    buttonEnn=tk.Button(frame21,text='OK',command=OK, font=('Times',10,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
    buttonEnn.place(relwidth=0.2, relheight=0.05, relx=0.75,rely=0.55)
