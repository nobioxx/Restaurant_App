from tkinter import*
from tkinter import messagebox
import random
import time;
import datetime
from PIL import Image, ImageTk
import sqlite3

#Design Elements

root=Tk()
root.title("Maa Resturant")
root.geometry("1650x700+0+0")
root.title("Maa Resturant")


#Top Heading part

Tops = Frame(root,width=1000, height=138)
Tops.pack(side=TOP)



#Selection Frame

f1 = Frame(root,width=700, height=350, bd= 0, relief='raise')
f1.pack(side=LEFT)
f1.configure(background="#FDF3F0")

f2 = Frame(root,width=700, height=350)
f2.pack()

f1a = Frame(f1,width=100, height=100, bd= 0, relief="raise")
f1a.pack(side=TOP)



#Recipt layout
fta = Frame(f2,width=200, height=200, bd= 2, relief="raise")
fta.pack(side=TOP)

fa2 = Frame(f2,width=200, height=50, relief="raise")
fa2.pack(side=BOTTOM)




#Bottom Layout
f2a = Frame(f1,width=100, height=320, bd= 2, relief="raise")
f2a.pack(side=TOP)

f1ba = Frame(f2a,width=100,height=330 ,relief="raise")
f1ba.pack(side=LEFT)

f1bb = Frame(f2a,width=100,height=330,padx=30, relief="raise")
f1bb.pack(side=RIGHT)










#section 1

f1aa = Frame(f1a,width=100,height=270, relief="raise")
f1aa.pack(side=LEFT)

#Section 2

f1ab = Frame(f1a, width = 100, height = 270,relief="raise")
f1ab.pack(side=RIGHT)

#background color of the layouts
f1a.configure(background='#FDF3F0')
fta.configure(background='#585828')
f1ab.configure(background="#FDF3F0")
f1aa.configure(background="#FDF3F0")
f2a.configure(background="#FEB642")
f1ba.configure(background="#FEB642")
f1bb.configure(background="#FEB642")

#header photo
headerphoto= Image.open("header.jpg")
photo = ImageTk.PhotoImage(headerphoto)
label=Label(Tops,image=photo)
label.image = photo
label.pack()

bgphoto= Image.open("bg.jpg")
photo = ImageTk.PhotoImage(bgphoto)
label=Label(root,image=photo)
label.image = photo
label.pack()

#========================================database==============================






def database():
    global conn, cursor
    conn= sqlite3.connect("Order.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'orderlist'(Name, Phone, Items)")
    cursor.execute("INSERT INTO 'orderlist'(Name, Phone, Items) VALUES (?,?,?)"(y_name.get(),y_phone.get(),Total_cost.get()))
    conn.commit()
    conn.close()
    


#==========================================Methods    ==========================


def quit():
    quit = messagebox.askyesno("Quit","Do you want to Quit?")
    if quit>0:
        root.destroy()
        return

def reset():
    CostofItem.set("")
    SubTotal.set("")
    cgst.set("")
    sgst.set("")
    TotalCost.set("")

    y_name.set("")
    y_number.set("")
    y_email.set("")
    txtReceipt.delete("1.0",END)

    D_Tea.set("0")
    D_Coffee.set("0")
    D_Water.set("0")
    S_Vroll.set("0")
    S_Eroll.set("0")
    S_Croll.set("0")
    S_Proll.set("0")
    S_Sroll.set("0")
    C_Vchow.set("0")
    C_Echow.set("0")
    C_Cchow.set("0")
    C_Vrice.set("0")
    C_Erice.set("0")
    C_Crice.set("0")
    P_pepsi.set("0")
    P_mojito.set("0")

    txttea.configure(state=DISABLED)
    txtcoffee.configure(state=DISABLED)
    txtwater.configure(state=DISABLED)
    txtvegroll.configure(state=DISABLED)
    txteggroll.configure(state=DISABLED)
    txtchickenroll.configure(state=DISABLED)
    txtpaneerroll.configure(state=DISABLED)
    txtsawarmaroll.configure(state=DISABLED)
    txtvegchow.configure(state=DISABLED)
    txteggchow.configure(state=DISABLED)
    txtchickenchow.configure(state=DISABLED)
    txtvegfried.configure(state=DISABLED)
    txteggfried.configure(state=DISABLED)
    txtchickenfried.configure(state=DISABLED)
    txtpepsi.configure(state=DISABLED)
    txtmojito.configure(state=DISABLED)


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    







   

