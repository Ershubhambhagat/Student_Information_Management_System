from tkinter import ttk
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
import time
import pandas
import random
import pymysql
###############################___Connect DB___########################
def connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+850+300')
    # dbroot.iconbitmap('.img\\Pce_purnea.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='Black')
    ###############################___Connect db Lebel___#################################
    hostlabel = Label(dbroot, text="Enter Host Name:- ", bg='gold', relief=RIDGE, font=(30), width=18, borderwidth=3,
                      anchor='w')
    hostlabel.place(x=10, y=20)

    userlabel = Label(dbroot, text="Enter User Name:- ", bg='gold', relief=RIDGE, font=(30), width=18, borderwidth=3,
                      anchor='w')
    userlabel.place(x=10, y=80)

    passwordlabel = Label(dbroot, text="Enter Password:-    ", bg='gold', relief=RIDGE, font=(30), width=18,
                          borderwidth=3, anchor='w')
    passwordlabel.place(x=10, y=140)

    ###############################___Connect Entry BoX___################
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        print(host, user, password)
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                "Notification", 'Given data is Incorrect \n''\nTry again', parent=dbroot)
            return
        try:
            crt = 'create database psms'
            mycursor.execute(crt)
            crt = 'use psms'
            mycursor.execute(crt)
            crt = 'create table psms(registration varchar(11) ,name varchar(20),branch varchar(35),mobile varchar(20),' \
                  'email varchar(30),gender varchar(20),address varchar(50),date varchar(10),time varchar(10));'
            mycursor.execute(crt)
            messagebox.showinfo(
                'Notification', 'Now You are Created and connect into  Database')
        except:
            crt = 'use psms'
            mycursor.execute(crt)
            messagebox.showinfo(
                'Notification', 'Now You are connect into  Database')
        dbroot.destroy()

    #############################################___host DB___#########################################################
    hostval = StringVar()
    # hostval.set('localhost')  # _REMOVE_####

    hostentry = Entry(dbroot, font=('roman,15,bold'),
                      bd=5, width=18, textvariable=hostval)
    hostentry.place(x=240, y=20)
    # print(hostval)
    #############################################___User DB___#########################################################
    userval = StringVar()
    # userval.set('root')  # _REMOVE_####
    userentry = Entry(dbroot, font=('roman,15,bold'),
                      bd=5, width=18, textvariable=userval)
    userentry.place(x=240, y=80)

    # print(user)
    ############################################___Password DB___#########################################

    passwordval = StringVar()
    # passwordval.set('Shubham@123')
    ####_REMOVE_####

    passwordentry = Entry(dbroot, font=('roman,15,bold'),
                          bd=5, width=18, textvariable=passwordval)
    passwordentry.place(x=240, y=140)
    # print(password)###___remove___######

    #############################___Submit db button___################################

    submitbotton = Button(dbroot, text="Submit", font=('roman', 15, 'bold '), borderwidth=10, bd=8, bg='red',
                          activebackground='black', activeforeground='white', command=submitdb)
    submitbotton.place(x=200, y=190)

    dbroot.mainloop()
    
###############################___Define Time And Date___##########################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date:' + date_string + "\n" + "Time :" + time_string)
    clock.after(200, tick)


##############################___Colour Name for choose Random color from this____#######################
colors = ['red', 'blue', 'yellow', 'pink', 'black', 'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
          'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20']

#####################################___Random color used___############################################


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(50, IntroLabelColorTick)

#############################___Intro Slider Blink ___################################
def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300, IntroLabelTick)

############################Main start___INTRO____######################################
root = Tk()
root.title(" Student  Management   System                       "
           "                                                                                         "
           "                                              "
           "By @Er_Shubham_Bhagat{ECE}")
root.config(bg='lightBlue3')
root.geometry('1200x700+202+18')
# root.iconbitmap('.img\\Pce_purnea.ico')
root.resizable(False, False)

###########################___slide Word Frame___###########################################

###########################___Data Enter Frame___######################################
DataEntryFrame = Frame(root, bg='black', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=40, y=100, width=500, height=600)

frontlable = Label(DataEntryFrame, text="---WELCOME---",
                   bg='red', width=25, font=('arial', 20, 'italic bold'))
frontlable.pack(side=TOP, expand=True)

########################___2 show Date Frame___###########################################

ShowDataFrame = Frame(root, bg='Black', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=640, y=100, width=500, height=600)

########################___2 show Date Frame___###########################################
########################___2 show Date Frame___###########################################
style = ttk.Style()
style.configure('Treeview.Heading', font=(
    'Book Antiqua', 15, 'bold'), bg='red', foreground='Black')
