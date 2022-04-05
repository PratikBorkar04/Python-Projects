from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
#----------------------------------------------------------
base =Tk()
base.geometry("1000x480+120+85")
base.title("Girls Hostel")
photo = ImageTk.PhotoImage(Image.open("Hostel.png"))
#-----------------------------------------------------------
canvas = Canvas(width=20000,height=20000,bg="white")
canvas.place(x=0,y=0)
canvas.create_image(25,72,image=photo, anchor= NW )
#-----------------------------------------------------------
def method1():
    base.destroy()
#----------------------------------------------------------
site=Label(base,width=2100,bg="White")
site.place(x=0,y=1)
site1=Label(base,width=2100,bg="White")
site1.place(x=0,y=7)
headline=Label(base,width=73,text="Hostelrooms",bg="Black",fg="White",font=("arial","18"))
headline.place(x=0,y=29)
arrowleft=Button(base,text="<-",fg="black")
arrowleft.place(x=1,y=2)
arrowright=Button(base,text="->",fg="black")
arrowright.place(x=24,y=2)
cancel=Button(base,text="X",bg="Red",fg="white",width=4,command=method1)
cancel.place(x=950,y=2)
refresh=Button(base,text="(^)",fg="black")
refresh.place(x=48,y=2)
website=Label(base,fg="Black",text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)")
website.place(x=74,y=4)
name=Label(base,text="WELCOME",font=("Arial",20),fg="red",bg="white")
name.place(x=714,y=66)
but3=Button(base,width="12",text="Employee",bg="cyan",fg="Black")
but3.place(x=740,y=110)
name1=Label(base,text="Email / Mob-No.",font=("Georgia","14"),bg="white",fg="black")
name1.place(x=610,y=160)
ent1=Entry(base,width=25,bg="thistle1")
ent1.place(x=769,y=166)
name2=Label(base,text="Password",font=("Georgia","14"),bg="white",fg="black")
name2.place(x=610,y=210)
ent2=Entry(base,width=25,bg="thistle1")
ent2.place(x=769,y=216)


#====================================================================


def method():
        base1 =Tk()
        base1.geometry("1000x480+120+85")
        base1.title("Main page")
#-----------------------------------------------------------
        def method2():
            base1.destroy()
#-----------------------------------------------------------
        arrowleft=Button(base1,text="<-",fg="black")
        arrowleft.place(x=1,y=2)
        arrowright=Button(base1,text="->",fg="black")
        arrowright.place(x=24,y=2)
        refresh=Button(base1,text="(^)",fg="black")
        refresh.place(x=48,y=2)
        website=Label(base1,fg="Black",text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)/main page")
        website.place(x=74,y=4)
        cancel1=Button(base1,text="X",bg="Red",fg="white",width=4,command=method2)
        cancel1.place(x=950,y=2)
#---------------------------------------------------------------------
        def method9():
            base5 = Tk()
            base5.geometry("1000x370+120+195")
            base5.title("New Admission")

            arrowleft = Button(base5, text="<-", fg="black")
            arrowleft.place(x=1, y=2)
            arrowright = Button(base5, text="->", fg="black")
            arrowright.place(x=24, y=2)
            refresh = Button(base5, text="(^)", fg="black")
            refresh.place(x=48, y=2)
            website = Label(base5, fg="Black",text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)/main page/New admission/create")
            website.place(x=74, y=4)