#======================================variables=====================================








Dateoforder=StringVar()
Reciept_ref=StringVar()
cgst=StringVar()
sgst=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofItem=StringVar()


D_Tea=StringVar()
D_Coffee=StringVar()
D_Water=StringVar()

S_Vroll=StringVar()
S_Eroll=StringVar()
S_Croll=StringVar()
S_Proll=StringVar()
S_Sroll=StringVar()

C_Vchow=StringVar()
C_Echow=StringVar()
C_Cchow=StringVar()
C_Vrice=StringVar()
C_Erice=StringVar()
C_Crice=StringVar()

P_pepsi=StringVar()
P_mojito=StringVar()

y_name=StringVar()
y_number=StringVar()
y_email=StringVar()




D_Tea.set("0")
D_Coffee.set("0")
D_Water.set("0")
S_Vroll.set("0")
S_Eroll.set("0")
S_Croll.set("0")
S_Proll.set("0")
S_Sroll.set("0")
C_Vchow.set("0")
C_Echow.set("0")
C_Cchow.set("0")
C_Vrice.set("0")
C_Erice.set("0")
C_Crice.set("0")
P_pepsi.set("0")
P_mojito.set("0")
Dateoforder.set(time.strftime("%d/%m/%y"))


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)







#===========================Total Method===================================

def Costof():
    Item1=float(D_Tea.get())
    Item2=float(D_Coffee.get())
    Item3=float(D_Water.get())
   
    Item4=float(S_Vroll.get())
    Item5=float(S_Eroll.get())
    Item6=float(S_Croll.get())
    Item7=float(S_Proll.get())
    Item8=float(S_Sroll.get())
   
    Item9=float(C_Vchow.get())
    Item10=float(C_Echow.get())
    Item11=float(C_Cchow.get())
    Item12=float(C_Vrice.get())
    Item13=float(C_Erice.get())
    Item14=float(C_Crice.get())
   
    Item15=float(P_pepsi.get())
    Item16=float(P_mojito.get())

    costofitem =(Item1*10)+(Item2*20)+(Item3*10)+(Item4*50)\
                   +(Item5*60)+(Item6*70)+(Item7*70)+(Item8*80)\
                   +(Item9*80)+(Item10*90)+(Item11*120)+(Item12*80)\
                   +(Item13*90)+(Item14*120)+(Item15*40)+(Item16*125)

    CostofItem.set(costofitem)
    gs1=(costofitem*0.02)
    cgst.set(gs1)
    gst2=(costofitem*0.02)
    sgst.set(gst2)

    ST=(costofitem*0.05)
    

    subtotal=(costofitem)+(ST)
    SubTotal.set(subtotal)

    Total_cost=str('%.2f'%(costofitem+gs1+gst2+ST))
    TotalCost.set(Total_cost)
    Receipt()