style.configure('Treeview', font=('System', 10, 'bold'),
                bg='red', foreground='Black')

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

studenttable = Treeview(ShowDataFrame, column=('Registration', 'Name', 'Branch', 'Phone No', 'Email Id', 'Gender',
                                               'Address', 'Added Time', 'Added Date'),
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Registration', text='Registration')
studenttable.heading('Name', text='Name')
studenttable.heading('Branch', text='Branch', anchor='w')
studenttable.heading('Phone No', text='Phone No')
studenttable.heading('Email Id', text='Email Id', anchor='w')
studenttable.heading('Gender', text='Gender', anchor='w')
studenttable.heading('Address', text='Address')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Registration', width=140)
studenttable.column('Gender', width=100)
####()####
studenttable.pack(fill=BOTH, expand=1)


####&&&&&&&&&&&&&&&&&&&&&&&&&&___Add student___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###############
def addstudent():
    print('Add Studnt Click')

    def submitadd():  # add student submit Button CMD
        print('Add Submit button click')
        reg = regval.get()
        name = nameval.get()
        branch = branchval.get()
        gendar = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        add = addressval.get()
        time1 = time.strftime("%H:%M:%S")
        date1 = time.strftime("%d/%m/%Y")
        try:
            crt = 'insert into psms values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(crt, (reg, name, branch, mobile,
                                   email, gendar, add, time1, date1))
            con.commit()
            res = messagebox.showinfo('Notification', 'Added successfully', parent=addroot)
            print(res)
            if (res == True):
                reg.set('')
                name.set('')
                branch.set('')
                gendar.set('')
                mobile.set('')
                email.set('')
                add.set('')
                time1.set('')
                date1.set('')
        except:
            print('Reg', reg, 'Name:-', name, 'Branch:-', branch, 'Gender;-', gendar, 'Mobile:-', mobile,
                  'Email:-', email, 'Address:-', add, 'Time:-', time1, 'Date:-', date1)
            messagebox.showerror(
                'Notification', 'Id already exit', parent=addroot)
        crt = 'select * from psms'
        mycursor.execute(crt)
        datas = mycursor.fetchall()
        print(datas)
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            # print(aa)
            studenttable.insert('', END, values=aa)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Add Student')
    addroot.config(bg='black')
    addroot.iconbitmap('add_student.ico')  ##if i wnat to add this i make change .img\\add_student.ico
    addroot.resizable(False, False)

    ############################___Add student level___#############################

    regleble = Label(addroot, text='Registation No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                     borderwidth=3, anchor='w')
    
    regleble.place(x=10, y=10)

    nameleble = Label(addroot, text='Enter Name:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                      borderwidth=3, anchor='w')
    nameleble.place(x=10, y=70)

    branchleble = Label(addroot, text='Enter Branch :-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                        borderwidth=3, anchor='w')
    branchleble.place(x=10, y=130)

    genderleble = Label(addroot, text='Enter Gender:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                        borderwidth=3, anchor='w')
    genderleble.place(x=10, y=190)

    mobilleble = Label(addroot, text='Enter Mobile No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                       borderwidth=3, anchor='w')
    mobilleble.place(x=10, y=250)

    emailleble = Label(addroot, text='Enter Email Id:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                       borderwidth=3, anchor='w')
    emailleble.place(x=10, y=310)

    addressleble = Label(addroot, text='Enter Address:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                         borderwidth=3, anchor='w')
    addressleble.place(x=10, y=370)

    #####################################___Add Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(addroot,show="shubham", font=("roman", 15, 'bold'),
                     bd=5, textvariable=regval)
    regentry.place(x=250, y=10)
    # regentry.insert(0,"shubham")

    nameval = StringVar()
    nameentry = Entry(addroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    branchval = StringVar()
    branchentry = Entry(addroot, font=("roman", 15, 'bold'),
                        bd=5, textvariable=branchval)
    branchentry.place(x=250, y=130)

    genderval = StringVar()
    genderentry = Entry(addroot, font=("roman", 15, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=250, y=190)

    mobileval = StringVar()
    mobentryentry = Entry(addroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=mobileval)
    mobentryentry.place(x=250, y=250)

    emailval = StringVar()
    emailentry = Entry(addroot, font=("roman", 15, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=250, y=310)

    addressval = StringVar()
    addressentry = Entry(addroot, font=("roman", 15, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=250, y=370)
    ################################___REMOVE IT___##########################################################
    # reg = regval.set(171041******)
    # name = nameval.set('Shubham Kumar')
    branch = branchval.set('ECE')
    # gender = genderval.set('Male')
    # mobile = mobileval.set('7319*****')
    email = emailval.set('Er.shubhamBhagat@gmail.com')
    # add = addressval.set('Sangrampur')

    #######&&&&&&&&&&&&&&&&&&&&&&___Submit___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&########

    submitbtn = Button(addroot, text='Submit', font=('roman', 15, "bold"), width=20, bg="red",
                       bd=6, activebackground='gold2', activeforeground='red', command=submitadd)
    submitbtn.place(x=150, y=420)

    ############################___submit  botton(Add)___#################################

    # print(reg, nameval, branchval, gender, mobile, email, add, times, date)

    addroot.mainloop()


################################___Add student upper layoyt__################################################
addbtn = Button(DataEntryFrame, text="1.Add Student", width=25, font=('chiller', 20, 'bold'), relief=RIDGE,
                bg='skyblue', bd=5,
                activebackground='red', activeforeground='white', command=addstudent)
addbtn.pack(side=TOP, expand=True)


####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&____Search Student___&&&&&&&&&&&&&&&&&&&&######################
def searchstudent():
    def submitsearch():  # submit Button CMD

        print("search")
        reg = regval.get()
        name = nameval.get()
        branch = branchval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        add = addressval.get()
        time1 = time.strftime("%H:%M:%S")
        date1 = time.strftime("%d/%m/%Y")
        if (reg != ''):
            crt = 'select *from psms where registration=%s'
            mycursor.execute(crt, (reg))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (name != ''):
            crt = 'select *from psms where name=%s'
            mycursor.execute(crt, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (branch != ''):
            crt = 'select *from psms where branch=%s'
            mycursor.execute(crt, (branch))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (gender != ''):
            crt = 'select *from psms where gender=%s'
            mycursor.execute(crt, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (mobile != ''):
            crt = 'select *from psms where mobile=%s'
            mycursor.execute(crt, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (email != ''):
            crt = 'select *from psms where email=%s'
            mycursor.execute(crt, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (add != ''):
            crt = 'select *from psms where address=%s'
            mycursor.execute(crt, (add))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (date1 != ''):
            crt = 'select *from psms where date=%s'
            mycursor.execute(crt, (date1))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)
        elif (time1 != ''):
            crt = 'select *from psms where time=%s'
            mycursor.execute(crt, (time1))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=aa)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x550+220+200')
    searchroot.title('Serch Student')
    searchroot.config(bg='firebrick1')
    # searchroot.iconbitmap('.img\\Pce_purnea.ico')
    searchroot.resizable(False, False)
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, "bold"), width=20, bg="red", bd=6,
                       activebackground='gold2', activeforeground='white', command=submitsearch)
    submitbtn.place(x=150, y=480)
    ############################___serch student level___#############################

    regleble = Label(searchroot, text='Registation No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                     borderwidth=3, anchor='w')
    regleble.place(x=10, y=10)

    nameleble = Label(searchroot, text='Enter Name:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                      borderwidth=3, anchor='w')
    nameleble.place(x=10, y=70)

    branchleble = Label(searchroot, text='Enter Branch :-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    branchleble.place(x=10, y=130)

    genderleble = Label(searchroot, text='Enter Gender:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    genderleble.place(x=10, y=190)

    mobilleble = Label(searchroot, text='Enter Mobile No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    mobilleble.place(x=10, y=250)

    emailleble = Label(searchroot, text='Enter Email Id:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    emailleble.place(x=10, y=310)

    addressleble = Label(searchroot, text='Enter Address:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                         width=12,
                         borderwidth=3, anchor='w')
    addressleble.place(x=10, y=370)

    adddateleble = Label(searchroot, text='Enter Date:-', bg='gold2', font=('time', 20, 'bold'), relief=RIDGE, width=12,
                         borderwidth=3, anchor="w")
    adddateleble.place(x=10, y=430)
    #####################################___Search Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(searchroot, font=("roman", 15, 'bold'),
                     bd=5, textvariable=regval)
    regentry.place(x=250, y=10)

    nameval = StringVar()
    nameentry = Entry(searchroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    branchval = StringVar()
    branchentry = Entry(searchroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=branchval)
    branchentry.place(x=250, y=130)

    genderval = StringVar()
    genderentry = Entry(searchroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=190)

    mobileval = StringVar()
    mobentryentry = Entry(searchroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=mobileval)
    mobentryentry.place(x=250, y=250)

    emailval = StringVar()
    emailentry = Entry(searchroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=310)

    addressval = StringVar()
    addressentry = Entry(searchroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=370)

    dateval = StringVar()
    dateentry = Entry(searchroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    #############################___Add (submit  button)___#################################

    searchroot.mainloop()


searchbtn = Button(DataEntryFrame, text="2.Search Student", width=25, font=('chiller', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='red', activeforeground='white', command=searchstudent)
searchbtn.pack(side=TOP, expand=True)


########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Delete___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###################

def deletestudent():
    print("3.Delete Student")
    store = studenttable.focus()
    content = studenttable.item(store)
    pp = content['values'][0]
    crt = 'delete from psms where registration=%s'
    mycursor.execute(crt, (pp))
    con.commit()
    messagebox.showinfo('Notification', 'reg{} deleted successfully')
    crt = 'select *from psms'
    mycursor.execute(crt)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=aa)


deletebtn = Button(DataEntryFrame, text="3.Delete Student", width=25, font=('chiller', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='red', activeforeground='white', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)


#########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Update___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&########################
def updatestudent():
    print("4.Update Student Click")###___remove___#######
    

    def submitupdate():  # submit Button CMD
        reg = regval.get()
        name = nameval.get()
        branch = branchval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        add = addressval.get()
        time1 = timeval.get()
        date1 = timeval.get()
        print("update submit button  Click")###___remove___#######
        crt = 'update psms set name=%s,branch=%s,gender=%s,mobile=%s,email=%s,address=%s,time=%s,date=%s where registration=%s'
        mycursor.execute(crt, (name, branch, gender, mobile,
                               email, add, date1, time1, reg))
        con.commit()
        crt = 'select *from psms'
        mycursor.execute(crt)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=aa)
        messagebox.showinfo('Notification', 'reg {} updated successfully'.format(reg))
        print("4.Update Student Click")###___remove___#######

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+100+185')
    updateroot.title('Update Student')
    updateroot.config(bg='#80461B')
    # updateroot.
    # bitmap('.img\\Pce_purnea.ico')
    updateroot.resizable(False, False)
    ############################___UPDATE_student level___#############################

    regleble = Label(updateroot, text='Registation No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                     width=12, borderwidth=3, anchor='w')
    regleble.place(x=10, y=10)

    nameleble = Label(updateroot, text='Enter Name:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                      width=12, borderwidth=3, anchor='w')
    nameleble.place(x=10, y=70)

    branchleble = Label(updateroot, text='Enter Branch :-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12, borderwidth=3, anchor='w')
    branchleble.place(x=10, y=130)

    genderleble = Label(updateroot, text='Mobile No:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12, borderwidth=3, anchor='w')
    genderleble.place(x=10, y=190)

    mobilleble = Label(updateroot, text='Enter Email Id:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12, borderwidth=3, anchor='w')
    mobilleble.place(x=10, y=250)

    emailleble = Label(updateroot, text='Gender:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12, borderwidth=3, anchor='w')
    emailleble.place(x=10, y=310)

    addressleble = Label(updateroot, text='Enter Address:-', bg='gold', font=('times', 20, 'bold'), relief=RIDGE,
                         width=12, borderwidth=3, anchor='w')
    addressleble.place(x=10, y=370)

    dateleble = Label(updateroot, text='Enter Date:- ', bg='gold2', font=('time', 20, 'bold'), relief=RIDGE,
                      width=12, borderwidth=3, anchor="w")
    dateleble.place(x=10, y=430)

    timeleble = Label(updateroot, text='Enter Time:-', bg='gold2', font=('time', 20, 'bold'), relief=RIDGE,
                      width=12, borderwidth=3, anchor="w")
    timeleble.place(x=10, y=490)
    #####################################___Search Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(updateroot, font=("roman", 15, 'bold'),
                     bd=5, textvariable=regval)
    regentry.place(x=250, y=10)

    nameval = StringVar()
    nameentry = Entry(updateroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    branchval = StringVar()
    branchentry = Entry(updateroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=branchval)
    branchentry.place(x=250, y=130)

    genderval = StringVar()
    genderentry = Entry(updateroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=190)

    mobileval = StringVar()
    mobentryentry = Entry(updateroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=mobileval)
    mobentryentry.place(x=250, y=250)

    emailval = StringVar()
    emailentry = Entry(updateroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=310)

    addressval = StringVar()
    addressentry = Entry(updateroot, font=(
        "roman", 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=370)

    dateval = StringVar()
    dateentry = Entry(updateroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeval = StringVar()
    timeentry = Entry(updateroot, font=("roman", 15, 'bold'),
                      bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)

    #############################___Add (submit  button)___#################################

    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, "bold"), width=20, bg="red", bd=6,
                       activebackground='gold2', activeforeground='red', command=submitupdate)
    submitbtn.place(x=150, y=535)
    aa = studenttable.focus()
    content = studenttable.item(aa)
    pp = content['values']
    if (len(pp) != 0):
        regval.set(pp[0])
        nameval.set(pp[1])
        branchval.set(pp[2])
        genderval.set(pp[3])
        mobileval.set(pp[4])
        emailval.set(pp[5])
        addressval.set(pp[6])
        timeval.set(pp[7])
        dateval.set(pp[8])
    updateroot.mainloop()
updatebtn = Button(DataEntryFrame, text="4.Update Student", width=25, font=('chiller', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='red', activeforeground='white', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)


############&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Show All___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##############################
def Showallstudent():
    print("5. Show all")
    crt = 'select *from psms'
    mycursor.execute(crt)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=aa)


showbtn = Button(DataEntryFrame, text="5. Show all", width=25, font=('chiller', 20, 'bold'), relief=RIDGE, bg='skyblue',
                 bd=5,
                 activebackground='red', activeforeground='white', command=Showallstudent)
showbtn.pack(side=TOP, expand=True)


#######&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Export Student___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#############
def Exportstudent():
    sh = filedialog.asksaveasfilename()
    print("click on Export Data")
    ub = studenttable.get_children()
    registration, name, branch, gender, mobile, email, address, date, time = [
    ], [], [], [], [], [], [], [], [],
    for i in ub:
        content = studenttable.item(i)
        pp = content['values']
        registration.append(pp[0]), name.append(pp[1]), branch.append(pp[2]), gender.append(pp[3]), mobile.append(
            pp[4]),
        email.append(pp[5]), address.append(
            pp[6]), date.append(pp[7]), time.append(pp[8])

    dd = ['Registration', 'Name', 'Branch', 'Gender',
          'Mobile No', 'Email Id', 'Address', 'Date', 'Time']
    df = pandas.DataFrame(list(zip(registration, name, branch,
                                   gender, mobile, email, address, date, time)), columns=dd)
    path = r'{}.csv'.format(sh)
    df.to_csv(path, index=False)
    messagebox.showinfo('Notification', 'Student data is save{}'.format(path))


exportbtn = Button(DataEntryFrame, text="6.Export Data", width=25, font=('chiller', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='red', activeforeground='white', command=Exportstudent)
exportbtn.pack(side=TOP, expand=True)


#######&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Exit___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####################
def Exitstudent():
    print("you click Exit")
    exitbox = messagebox.askyesno("Notification", "Do you want to Exit")
    # print(Exitbox)
    if (exitbox == True):
        root.destroy()


exitbtn = Button(DataEntryFrame, text="7. Exit", width=25, font=('chiller', 20, 'bold'), relief=RIDGE, bg='skyblue',
                 bd=5,
                 activebackground='red', activeforeground='white', command=Exitstudent)
exitbtn.pack(side=TOP, expand=True)

###########################___Slider Word_Design___###################
ss = 'Welcome To PCE_PURNEA '
count = 0
text = ''

SliderLabel = Label(root, text=ss, bg='#031d2e', relief=RIDGE, font=('roman', 30, ' bold'), width=35,
                    borderwidth=5)
SliderLabel.place(x=220, y=0)
IntroLabelTick()
IntroLabelColorTick()

##########################___clock___###################################################

clock = Label(root, bg='wheat1', relief=RIDGE, font=('red', 15, 'italic bold'), activebackground='red', width=15,
              borderwidth=4)
clock.place(x=0, y=0)
tick()

#########################___Created DataBase Botton___###########################################

connectbutton = Button(root, text="Connect Data Base", width=15, font=('red', 20, 'italic bold'),
                       borderwidth=6, bd=6, bg='lightBlue4', activebackground='black',
                       activeforeground='white', command=connectdb)
connectbutton.place(x=920, y=2)




















def help():
    help_s=Toplevel()
    # help_s.grab_set()
    help_s.geometry('540x250+500+200')
    help_s.resizable(False, False)
    help_s.config(bg='Black')
    label = Label(help_s,text="I am Shubham Kumar (ECE {2017}) and Reg No:-17104131027\n"
        "if you facing any problems in Softwere you contacts on \t"   " \n whatapp(7319944888) or \n Email:- Er.shubhambhagat@gmail.com\n"
     " \n\t\nMost Welcome For your Feedback""\n\n\n Thank You",    
        font=('times',15, 'bold'),
        fg="white",
        bg="black"    )
    label.pack()
helpbox = Button(root,text="Help", width=5, font=('red', 10, 'italic bold'),
                        borderwidth=8, bd=6, bg='red', activebackground='black',
                        activeforeground='white', command=help)
helpbox.place(x=1140, y=660)

# root_help.mainloop()














root.mainloop()