#````````````````````````````````````````````````````````````````
            def method10():
                root1 = Tk()
                root1.geometry('685x368+436+195')
                root1.title("Create new")

                def open_txt():
                    text_file = open("gui-1.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()

                def save_txt():
                    text_file = open("gui-2.txt", "w")
                    text_file.write(my_text.get(1.0, END))

                my_text = Text(root1, width=75, height=20)
                my_text.place(x=20, y=20)
                buttonO = Button(root1, text="Open Form", command=open_txt, bg="green",fg="white")
                buttonO.place(x=200, y=210)

                buttonS = Button(root1, text="Confirm", command=save_txt,bg="orange",fg="white")
                buttonS.place(x=400, y=210)
                def method12():
                    root1.destroy()

                cancel1 = Button(root1, width=8,text="Submit", bg="Yellow", fg="Black", command=method12)
                cancel1.place(x=288, y=270)
                root1.mainloop()
#````````````````````````````````````````````````````````````````````````````````

            button1 = Button(base5, text="Create New", bg="blue", fg="white", width=12, command=method10)
            button1.place(x=50, y=85)
#all admissions--------------------------------------------------------
            def method12():
                root2 = Tk()
                root2.geometry('685x368+436+195')
                root2.title("All admissions")
                def open_txt():
                    text_file = open("gui-2.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()
                my_text = Text(root2, width=75, height=20)
                my_text.place(x=20, y=20)
                buttonO = Button(root2, text="open", command=open_txt, bg="green")
                buttonO.place(x=288, y=270)

            button2 = Button(base5, text="All Admissions", bg="blue", fg="white", width=12, command=method12)
            button2.place(x=50, y=155)
#----------------------------------------------------------------------
            def method11():
                base5.destroy()
            cancel1 = Button(base5, text="X", bg="Red", fg="white", width=4, command=method11)
            cancel1.place(x=950, y=2)
        button1=Button(base1,text="Admissions",bg="blue",fg="white",width=12,command=method9)
        button1.place(x=50,y=35)
#++++1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        def method3():
            base2 = Tk()
            base2.geometry("1000x370+120+195")
            base2.title("Fees")
#--------------------------------hostel fees-------------------------
            def method13():
                root3 = Tk()
                root3.geometry('368x368+436+195')
                root3.title("Hostel Fess")
                rbval = IntVar()
                rb1 = Radiobutton(root3, text="Monthly(1700)", variable=rbval, value=0)
                rb1.place(x=125, y=15)
                rb2 = Radiobutton(root3, text="Quarterly(4500)", variable=rbval, value=1)
                rb2.place(x=125, y=50)
                rb2 = Radiobutton(root3, text="Annualy(18500)", variable=rbval, value=2)
                rb2.place(x=125, y=85)
                ls = Listbox(root3, width=25, height=7)
                ls.insert(END, "  UPI")
                ls.insert(END, "  Cash")
                ls.insert(END, "  Net Banking")
                ls.insert(END, "  Cheque")
                ls.insert(END, "  Card Payment")
                ls.place(x=110, y=125)

                def method14():
                    root3.destroy()

                button2 = Button(root3, text="Pay", command=method14, bg="purple", fg="white", width=12)
                button2.place(x=132, y=300)
                root3.mainloop()
                def method14():
                    root4 = Tk()
                    root4.geometry('368x368+436+195')
                    root4.title("Mess Fess")
                    rbval = IntVar()
                    rb1 = Radiobutton(root4, text="Monthly(5000)", variable=rbval, value=0)
                    rb1.place(x=125, y=15)
                    rb2 = Radiobutton(root4, text="Quarterly(14000)", variable=rbval, value=1)
                    rb2.place(x=125, y=50)
                    rb2 = Radiobutton(root4, text="Annualy(53500)", variable=rbval, value=2)
                    rb2.place(x=125, y=85)
                    ls = Listbox(root4, width=25, height=7)
                    ls.insert(END, "  UPI")
                    ls.insert(END, "  Cash")
                    ls.insert(END, "  Net Banking")
                    ls.insert(END, "  Cheque")
                    ls.insert(END, "  Card Payment")
                    ls.place(x=110, y=125)

                    def method14():
                        root4.destroy()

                    button2 = Button(root4, text="Pay", command=method14, bg="purple", fg="white", width=12)
                    button2.place(x=132, y=300)
                    root4.mainloop()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            button1 = Button(base2,command=method13,text="Hostel", bg="blue", fg="white", width=12)
            button1.place(x=50, y=85)
#===============================Mess Fess=========================
            def method14():
                root4 = Tk()
                root4.geometry('368x368+436+195')
                root4.title("Mess Fess")
                rbval = IntVar()
                rb1 = Radiobutton(root4, text="Monthly(1700)", variable=rbval, value=0)
                rb1.place(x=125, y=15)
                rb2 = Radiobutton(root4, text="Quarterly(4500)", variable=rbval, value=1)
                rb2.place(x=125, y=50)
                rb2 = Radiobutton(root4, text="Annualy(18500)", variable=rbval, value=2)
                rb2.place(x=125, y=85)
                ls = Listbox(root4, width=25, height=7)
                ls.insert(END, "  UPI")
                ls.insert(END, "  Cash")
                ls.insert(END, "  Net Banking")
                ls.insert(END, "  Cheque")
                ls.insert(END, "  Card Payment")
                ls.place(x=110, y=125)
                def method14():
                    root4.destroy()
                button2 = Button(root4, text="Pay",command=method14, bg="purple", fg="white", width=12)
                button2.place(x=132, y=300)
                root4.mainloop()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            button2 = Button(base2,command=method14,text="Mess", bg="blue", fg="white", width=12)
            button2.place(x=50, y=155)
            arrowleft = Button(base2, text="<-", fg="black")
            arrowleft.place(x=1, y=2)
            arrowright = Button(base2, text="->", fg="black")
            arrowright.place(x=24, y=2)
            refresh = Button(base2, text="(^)", fg="black")
            refresh.place(x=48, y=2)
            website = Label(base2, fg="Black",text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)/main page/Fess/Hostel")
            website.place(x=74, y=4)
            def method4():
               base2.destroy()
            cancel1 = Button(base2, text="X", bg="Red", fg="white", width=4, command=method4)
            cancel1.place(x=950, y=2)
            base2.mainloop()
#++++++2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        button2=Button(base1,text="Fees",bg="blue",fg="white",width=12,command=method3)
        button2.place(x=215,y=35)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        def method15():
            root5 = Tk()
            root5.geometry('368x368+436+195')
            root5.title("Guest/Vistors")
#Guest-application
            def open_txt():
                text_file = open("gui-4.txt", "r")
                stuff = text_file.read()
                my_text.insert(END, stuff)
                text_file.close()

            def save_txt():
                text_file = open("gui-5.txt", "w")
                text_file.write(my_text.get(1.0, END))

            my_text = Text(root5, width=40, height=25)
            my_text.place(x=20, y=20)
            buttonO = Button(root5, text="Open", command=open_txt, bg="Orange",fg="White")
            buttonO.place(x=105, y=200)
            buttonO = Button(root5, text="Save", command=save_txt, bg="Purple",fg="White")
            buttonO.place(x=195, y=200)
            buttonS = Button(root5, text="Check all Visitors", command=save_txt,fg="White",bg="Blue")
            buttonS.place(x=125, y=250)
            def method16():
                root5.destroy()
            buttonb = Button(root5, text="<-back", command=method16, bg="Red",fg="White")
            buttonb.place(x=20, y=298)
            root5.mainloop()
        button3=Button(base1,command=method15,text="Visitors/Guest",bg="blue",fg="white",width=12)
        button3.place(x=380,y=35)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        def method5():
            base3 = Tk()
            base3.geometry("1000x370+120+195")
            base3.title("Student Profile")
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            def method17():
                root6 = Tk()
                root6.geometry('368x368+436+195')
                root6.title("Guest/Vistors")

                def open_txt():
                    text_file = open("gui-2.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()
                my_text = Text(root6, width=40, height=25)
                my_text.place(x=20, y=20)
                buttonO = Button(root6, text="Open", command=open_txt, bg="Orange", fg="White")
                buttonO.place(x=140, y=200)
                def method18():
                    root6.destroy()
                buttonb = Button(root6, text="<-back", command=method18, bg="Red", fg="White")
                buttonb.place(x=20, y=298)
                root6.mainloop()
            button1 = Button(base3,command=method17, text="Student Details", bg="blue", fg="white", width=12)
            button1.place(x=50, y=38)
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
            def method26():
                root25 = Tk()
                root25.geometry('368x368+436+195')
                root25.title("Vehicle")


                def open_txt():
                    text_file = open("gui-9.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()

                def save_txt():
                    text_file = open("gui-9.txt", "w")
                    text_file.write(my_text.get(1.0, END))

                my_text = Text(root25, width=40, height=25)
                my_text.place(x=20, y=20)
                buttonO = Button(root25, text="Open", command=open_txt, bg="Orange", fg="White")
                buttonO.place(x=105, y=200)
                buttonO = Button(root25, text="Save", command=save_txt, bg="Purple", fg="White")
                buttonO.place(x=195, y=200)
                buttonO = Button(root25, text="Check", command=open_txt, bg="Green", fg="White")
                buttonO.place(x=150, y=250)
                root25.mainloop()
            button2 = Button(base3,command=method26, text="Vehicle", bg="blue", fg="white", width=12)
            button2.place(x=300, y=38)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            def method25():
                root26 = Tk()
                root26.geometry('368x368+436+195')
                root26.title("Intime/Outime")


                def open_txt():
                    text_file = open("gui-10.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()

                def save_txt():
                    text_file = open("gui-10.txt", "w")
                    text_file.write(my_text.get(1.0, END))

                my_text = Text(root26, width=40, height=25)
                my_text.place(x=20, y=20)
                buttonO = Button(root26, text="Open", command=open_txt, bg="Orange", fg="White")
                buttonO.place(x=105, y=200)
                buttonO = Button(root26, text="Save", command=save_txt, bg="Purple", fg="White")
                buttonO.place(x=195, y=200)
                buttonO = Button(root26, text="Check", command=open_txt, bg="Green", fg="White")
                buttonO.place(x=150, y=250)
                root26.mainloop()
            button3 = Button(base3,command=method25, text="Intime/Outime", bg="blue", fg="white", width=12)
            button3.place(x=550, y=38)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            def method19():
                root7 = Tk()
                root7.geometry('685x368+436+195')
                root7.title("Leave application")
                def open_txt():
                    text_file = open("gui-6.txt", "r")
                    stuff = text_file.read()
                    my_text.insert(END, stuff)
                    text_file.close()
                my_text = Text(root7, width=120, height=25)
                my_text.place(x=20, y=20)
                buttonO = Button(root7, text="Check Application", command=open_txt, bg="Orange", fg="White")
                buttonO.place(x=20, y=258)
                def method20():
                    root7.destroy()
                buttonb = Button(root7, text="Approved", command=method20, bg="Green", fg="White")
                buttonb.place(x=20, y=298)
                root7.mainloop()
            button4 = Button(base3,command=method19, text="Leave Application", bg="blue", fg="white", width=14)
            button4.place(x=800, y=38)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            arrowleft = Button(base3, text="<-", fg="black")
            arrowleft.place(x=1, y=2)
            arrowright = Button(base3, text="->", fg="black")
            arrowright.place(x=24, y=2)
            refresh = Button(base3, text="(^)", fg="black")
            refresh.place(x=48, y=2)
            website = Label(base3, fg="Black",text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)/main page/Fess/Student Profile")
            website.place(x=74, y=4)
            def method6():
               base3.destroy()
            cancel1 = Button(base3, text="X", bg="Red", fg="white", width=4, command=method6)
            cancel1.place(x=950, y=2)
            base3.mainloop()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        button4=Button(base1,text="Student Report",bg="blue",fg="white",width=12,command=method5)
        button4.place(x=545,y=35)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def method7():
            base4 = Tk()
            base4.geometry("1000x370+120+195")
            base4.title("Rooms")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            def method20():
                root7 = Tk()
                root7.geometry('468x368+120+195')
                root7.title("Room Status")

                def method24():
                    root11 = Tk()
                    root11.geometry('468x108+645+245')
                    root11.title("Room1")

                    def open_txt():
                        text_file = open("gui-7.txt", "r")
                        stuff = text_file.read()
                        my_text.insert(END, stuff)
                        text_file.close()

                    my_text = Text(root11, width=40, height=5)
                    my_text.place(x=20, y=20)
                    buttonO = Button(root11, text="Check", command=open_txt, bg="green")
                    buttonO.place(x=155, y=80)
                    root11.mainloop()

                button1 = Button(root7, command=method24, text="Room1", bg="Sky Blue", fg="Black", width=12, )
                button1.place(x=102, y=38)
                button1 = Button(root7, command=method24, text="Room2", bg="Sky Blue", fg="Black", width=12, )
                button1.place(x=102, y=98)
                root7.mainloop()

            button1 = Button(base4,command=method20, text="View", bg="blue", fg="white", width=12)
            button1.place(x=100, y=38)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            def method21():
                root8 = Tk()
                root8.geometry('468x368+335+195')
                root8.title("Change Rooms")
                button1 = Button(root8, command=method21, text="Room1", bg="Pink", fg="Black", width=12, )
                button1.place(x=150, y=38)
                button1 = Button(root8, command=method21, text="Room2", bg="Pink", fg="Black", width=12, )
                button1.place(x=150, y=98)
                root8.mainloop()

            button2 = Button(base4,command=method21,text="Change", bg="blue", fg="white", width=12,)
            button2.place(x=400, y=38)
#_____________________________________________________________________
            def method22():
                root9 = Tk()
                root9.geometry('468x368+645+195')
                root9.title("Availablity Status")
                root9.mainloop()
            def method23():
                        root10 = Tk()
                        root10.geometry('468x308+645+245')
                        root10.title("Rooms")

                        def method24():
                            root11 = Tk()
                            root11.geometry('468x108+645+245')
                            root11.title("Room1")

                            def open_txt():
                                text_file = open("gui-7.txt", "r")
                                stuff = text_file.read()
                                my_text.insert(END, stuff)
                                text_file.close()

                            my_text = Text(root11, width=40, height=5)
                            my_text.place(x=20, y=20)
                            buttonO = Button(root11, text="Check", command=open_txt, bg="green")
                            buttonO.place(x=155, y=80)
                            root11.mainloop()
                        button1 = Button(root10,command=method24, text="Room1(Status)", bg="orange", fg="white", width=12, )
                        button1.place(x=70, y=38)
                        def method25():
                            root12 = Tk()
                            root12.geometry('468x108+645+245')
                            root12.title("Room1")

                            def open_txt():
                                text_file = open("gui-8.txt", "r")
                                stuff = text_file.read()
                                my_text.insert(END, stuff)
                                text_file.close()

                            my_text = Text(root12, width=40, height=5)
                            my_text.place(x=20, y=20)
                            buttonO = Button(root12, text="Check", command=open_txt, bg="green")
                            buttonO.place(x=155, y=80)
                            root12.mainloop()
                        button2 = Button(root10,command=method25, text="Room2(Status)", bg="orange", fg="white", width=12, )
                        button2.place(x=280, y=38)
                        root10.mainloop()
            button3 = Button(base4,command=method23,text="Available", bg="blue", fg="white", width=12,)
            button3.place(x=700, y=38)
#********************************************************************
            arrowleft = Button(base4, text="<-", fg="black")
            arrowleft.place(x=1, y=2)
            arrowright = Button(base4, text="->", fg="black")
            arrowright.place(x=24, y=2)
            refresh = Button(base4, text="(^)", fg="black")
            refresh.place(x=48, y=2)
            website = Label(base4, fg="Black",
                            text="(!-!)https://hostelrooms.com/hostel-website-Login-(student/employee)/main page/Fess/Rooms")
            website.place(x=74, y=4)
            def method8():
                base4.destroy()
            cancel1 = Button(base4, text="X", bg="Red", fg="white", width=4, command=method8)
            cancel1.place(x=950, y=2)
            base4.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        button5=Button(base1,text="Rooms",bg="blue",fg="white",width=12,command=method7)
        button5.place(x=710,y=35)
        button5=Button(base1,text="Logout",bg="blue",fg="white",width=12)
        button5.place(x=875,y=35)

        base1.mainloop()

#===========================================================================
but3=Button(base,width="12",text="Login",bg="blue",fg="white",command=method)
but3.place(x=730,y=250)
ent2=Label(base,text="Forgot password?",font=("arial","11"),fg="black",bg="white")
ent2.place(x=725,y=290)
but4=Button(base,width="12",text="Click Here",bg="Red",fg="White")
but4.place(x=728,y=330)
bottom=Label(base,bg="black",width=2100)
bottom.place(x=0,y=420)
bottom1=Label(base,bg="black",width=2100)
bottom1.place(x=0,y=440)
bottom2=Label(base,bg="black",width=2100)
bottom2.place(x=0,y=460)
bottom3=Label(base,bg="black",width=2100)
bottom3.place(x=0,y=480)
points=Label(base,font=("Berlin Sans FB Demi","15"),bg="Black",fg="white",text="# Best Hostel in City")
points.place(x=32,y=430)
points1=Label(base,font=("Berlin Sans FB Demi","15"),bg="Black",fg="white",text="# 8.8 out of 10 stars")
points1.place(x=290,y=430)
points2=Label(base,font=("Berlin Sans FB Demi","15"),bg="Black",fg="white",text="--   ( STAY WITH US , FELL AT HOME )   --")
points2.place(x=540,y=430)
#--------------------------------------------------------------------
base.mainloop()