def checkbtn():
    if(var1.get() == 1):
        txttea.configure(state=NORMAL)
        D_Tea.set("1")
    elif(var1.get() == 0):
        txttea.configure(state=DISABLED)
        D_Tea.set("0")
    if(var2.get() == 1):
        txtcoffee.configure(state=NORMAL)
        D_Coffee.set("1")
    elif(var2.get() == 0):
        txtcoffee.configure(state=DISABLED)
        D_Coffee.set("0")
    if(var3.get() == 1):
        txtwater.configure(state=NORMAL)
        D_Water.set("1")
    elif(var3.get() == 0):
        txtwater.configure(state=DISABLED)
        D_Water.set("0")
    if(var4.get() == 1):
        txtvegroll.configure(state=NORMAL)
        S_Vroll.set("1")
    elif(var4.get() == 0):
        txtvegroll.configure(state=DISABLED)
        S_Vroll.set("0")
    if(var5.get() == 1):
        txteggroll.configure(state=NORMAL)
        S_Eroll.set("1")
    elif(var5.get() == 0):
        txteggroll.configure(state=DISABLED)
        S_Eroll.set("0")
    if(var6.get() == 1):
        txtchickenroll.configure(state=NORMAL)
        S_Croll.set("1")
    elif(var6.get() == 0):
        txtchickenroll.configure(state=DISABLED)
        S_Croll.set("0")
    if(var7.get() == 1):
        txtpaneerroll.configure(state=NORMAL)
        S_Proll.set("1")
    elif(var7.get() == 0):
        txtpaneerroll.configure(state=DISABLED)
        S_Proll.set("0")
    if(var8.get() == 1):
        txtsawarmaroll.configure(state=NORMAL)
        S_Sroll.set("1")
    elif(var8.get() == 0):
        txtsawarmaroll.configure(state=DISABLED)
        S_Sroll.set("0")
    if(var9.get() == 1):
        txtvegchow.configure(state=NORMAL)
        C_Vchow.set("1")
    elif(var9.get() == 0):
        txtvegchow.configure(state=DISABLED)
        C_Vchow.set("0")
    if(var10.get() == 1):
        txteggchow.configure(state=NORMAL)
        C_Echow.set("1")
    elif(var10.get() == 0):
        txteggchow.configure(state=DISABLED)
        C_Echow.set("0")
    if(var11.get() == 1):
        txtchickenchow.configure(state=NORMAL)
        C_Cchow.set("1")
    elif(var11.get() == 0):
        txtchickenchow.configure(state=DISABLED)
        C_Cchow.set("0")
    if(var12.get() == 1):
        txtvegfried.configure(state=NORMAL)
        C_Vrice.set("1")
    elif(var12.get() == 0):
        txtvegfried.configure(state=DISABLED)
        C_Vrice.set("0")
    if(var13.get() == 1):
        txteggfried.configure(state=NORMAL)
        C_Erice.set("1")
    elif(var13.get() == 0):
        txteggfried.configure(state=DISABLED)
        C_Erice.set("0")
    if(var14.get() == 1):
        txtchickenfried.configure(state=NORMAL)
        C_Crice.set("1")
    elif(var14.get() == 0):
        txtchickenfried.configure(state=DISABLED)
        C_Crice.set("0")
    if(var15.get() == 1):
        txtpepsi.configure(state=NORMAL)
        P_pepsi.set("1")
    elif(var15.get() == 0):
        txtpepsi.configure(state=DISABLED)
        P_pepsi.set("0")
    if(var16.get() == 1):
        txtmojito.configure(state=NORMAL)
        P_mojito.set("1")
    elif(var16.get() == 0):
        txtmojito.configure(state=DISABLED)
        P_mojito.set("0")

    
    





def Receipt():
    txtReceipt.delete("1.0",END)
    x= random.randint(10908,500876)
    randomRef = str(x)
    Reciept_ref.set("BILL"+randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Reciept_ref.get()+'\t\t'+ Dateoforder.get()+"\n")
    txtReceipt.insert(END,'ITems:\t\t\t\t'+"Quantity and Cost\n\n")
    if(var1.get() == 1):
        txtReceipt.insert(END,'Tea:\t\t\t\t'+D_Tea.get()+'\t₹10 \t\t'+ "\n")
    if(var2.get() ==1):
        txtReceipt.insert(END,'Coffee:\t\t\t\t'+D_Coffee.get()+'x\t₹20\t\t'+"\n")
    if(var3.get() == 1):
        txtReceipt.insert(END,'Water:\t\t\t\t'+D_Water.get()+'x\t₹10\t\t'+"\n")
    if(var4.get() == 1):
        txtReceipt.insert(END,'Veg Roll:\t\t\t\t'+S_Vroll.get()+'x\t₹50\t\t'+"\n")
    if(var5.get() == 1):
        txtReceipt.insert(END,'Egg Roll:\t\t\t\t'+S_Eroll.get()+'x\t₹60\t\t'+"\n")
    if(var6.get() == 1):
        txtReceipt.insert(END,'Chicken Roll:\t\t\t\t'+S_Croll.get()+'x\t₹70\t\t'+"\n")
    if(var7.get() == 1):
        txtReceipt.insert(END,'Paneer Roll:\t\t\t\t'+S_Proll.get()+'x\t₹70\t\t'+"\n")
    if(var8.get() == 1):
        txtReceipt.insert(END,'Sawarma Roll:\t\t\t\t'+S_Sroll.get()+'x\t₹80\t\t'+"\n")
    if(var9.get() == 1):
        txtReceipt.insert(END,'Veg Chow:\t\t\t\t'+C_Vchow.get()+'x\t₹80\t\t'+"\n")
    if(var10.get() == 1):
        txtReceipt.insert(END,'Egg Chow:\t\t\t\t'+C_Echow.get()+'x\t₹90\t\t'+"\n")
    if(var11.get() == 1):
        txtReceipt.insert(END,'Chicken Chow:\t\t\t\t'+C_Cchow.get()+'x\t₹120\t\t'+"\n")
    if(var12.get() == 1):
        txtReceipt.insert(END,'Veg Fried Rice:\t\t\t\t'+C_Vrice.get()+'x\t₹80\t\t'+"\n")
    if(var13.get() == 1):
        txtReceipt.insert(END,'Egg Fried Rice:\t\t\t\t'+C_Erice.get()+'x\t₹90\t\t'+"\n")
    if(var14.get() == 1):
        txtReceipt.insert(END,'Chicken Fried Rice:\t\t\t\t'+C_Crice.get()+'x\t₹120\t\t'+"\n")
    if(var15.get() == 1):
        txtReceipt.insert(END,'Pepsi:\t\t\t\t'+P_pepsi.get()+'x\t₹40\t\t'+"\n")
    if(var16.get() == 1):
        txtReceipt.insert(END,'Mojito:\t\t\t\t'+P_mojito.get()+'x\t₹125\t\t'+"\n")
    else:
        txtReceipt.insert(END,'')
    txtReceipt.insert(END,'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')       
    txtReceipt.insert(END,'Item Cost:\t\t\t\t'+"₹"+CostofItem.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'CGST:\t\t\t\t'+"₹"+cgst.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'SGST:\t\t\t\t'+"₹"+sgst.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'Total:\t\t\t\t'+"₹"+TotalCost.get()+'\t\t\t'+"\n")



def orderItem():
    txtReceipt.delete("1.0",END)
    x= random.randint(10908,500876)
    randomRef = str(x)
    Reciept_ref.set("BILL"+randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Reciept_ref.get()+'\t\t'+ Dateoforder.get()+"\n")
    txtReceipt.insert(END,'Name:\t'+y_name.get()+'\t\t'+"\n")
    txtReceipt.insert(END,'Mobile:\t'+y_number.get()+'\t\t'+"\n")
    txtReceipt.insert(END,'Email:\t'+y_email.get()+'\t\t'+"\n")
    
    txtReceipt.insert(END,'ITems:\t\t\t\t'+"Quantity and Cost\n\n")
    if(var1.get() == 1):
        txtReceipt.insert(END,'Tea:\t\t\t\t'+D_Tea.get()+'\t₹10 \t\t'+ "\n")
    if(var2.get() ==1):
        txtReceipt.insert(END,'Coffee:\t\t\t\t'+D_Coffee.get()+'x\t₹20\t\t'+"\n")
    if(var3.get() == 1):
        txtReceipt.insert(END,'Water:\t\t\t\t'+D_Water.get()+'x\t₹10\t\t'+"\n")
    if(var4.get() == 1):
        txtReceipt.insert(END,'Veg Roll:\t\t\t\t'+S_Vroll.get()+'x\t₹50\t\t'+"\n")
    if(var5.get() == 1):
        txtReceipt.insert(END,'Egg Roll:\t\t\t\t'+S_Eroll.get()+'x\t₹60\t\t'+"\n")
    if(var6.get() == 1):
        txtReceipt.insert(END,'Chicken Roll:\t\t\t\t'+S_Croll.get()+'x\t₹70\t\t'+"\n")
    if(var7.get() == 1):
        txtReceipt.insert(END,'Paneer Roll:\t\t\t\t'+S_Proll.get()+'x\t₹70\t\t'+"\n")
    if(var8.get() == 1):
        txtReceipt.insert(END,'Sawarma Roll:\t\t\t\t'+S_Sroll.get()+'x\t₹80\t\t'+"\n")
    if(var9.get() == 1):
        txtReceipt.insert(END,'Veg Chow:\t\t\t\t'+C_Vchow.get()+'x\t₹80\t\t'+"\n")
    if(var10.get() == 1):
        txtReceipt.insert(END,'Egg Chow:\t\t\t\t'+C_Echow.get()+'x\t₹90\t\t'+"\n")
    if(var11.get() == 1):
        txtReceipt.insert(END,'Chicken Chow:\t\t\t\t'+C_Cchow.get()+'x\t₹120\t\t'+"\n")
    if(var12.get() == 1):
        txtReceipt.insert(END,'Veg Fried Rice:\t\t\t\t'+C_Vrice.get()+'x\t₹80\t\t'+"\n")
    if(var13.get() == 1):
        txtReceipt.insert(END,'Egg Fried Rice:\t\t\t\t'+C_Erice.get()+'x\t₹90\t\t'+"\n")
    if(var14.get() == 1):
        txtReceipt.insert(END,'Chicken Fried Rice:\t\t\t\t'+C_Crice.get()+'x\t₹120\t\t'+"\n")
    if(var15.get() == 1):
        txtReceipt.insert(END,'Pepsi:\t\t\t\t'+P_pepsi.get()+'x\t₹40\t\t'+"\n")
    if(var16.get() == 1):
        txtReceipt.insert(END,'Mojito:\t\t\t\t'+P_mojito.get()+'x\t₹125\t\t'+"\n")
    else:
        txtReceipt.insert(END,'')
    txtReceipt.insert(END,'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')       
    txtReceipt.insert(END,'Item Cost:\t\t\t\t'+"₹"+CostofItem.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'CGST:\t\t\t\t'+"₹"+cgst.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'SGST:\t\t\t\t'+"₹"+sgst.get()+'\t\t\t'+"\n")
    txtReceipt.insert(END,'Total:\t\t\t\t'+"₹"+TotalCost.get()+'\t\t\t'+"\n")

    database()
    



#==================Label==================================





#=============================MENU SECTION 1===========================================



name=Label(f1aa, text="Drinks\t",bg="#FDF3F0",font=('courier',18,'bold')).grid(row=0,sticky=W)

                      
tea = Checkbutton(f1aa,bg="#FDF3F0", variable=var1, onvalue=1, offvalue=0, command= checkbtn,bd=0, text="Tea\t",font=('Courier',14,'bold')).grid(row=1,sticky=W)
coffee = Checkbutton(f1aa,bg="#FDF3F0", variable=var2, onvalue=1, offvalue=0, command= checkbtn,bd=0, text="Coffee\t",font=('Courier',14,'bold')).grid(row=2,sticky=W)
water = Checkbutton(f1aa,bg="#FDF3F0", variable=var3, onvalue=1, offvalue=0,command= checkbtn, bd=0, text="Water\t", font=('Courier',14,'bold')).grid(row=3,sticky=W)

name=Label(f1aa,bg="#FDF3F0", text="Spring Rolls\t",font=('courier',18,'bold')).grid(row=4,sticky=W)

veg_roll = Checkbutton(f1aa ,bd=0, variable=var4, onvalue=1, offvalue=0,command= checkbtn, bg="#FDF3F0",text="Veg Roll\t" ,font=('Courier',14,'bold')).grid(row=5,sticky=W)
egg_roll = Checkbutton(f1aa, bd=0, variable=var5, onvalue=1, offvalue=0,command= checkbtn,bg="#FDF3F0", text="Egg Roll\t",font=('Courier',14,'bold')).grid(row=6,sticky=W)
chicken_roll= Checkbutton(f1aa, bd=0, variable=var6, onvalue=1, offvalue=0,command= checkbtn,bg="#FDF3F0", text="Chicken Roll\t",font=('Courier',14,'bold')).grid(row=7,sticky=W)
paneer_roll = Checkbutton(f1aa, bd=0, variable=var7, onvalue=1, offvalue=0,command= checkbtn, bg="#FDF3F0",text="Paneer Roll\t", font=('Courier',14,'bold')).grid(row=8,sticky=W)
sawarma_roll = Checkbutton(f1aa, bd=0, variable=var8, onvalue=1, offvalue=0,command= checkbtn,bg="#FDF3F0", text="Sawarma Roll\t",font=('Courier',14,'bold')).grid(row=9,sticky=W)


#=============================x label1===========================================

x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=1,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=2,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=3,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=5,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=6,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=7,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=8,column=6)
x=Label(f1aa, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=9,column=6)


#=============================x label2===========================================


x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=1,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=2,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=3,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=4,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=5,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=6,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=8,column=6)
x=Label(f1ab, text="x",bg="#FDF3F0",font=('arial',8)).grid(row=9,column=6)


#=============================MENU SECTION 2===========================================

name=Label(f1ab, text="Chinese Dishes\t",bg="#FDF3F0",padx=10,font=('courier',18,'bold')).grid(row=0,sticky=W)


veg_chow = Checkbutton(f1ab,bg="#FDF3F0", bd=0,padx=15,variable=var9, command= checkbtn,onvalue=1, offvalue=0, text="Veg Chow\t",font=('Courier',14,'bold')).grid(row=1,sticky=W)
egg_chow= Checkbutton(f1ab,bg="#FDF3F0", bd=0,padx=15,variable=var10, command= checkbtn,onvalue=1, offvalue=0, text="Egg Chow\t", font=('Courier',14,'bold')).grid(row=2,sticky=W)
chicken_chow = Checkbutton(f1ab,bg="#FDF3F0",padx=15,variable=var11, command= checkbtn,onvalue=1, offvalue=0, bd=0, text="Chicken Chow\t",font=('Courier',14,'bold')).grid(row=3,sticky=W)
veg_fried_rice = Checkbutton(f1ab, bg="#FDF3F0",bd=0,padx=15,variable=var12, command= checkbtn,onvalue=1, offvalue=0, text="Veg Fried Rice\t",font=('Courier',14,'bold')).grid(row=4,sticky=W)
egg_fried_rice = Checkbutton(f1ab,bg="#FDF3F0", bd=0,padx=15,variable=var13, command= checkbtn,onvalue=1, offvalue=0, text="Egg Fried Rice\t",font=('Courier',14,'bold')).grid(row=5,sticky=W)
chicken_fried_rice = Checkbutton(f1ab,bg="#FDF3F0", bd=0,padx=15,variable=var14, command= checkbtn,onvalue=1, offvalue=0, text="Chicken Friend Rice\t", font=('Courier',14,'bold')).grid(row=6,sticky=W)


name=Label(f1ab, text="Cold Drinks\t",bg="#FDF3F0",padx=15,font=('courier',18,'bold')).grid(row=7,sticky=W)


pepsi = Checkbutton(f1ab, bd=0,bg="#FDF3F0",variable=var15, onvalue=1, offvalue=0,command= checkbtn, text="Pepsi \t",padx=15,font=('Courier',14,'bold')).grid(row=8,sticky=W)
coca = Checkbutton(f1ab, bd=0,bg="#FDF3F0",variable=var16, onvalue=1, offvalue=0, command= checkbtn,text="Mojito\t",padx=15,font=('Courier',14,'bold')).grid(row=9,sticky=W)


#=============================Section 1 Widgets===========================================

txttea = Entry(f1aa, font=('arial',12),textvariable=D_Tea, bg="#FDF3F0",bd=2, width=5, justify='left',state=DISABLED)
txttea.grid(row=1, column=7)
txtcoffee = Entry(f1aa, font=('arial',12),bg="#FDF3F0",textvariable=D_Coffee, bd=2, width=5, justify='left',state=DISABLED)
txtcoffee.grid(row=2, column=7)
txtwater = Entry(f1aa, font=('arial',12), bg="#FDF3F0",bd=2,textvariable=D_Water, width=5, justify='left',state=DISABLED)
txtwater.grid(row=3, column=7)
txtvegroll = Entry(f1aa, font=('arial',12), bg="#FDF3F0",bd=2, width=5,textvariable=S_Vroll, justify='left',state=DISABLED)
txtvegroll.grid(row=5, column=7)
txteggroll = Entry(f1aa, font=('arial',12), bg="#FDF3F0",bd=2, width=5, justify='left',textvariable=S_Eroll,state=DISABLED)
txteggroll.grid(row=6, column=7)
txtchickenroll = Entry(f1aa, font=('arial',12),bg="#FDF3F0", bd=2, width=5, justify='left',textvariable=S_Croll,state=DISABLED)
txtchickenroll.grid(row=7, column=7)
txtpaneerroll = Entry(f1aa, font=('arial',12), bg="#FDF3F0",bd=2, width=5, justify='left',textvariable=S_Proll,state=DISABLED)
txtpaneerroll.grid(row=8, column=7)
txtsawarmaroll = Entry(f1aa, font=('arial',12), bg="#FDF3F0",bd=2, width=5, justify='left',textvariable=S_Sroll,state=DISABLED)
txtsawarmaroll.grid(row=9, column=7)

#=============================Section 2 Widgets===========================================
txtvegchow = Entry(f1ab, font=('arial',12), bd=2,bg="#FDF3F0",textvariable=C_Vchow, width=5, justify='left',state=DISABLED)
txtvegchow.grid(row=1, column=7)
txteggchow = Entry(f1ab, font=('arial',12), bd=2, bg="#FDF3F0",width=5,textvariable=C_Echow, justify='left',state=DISABLED)
txteggchow.grid(row=2, column=7)
txtchickenchow = Entry(f1ab, font=('arial',12), bd=2, bg="#FDF3F0",width=5,textvariable=C_Cchow, justify='left',state=DISABLED)
txtchickenchow.grid(row=3, column=7)
txtvegfried = Entry(f1ab, font=('arial',12), bd=2, bg="#FDF3F0",width=5,textvariable=C_Vrice, justify='left',state=DISABLED)
txtvegfried.grid(row=4, column=7)
txteggfried = Entry(f1ab, font=('arial',12), bd=2, bg="#FDF3F0",width=5,textvariable=C_Erice, justify='left',state=DISABLED)
txteggfried.grid(row=5, column=7)
txtchickenfried = Entry(f1ab, font=('arial',12), bd=2, bg="#FDF3F0",width=5,textvariable=C_Crice, justify='left',state=DISABLED)
txtchickenfried.grid(row=6, column=7)
txtpepsi = Entry(f1ab, font=('arial',12), bd=2, width=5, bg="#FDF3F0",justify='left',textvariable=P_pepsi,state=DISABLED)
txtpepsi.grid(row=8, column=7)
txtmojito = Entry(f1ab, font=('arial',12), bd=2, width=5, bg="#FDF3F0",justify='left',textvariable=P_mojito,state=DISABLED)
txtmojito.grid(row=9, column=7)

#=============================information===========================================

lblrecipt = Label(fta,font=('arial',12 ,'bold'),text="Receipt",bd=5).grid(row=0, column=0,sticky=W)
txtReceipt = Text(fta,font=('arial',11,'bold'),bd=8,width=50)
txtReceipt.grid(row=1,column=0)


#==============Clock================





#=============================Item Payment===========================================

lblCostofSection1 = Label(f1ba,padx=5,pady=10, font=('arial',15,'bold'),text="Cost of Items\t\t",fg="#F2F2F2")
lblCostofSection1.grid(row=0,column=0,sticky=W)
txtCostofSection1=Entry(f1ba,font=('arial',12,'bold'),width=10,textvariable=CostofItem,bg="#FEB642",justify='left')
txtCostofSection1.grid(row=0,column=2)
lblCostofSection1.configure(background="#FEB642")


lblCostofSection2 = Label(f1ba,padx=5, font=('arial',15,'bold'),pady=10,text="CGST tax \t\t\t",fg="#F2F2F2")
lblCostofSection2.grid(row=1,column=0)
txtCostofSection2=Entry(f1ba,font=('arial',12,'bold'),width=10,textvariable=cgst,bg="#FEB642", justify='left')
txtCostofSection2.grid(row=1,column=2)
lblCostofSection2.configure(background="#FEB642")



lblCostofSection3 = Label(f1ba,padx=5, font=('arial',15,'bold'),pady=10,text="SGST tax\t\t\t",fg="#F2F2F2")
lblCostofSection3.grid(row=2,column=0,sticky=W)
txtCostofSection3=Entry(f1ba,font=('arial',12,'bold'),width=10,textvariable=sgst,bg="#FEB642", justify='left')
txtCostofSection3.grid(row=2,column=2)
lblCostofSection3.configure(background="#FEB642")


lblCostofSection4 = Label(f1ba,padx=5, font=('arial',15,'bold'),pady=10,text="Subtotal\t\t\t",fg="#F2F2F2")
lblCostofSection4.grid(row=3,column=0,sticky=W)
txtCostofSection4=Entry(f1ba,font=('arial',12,'bold'),width=10, textvariable=SubTotal,bg="#FEB642",justify='left')
txtCostofSection4.grid(row=3,column=2)
lblCostofSection4.configure(background="#FEB642")




lblCostofSection5 = Label(f1ba,padx=5, font=('arial',15,'bold'),pady=10,text="Total\t\t\t",fg="#F2F2F2")
lblCostofSection5.grid(row=4,column=0,sticky=W)
txtCostofSection5=Entry(f1ba,font=('arial',12,'bold'),width=10,bg="#FEB642", textvariable=TotalCost,justify='left')
txtCostofSection5.grid(row=4,column=2)
lblCostofSection5.configure(background="#FEB642")


#=======================Labels==============================================

x=Label(f1ba, text="₹",fg="#F2F2F2",bg="#FEB642",font=('arial',8)).grid(row=0,column=1)
x=Label(f1ba, text="₹",fg="#F2F2F2",bg="#FEB642",font=('arial',8)).grid(row=1,column=1)
x=Label(f1ba, text="₹",fg="#F2F2F2",bg="#FEB642",font=('arial',8)).grid(row=2,column=1)
x=Label(f1ba, text="₹",fg="#F2F2F2",bg="#FEB642",font=('arial',8)).grid(row=3,column=1)
x=Label(f1ba, text="₹",fg="#F2F2F2",bg="#FEB642",font=('arial',8)).grid(row=4,column=1)

#=============================order information===========================================

order=Label(f1bb, font=('Courier',20,'bold'),bg="#FEB642",anchor='w',text="Order Us\t\t").grid(row=0,column=0)
yname=Label(f1bb, font=('Courier',8,'bold'),bg="#FEB642",anchor='w',text="Your Name\t").grid(row=2,column=0,sticky=W)
txtYourname = Entry(f1bb, font=('arial',10), bd=2, width=25, bg="#FEB642",justify='left',textvariable=y_name,state=NORMAL)
txtYourname.grid(row=3, column=0, sticky=W)

ynumber=Label(f1bb, font=('Courier',10,'bold'),bg="#FEB642",anchor='w',text="Phone Number\t").grid(row=4,column=0,sticky=W)
txtYournumber = Entry(f1bb, font=('arial',10), bd=2, width=25, bg="#FEB642",justify='left',textvariable=y_number,state=NORMAL)
txtYournumber.grid(row=5, column=0, sticky=W)

yemail=Label(f1bb, font=('Courier',10,'bold'),bg="#FEB642",anchor='w',text="Email\t").grid(row=6,column=0,sticky=W)
txtYouremail = Entry(f1bb, font=('arial',10), bd=2, width=25, bg="#FEB642",justify='left',textvariable=y_email,state=NORMAL)
txtYouremail.grid(row=7, column=0, sticky=W)
#=============================information===========================================






#=============================button===========================================

btnTotal=Button(fa2,padx=12,pady=1,bd=1,fg="black",font=('arial',12,'bold'),width=4,height=1, text="Total",command= Costof).grid(row=0,column=0)
btnRecipt=Button(fa2,padx=12,pady=1,bd=1,fg="black",font=('arial',12,'bold'),width=6,height=1, text="View",command= database).grid(row=0,column=1)
btnOrder=Button(fa2,padx=12,pady=1,bd=1,fg="black",font=('arial',12,'bold'),width=4,height=1, text="Order",command=orderItem).grid(row=0,column=2)
btnReset=Button(fa2,padx=12,pady=1,bd=1,fg="black",font=('arial',12,'bold'),width=4,height=1, text="Reset",command=reset).grid(row=0,column=3)
btnExit=Button(fa2,padx=12,pady=1,bd=1,fg="black",font=('arial',12,'bold'),width=4,height=1, text="Exit",command= quit).grid(row=0,column=4)
txtdev=Label(fa2,fg="black", font=("Time",8),text="Deepjyoti Dutta").grid(row=1,column=0)






root.mainloop()



