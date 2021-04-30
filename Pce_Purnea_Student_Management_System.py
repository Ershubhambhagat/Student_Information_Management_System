from tkinter import ttk
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
import time
import random
import pymysql


###############################___Connect DB___########################
def connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+850+300')
    # dbroot.iconbitmap('Pce_purnea.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='Black')
    ###############################___Connect db Lebel___#################################
    hostlabel = Label(dbroot, text="Enter Host Name:- ", bg='light Green', relief=RIDGE, font=(30), width=18,
                      borderwidth=3,
                      anchor='w')
    hostlabel.place(x=10, y=20)

    userlabel = Label(dbroot, text="Enter User Name:- ", bg='light Green', relief=RIDGE, font=(30), width=18,
                      borderwidth=3,
                      anchor='w')
    userlabel.place(x=10, y=80)

    passwordlabel = Label(dbroot, text="Enter Password:-    ", bg='light Green', relief=RIDGE, font=(30), width=18,
                          borderwidth=3, anchor='w')
    passwordlabel.place(x=10, y=140)

    ###############################___Connect Entry BoX___################
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        print(host, user, password) #remove
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                "Notification", 'Given data is Incorrect \n''\nTry again', parent=dbroot)
            return
        try:
            crt = 'create database pcesms'
            mycursor.execute(crt)
            crt = 'use pcesms'
            mycursor.execute(crt)
            crt = 'create table pcesms(registration varchar(11) NOT NULL,name varchar(30),father_name varchar(50),' \
                  'branch varchar(35),gender varchar(12),mobile varchar(15),email varchar(35),address varchar(80),Category varchar(20) ,' \
                  'dob varchar(20),session varchar(20)); '
            mycursor.execute(crt)
            messagebox.showinfo(
                'Notification', 'Now You are Created and connect into  Database')
        except:
            crt = 'use pcesms'
            mycursor.execute(crt)
            messagebox.showinfo(
                'Notification', 'Now You are connect into  Database')
        dbroot.destroy()

    #############################################___host DB___#########################################################
    hostval = StringVar()
    hostval.set('localhost')  # _REMOVE_####

    hostentry = Entry(dbroot, font=('roman,15,bold'),
                      bd=5, width=18, textvariable=hostval)
    hostentry.place(x=240, y=20)
    # print(hostval)
    #############################################___User DB___#########################################################
    userval = StringVar()
    userval.set('root')  # _REMOVE_####
    userentry = Entry(dbroot, font=('roman,15,bold'),
                      bd=5, width=18, textvariable=userval)
    userentry.place(x=240, y=80)

    # print(user)
    ############################################___Password DB___#########################################

    passwordval = StringVar()
    passwordval.set('Shubham@00')
    ####_REMOVE_####

    passwordentry = Entry(dbroot, font=('roman,15,bold'),
                          bd=5, width=18, textvariable=passwordval,show="*")
    passwordentry.place(x=240, y=140)
    # print(password)###___remove___######

    #############################___Submit db button___################################

    submitbotton = Button(dbroot, text="Submit", font=('ubuntu mono', 15, 'bold '), borderwidth=10, bd=8, bg='sky blue',
                          activebackground='green', activeforeground='blue', command=submitdb)
    submitbotton.place(x=200, y=190)

    dbroot.mainloop()


###############################___Define Time And Date___##########################
def tick():
    time_string = time.strftime("%I:%M:%S")
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
          'gray1']


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


############################___INTRO____######################################
root = Tk()
root.title(" Student Information Management System                       "
           "                                                                                   "
           "                                                                                     "
           "    By @Er_Shubham_Bhagat{ECE}")
root.config(bg='lightBlue3')
# root.geometry('1500x800+0+0')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print("height:-", height)
print("width:-", width)  # remove
# h=int(height)-0
# w=int(width)-0
# print("W",w)           #remove
# print("he",h)

root.geometry("%dx%d" % (width, height))
# root.iconbitmap('Pce_purnea.ico')
root.resizable(False, False)

###########################___slide Word Frame___###########################################

###########################___Data Enter Frame___######################################
DataEntryFrame = Frame(root, bg='black', relief=GROOVE, borderwidth=10)
DataEntryFrame.place(x=40, y=100, width=500, height=700)

frontlable = Label(DataEntryFrame, text="--- WELCOME ---",
                   bg='red', width=25, font=('ubuntu mono', 20, 'italic bold'))
frontlable.pack(side=TOP, expand=True)

########################___2 show Date Frame___###########################################

ShowDataFrame = Frame(root, bg='Black', relief=GROOVE, borderwidth=2)
ShowDataFrame.place(x=570, y=100, width=950, height=700)

########################___2 show Date Frame_ work__###########################################
style = ttk.Style()
style.configure('Treeview.Heading', font=(
    'Book Antiqua', 15, 'bold'), bg='red', foreground='Black')
style.configure('Treeview', font=('System', 10, 'bold'),
                bg='red', foreground='Black')

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

studenttable = Treeview(ShowDataFrame, column=('Registration', 'Name', 'Father Name', 'Branch', 'Gender',
                                               'Phone No', 'Email Id', 'Address','Category', 'dob', 'session'),
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Registration', text='Registration')
studenttable.heading('Name', text='Name',anchor='w')
studenttable.heading('Father Name', text='Father Name',anchor='w')
studenttable.heading('Branch', text='Branch', anchor='w')
studenttable.heading('Phone No', text='Phone No',anchor='w')
studenttable.heading('Email Id', text='Email Id', anchor='w')
studenttable.heading('Gender', text='Gender', anchor='w')
studenttable.heading('Category',text='Category',anchor='w')
studenttable.heading('Address', text='Address')
studenttable.heading('dob', text='D_O_B',anchor='w')
studenttable.heading('session', text='session',anchor='w')
studenttable['show'] = 'headings'
studenttable.column('Registration', width=140)
studenttable.column('Gender', width=100)
studenttable.pack(fill=BOTH, expand=1)


####&&&&&&&&&&&&&&&&&&&&&&&&&&___Add student___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###############
def addstudent():
    print('Add Studnt Click')

    def submitadd():  # add student submit Button CMD
        print('Add Submit button click')
        reg = regval.get()
        name = nameval.get()
        father_name = fatherval.get()
        branch = branchval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        add = addressval.get()
        cate = cateval.get()
        dob = dobval.get()
        session = sessionval.get()
        print("before", 'Reg', reg, 'Name:-', name, 'father Name:- ', father, 'Branch:-', branch, 'Gender;-', gender,
              'Mobile:-', mobile, 'Email:-', email, 'Address:-', add, 'Category:-', cate, 'DOB:-', dob,
              'session:-', session)  # remove
        try:
            crt = 'INSERT INTO pcesms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(crt, (reg, name, father_name, branch, gender, mobile,
                                   email, add, cate, dob, session))
            con.commit()
            res = messagebox.askyesnocancel('Notification',
                                            'id {} Name {} Added successfully' 'Want to clear the Form'.format(reg,
                                                                                                               name),
                                            parent=addroot)
            if (res == True):
                regval.set('')
                nameval.set('')
                fatherval.set('')
                branchval.set('')
                genderval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                cateval.set('')
                dobval.set('')
                sessionval.set('')

        except:
            print('Reg', reg, 'Name:-', name, 'father Name:- ', father, 'Branch:-', branch, 'Gender;-', gender,
                  'Mobile:-', mobile, 'Email:-', email, 'Address:-', add, 'Category:-', cate, 'DOB:-', dob,
                  'session:-', session)  # remove
            messagebox.showerror('Notification', 'Id already exit', parent=addroot)
        crt = 'select * from pcesms'
        mycursor.execute(crt)
        datas = mycursor.fetchall()
        print(datas)  # remove
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
            print(aa)  # remove
            studenttable.insert('', END, values=aa)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('508x710+70+85')
    addroot.title('Add Student')
    addroot.config(bg='black')
    # addroot.iconbitmap('add_student.ico')
    addroot.resizable(False, False)

    ############################___Add student level___#############################

    regleble = Label(addroot, text='Registration No:- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                     width=12,
                     borderwidth=3, anchor='w')
    regleble.place(x=10, y=10)

    nameleble = Label(addroot, text=' Name :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                      borderwidth=3, anchor='w')
    nameleble.place(x=10, y=70)

    fatherleble = Label(addroot, text=' Fathers Name :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    fatherleble.place(x=10, y=130)

    branchleble = Label(addroot, text=' Branch :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    branchleble.place(x=10, y=190)

    genderleble = Label(addroot, text=' Gender :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    genderleble.place(x=10, y=250)

    mobilleble = Label(addroot, text=' Mobile No :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    mobilleble.place(x=10, y=310)

    emailleble = Label(addroot, text=' Email Id :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    emailleble.place(x=10, y=370)

    addressleble = Label(addroot, text=' Address :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                         width=12,
                         borderwidth=3, anchor='w')
    addressleble.place(x=10, y=430)

    categorylebel = Label(addroot, text=' Category :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE,
                          width=12,
                          borderwidth=3, anchor='w')
    categorylebel.place(x=10, y=490)

    DOB = Label(addroot, text=' D.O.B :- ', bg='yellow', font=('light green', 20, 'bold'), relief=RIDGE, width=11,
                borderwidth=3, anchor='w')
    DOB.place(x=10, y=550)

    session = Label(addroot, text=' Session :- ', bg='yellow', font=('times', 20, 'bold'), relief=RIDGE, width=12,
                    borderwidth=3, anchor='w')
    session.place(x=10, y=610)

    #####################################___Add Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                     bd=5, textvariable=regval)
    regentry.place(x=230, y=10)

    nameval = StringVar()
    nameentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    fatherval = StringVar()
    father = Entry(addroot, font=("Open Sans", 17, 'bold'),  # Modify this line
                   bd=5, textvariable=fatherval)
    father.place(x=230, y=130)

    branchval = StringVar()
    branchentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                        bd=5, textvariable=branchval)
    branchentry.place(x=230, y=190)

    genderval = StringVar()
    genderentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=230, y=250)

    mobileval = StringVar()
    mobentryentry = Entry(addroot, font=(
        "Open Sans", 17, 'bold'), bd=5, textvariable=mobileval)
    mobentryentry.place(x=230, y=310)

    emailval = StringVar()
    emailentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=230, y=370)

    addressval = StringVar()
    addressentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=230, y=430)

    cateval = StringVar()
    catentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                     bd=5, textvariable=cateval)  # modifyed
    catentry.place(x=230, y=490)

    dobval = StringVar()
    dobentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                     bd=5, textvariable=dobval)  # modifyed
    dobentry.place(x=230, y=550)

    sessionval = StringVar()
    sessionentry = Entry(addroot, font=("Open Sans", 17, 'bold'),
                         bd=5, textvariable=sessionval)  # modifyed
    sessionentry.place(x=230, y=610)

    ################################___REMOVE IT___##########################################################
    # reg = regval.set(171041310)
    # name = nameval.set('Shubham Kumar')
    # father = fatherval.set("Prof. Sanjiv Kumar Bhagat")
    # branch = branchval.set('ECE')
    # gender = genderval.set('Male')
    # mobile = mobileval.set('7319944888')
    # email = emailval.set('Er.shubhamBhagat@gmail.com')
    # add = addressval.set('Bihar')
    # cate = cateval.set("EBC")
    # dob = dobval.set('03/06/2000')
    # session = sessionval.set('2017 - 2021')
    #######&&&&&&&&&&&&&&&&&&&&&&___Submit___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&########

    submitbtn = Button(addroot, text='Submit', font=('roman', 15, "bold"), width=20, bg="red",
                       bd=6, activebackground='gold2', activeforeground='red', command=submitadd)
    submitbtn.place(x=150, y=655)

    ############################___submit  botton(Add)___#################################

    # print(reg, nameval, branchval, gender, mobile, email, add, times, date)

    addroot.mainloop()


################################___Add student upper layoyt__################################################
addbtn = Button(DataEntryFrame, text=" Add Student ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE,
                bg='skyblue', bd=5,
                activebackground='green', activeforeground='blue', command=addstudent)
addbtn.pack(side=TOP, expand=True)


####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&____Search Student___&&&&&&&&&&&&&&&&&&&&######################
def searchstudent():
    def submitsearch():  # submit Button CMD
        print("search")
        reg = regval.get()
        name = nameval.get()
        father_n = fatherval.get()
        branch = branchval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        add = addressval.get()
        cate = catval.get()
        dob = dobval.get()
        session = sessionval.get()

        if (reg != ''):
            crt = 'select *from pcesms where registration=%s'
            mycursor.execute(crt, (reg))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (name != ''):
            crt = 'select *from pcesms where name=%s'
            mycursor.execute(crt, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (father_n != ''):
            crt = 'select *from pcesms where father_name=%s'
            mycursor.execute(crt, (father_n))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (branch != ''):
            crt = 'select *from pcesms where branch=%s'
            mycursor.execute(crt, (branch))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (gender != ''):
            crt = 'select *from pcesms where gender=%s'
            mycursor.execute(crt, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (mobile != ''):
            crt = 'select *from pcesms where mobile=%s'
            mycursor.execute(crt, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (email != ''):
            crt = 'select *from pcesms where email=%s'
            mycursor.execute(crt, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (add != ''):
            crt = 'select *from pcesms where address=%s'
            mycursor.execute(crt, (add))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)

        elif (cate != ''):
            crt = 'select *from pcesms where Category=%s'
            mycursor.execute(crt, (cate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)

        elif (dob != ''):
            crt = 'select *from pcesms where dob=%s'
            mycursor.execute(crt, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        elif (session != ''):
            crt = 'select *from pcesms where session=%s'
            mycursor.execute(crt, (session))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=aa)
        print("work search")           #Remove

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('450x620+70+100')
    searchroot.title('Serch Student')
    searchroot.config(bg='brown')
    # searchroot.iconbitmap('Pce_purnea.ico')
    searchroot.resizable(False, False)
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, "bold"), width=20, bg="red", bd=6,
                       activebackground='green', activeforeground='blue', command=submitsearch)
    submitbtn.place(x=150, y=560)
    ############################___search student level___#############################

    regleble = Label(searchroot, text='registration No:- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                     width=12,
                     borderwidth=3, anchor='w')
    regleble.place(x=10, y=10)

    nameleble = Label(searchroot, text=' Name :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                      width=12,
                      borderwidth=3, anchor='w')
    nameleble.place(x=10, y=57)

    fatherleble = Label(searchroot, text=' Father Name :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    fatherleble.place(x=10, y=107)

    branchleble = Label(searchroot, text=' Branch :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    branchleble.place(x=10, y=157)

    genderleble = Label(searchroot, text=' Gender :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12,
                        borderwidth=3, anchor='w')
    genderleble.place(x=10, y=207)

    mobilleble = Label(searchroot, text=' Mobile No :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    mobilleble.place(x=10, y=257)

    emailleble = Label(searchroot, text=' Email Id :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12,
                       borderwidth=3, anchor='w')
    emailleble.place(x=10, y=307)

    addressleble = Label(searchroot, text=' Address :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                         width=12,
                         borderwidth=3, anchor='w')
    addressleble.place(x=10, y=357)

    dobleble = Label(searchroot, text=' D.O.B :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                     width=12,
                     borderwidth=3, anchor='w')
    dobleble.place(x=10, y=407)

    catleble = Label(searchroot, text=' Category :- ', bg='light green', font=('time', 20, 'bold'), relief=RIDGE,
                     width=11,
                     borderwidth=3, anchor="w")
    catleble.place(x=10, y=457)

    seasionleble = Label(searchroot, text=' Session :- ', bg='light green', font=('time', 20, 'bold'), relief=RIDGE,
                         width=11,
                         borderwidth=3, anchor="w")
    seasionleble.place(x=10, y=507)

    #####################################___Search Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(searchroot, font=("Roman",15, 'bold'),
                     bd=5,width=19, textvariable=regval)
    regentry.place(x=230, y=10)

    nameval = StringVar()
    nameentry = Entry(searchroot, font=("Roman", 15, 'bold'),
                      bd=5,width=19, textvariable=nameval)
    nameentry.place(x=230, y=60)

    fatherval = StringVar()
    fatherentry = Entry(searchroot, font=("Roman", 15, 'bold'),
                        bd=5,width=19, textvariable=fatherval)  # modify
    fatherentry.place(x=230, y=110)

    branchval = StringVar()
    branchentry = Entry(searchroot,font=("Roman", 15, 'bold'),
                        bd=5,width=19, textvariable=branchval)
    branchentry.place(x=230, y=160)

    genderval = StringVar()
    genderentry = Entry(searchroot, font=("Roman", 15, 'bold'),
                        bd=5,width=19, textvariable=genderval)
    genderentry.place(x=230, y=210)

    mobileval = StringVar()
    mobentryentry = Entry(searchroot, font=("Roman", 15, 'bold'),
                          bd=5, width=19,textvariable=mobileval)
    mobentryentry.place(x=230, y=260)

    emailval = StringVar()
    emailentry = Entry(searchroot,font=("Roman", 15, 'bold'),
                       bd=5,width=19, textvariable=emailval)
    emailentry.place(x=230, y=310)

    addressval = StringVar()
    addressentry = Entry(searchroot, font=("Roman", 15, 'bold'),
                         bd=5,width=19, textvariable=addressval)
    addressentry.place(x=230, y=360)

    catval = StringVar()
    categorylebel = Entry(searchroot,font=("Roman", 15, 'bold'),
                          bd=5,width=19, textvariable=catval)
    categorylebel.place(x=230, y=410)

    dobval = StringVar()
    dobentry = Entry(searchroot,font=("Roman", 15, 'bold'),
                     bd=5,width=19, textvariable=dobval)
    dobentry.place(x=230, y=460)

    sessionval = StringVar()
    sessionentry = Entry(searchroot,font=("Roman", 15, 'bold'),
                         bd=5,width=19, textvariable=sessionval)
    sessionentry.place(x=230, y=510)

    #############################___Add (submit  button)___#################################

    searchroot.mainloop()


searchbtn = Button(DataEntryFrame, text=" Search Student ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='green', activeforeground='blue', command=searchstudent)
searchbtn.pack(side=TOP, expand=True)


########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Delete___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###################

def deletestudent():
    print("3.Delete Student")
    store = studenttable.focus()
    content = studenttable.item(store)
    pp = content['values'][0]
    crt = 'delete from pcesms where registration=%s'
    mycursor.execute(crt, (pp))
    con.commit()
    messagebox.showinfo('Notification', ' Deleted successfully...')
    crt = 'select *from pcesms'
    mycursor.execute(crt)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
        studenttable.insert('', END, values=aa)


deletebtn = Button(DataEntryFrame, text=" Delete Student ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='green', activeforeground='blue', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)


#########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Update___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&########################
def updatestudent():
    print("4.Update Student Click")  ###___remove___#######

    def submitupdate():  # submit Button CMD

        registration = regval.get()
        name = nameval.get()
        father_name = fatherval.get()
        branch = branchval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        cate = cateval.get()
        dob = dobval.get()
        session = sessionval.get()

        print('update submit button  Click')  ###___remove___#######
        crt = 'UPDATE pcesms SET name=%s,father_name=%s,branch=%s,gender=%s,mobile=%s,email=%s,address=%s,Category=%s,dob=%s,session=%s WHERE registration=%s'
        mycursor.execute(crt,
                         (name, father_name, branch, gender, mobile, email, address, cate, dob, session, registration))
        con.commit()
        messagebox.showinfo('Notifcation', 'registration:-{} Modifired Sucessfully...'.format(registration),
                            parent=updateroot)

        ##############_____this line for up2date__________#####################################
        crt = 'select *from pcesms'
        mycursor.execute(crt)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
            studenttable.insert('', END, values=aa)

        print("4.Update Student Click")  ###___remove___#######

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('508x650+70+100')
    updateroot.title('Update Student')
    updateroot.config(bg='#80461B')
    # updateroot.iconbitmap('Pce_purnea.ico')
    updateroot.resizable(False, False)
    ############################___UPDATE_student level___#############################

    regleble = Label(updateroot, text=' registration No :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                     width=12, borderwidth=3, anchor='w', bd=5)
    regleble.place(x=10, y=10)

    nameleble = Label(updateroot, text=' Name :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                      width=12, borderwidth=3, anchor='w', bd=5)
    nameleble.place(x=10, y=61)

    nameleble = Label(updateroot, text=' Father Name :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                      width=12, borderwidth=3, anchor='w', bd=5)
    nameleble.place(x=10, y=113)  # modify

    branchleble = Label(updateroot, text=' Branch :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12, borderwidth=3, anchor='w', bd=5)
    branchleble.place(x=10, y=165)

    genderleble = Label(updateroot, text=' Gender:- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                        width=12, borderwidth=3, anchor='w', bd=5)
    genderleble.place(x=10, y=218)

    mobilleble = Label(updateroot, text='Mobile No   :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12, borderwidth=3, anchor='w', bd=5)
    mobilleble.place(x=10, y=272)

    emailleble = Label(updateroot, text='Email Id  :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                       width=12, borderwidth=3, anchor='w', bd=5)
    emailleble.place(x=10, y=326)

    addressleble = Label(updateroot, text=' Address :- ', bg='light green', font=('times', 20, 'bold'), relief=RIDGE,
                         width=12, borderwidth=3, anchor='w', bd=5)
    addressleble.place(x=10, y=379)

    catleble = Label(updateroot, text=' Category :- ', bg='light green', font=('time', 20, 'bold'), relief=RIDGE,
                     width=11, borderwidth=3, anchor="w", bd=5)
    catleble.place(x=10, y=432)

    dobleble = Label(updateroot, text=' D.O.B:- ', bg='light green', font=('time', 20, 'bold'), relief=RIDGE,
                     width=11, borderwidth=3, anchor="w", bd=5)
    dobleble.place(x=10, y=487)

    sessionleble = Label(updateroot, text=' Session :-', bg='light green', font=('time', 20, 'bold'), relief=RIDGE,
                         width=11, borderwidth=3, anchor="w", bd=5)
    sessionleble.place(x=10, y=541)

    #####################################___update Student Entry box___##############################################
    regval = StringVar()
    regentry = Entry(updateroot, font=("Open Sans", 17, 'bold'), bd=5,width=19
                     , textvariable=regval)
    regentry.place(x=230, y=10)

    nameval = StringVar()
    nameentry = Entry(updateroot, font=("Open Sans", 17, 'bold'), bd=5,width=19, textvariable=nameval)
    nameentry.place(x=230, y=61)

    fatherval = StringVar()
    fatherentry = Entry(updateroot, font=("Open Sans", 17, 'bold'), bd=5,width=19, textvariable=fatherval)
    fatherentry.place(x=230, y=113)

    branchval = StringVar()
    branchentry = Entry(updateroot, font=(
        "Open Sans", 17, 'bold'), bd=5,width=19, textvariable=branchval)
    branchentry.place(x=230, y=165)

    genderval = StringVar()
    genderentry = Entry(updateroot, font=(
        "Open Sans", 17, 'bold'), bd=5,width=19, textvariable=genderval)
    genderentry.place(x=230, y=219)

    mobileval = StringVar()
    mobentryentry = Entry(updateroot, font=(
        "Open Sans", 17, 'bold'), bd=5,width=19, textvariable=mobileval)
    mobentryentry.place(x=230, y=273)

    emailval = StringVar()
    emailentry = Entry(updateroot, font=(
        "Open Sans", 17, 'bold'), bd=5,width=19, textvariable=emailval)
    emailentry.place(x=230, y=327)

    addressval = StringVar()
    addressentry = Entry(updateroot, font=(
        "Open Sans", 17, 'bold'), bd=5,width=19, textvariable=addressval)
    addressentry.place(x=230, y=380)

    cateval = StringVar()
    catentry = Entry(updateroot, font=("Open Sans", 17, 'bold'),
                     bd=5,width=19, textvariable=cateval)
    catentry.place(x=230, y=433)

    dobval = StringVar()
    dobentry = Entry(updateroot, font=("Open Sans", 17, 'bold'),
                     bd=5,width=19, textvariable=dobval)
    dobentry.place(x=230, y=488)

    sessionval = StringVar()
    sessionentry = Entry(updateroot, font=("Open Sans", 17, 'bold'),
                         bd=5,width=19, textvariable=sessionval)
    sessionentry.place(x=230, y=542)

    #############################___update focus )___#################################

    submitbtn = Button(updateroot, text='Submit', font=('Ubuntu Mono', 15, "bold"), width=20, bg="red", bd=6,
                       activebackground='green', activeforeground='blue', command=submitupdate)
    submitbtn.place(x=150, y=595)
    aa = studenttable.focus()  # for focus text where i want to copy in clipboard
    content = studenttable.item(aa)
    pp = content['values']
    if (len(pp) != 0):
        regval.set(pp[0])
        nameval.set(pp[1])
        fatherval.set(pp[2])
        branchval.set(pp[3])
        genderval.set(pp[4])
        mobileval.set(pp[5])
        emailval.set(pp[6])
        addressval.set(pp[7])
        dobval.set(pp[9])
        cateval.set(pp[8])
        sessionval.set(pp[10])
    updateroot.mainloop()

updatebtn = Button(DataEntryFrame, text=" Update Student ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='green', activeforeground='blue', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

############&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Show All___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##############################
def Showallstudent():
    print("5. Show all")
    crt = 'select *from pcesms'
    mycursor.execute(crt)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        aa = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
        studenttable.insert('', END, values=aa)
showbtn = Button(DataEntryFrame, text=" Show all ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE, bg='skyblue',
                 bd=5,
                 activebackground='green', activeforeground='blue', command=Showallstudent)
showbtn.pack(side=TOP, expand=True)

#######&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Export Student___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#############
def Exportstudent():
    sh = filedialog.asksaveasfilename()
    print("click on Export Data")
    ub = studenttable.get_children()
    registration, name, father_name, branch, gender, mobile, email, address, Category, dob, session = [], [], [], [], [], [], [], [], [], [], []
    for i in ub:
        content = studenttable.item(i)
        pp = content['values']
        registration.append(pp[0]), name.append(pp[1]), father_name.append(pp[2]), branch.append(pp[3]), gender.append(
            pp[4]), \
        mobile.append(pp[5]), email.append(pp[6]), address.append(pp[7]), Category.append(pp[8]), dob.append(
            pp[9]), session.append(pp[10])
    dd = ['Registration', 'Name', 'father Name', 'Branch', 'Gender',
          'Mobile No', 'Email Id', 'Address', 'Category', 'D.O.B', 'session']
    df = pandas.DataFrame(list(zip(registration, name, father_name, branch,
                                   gender, mobile, email, address, Category, dob, session)), columns=dd)
    path = r'{}.csv'.format(sh)
    df.to_csv(path, index=False)
    messagebox.showinfo('Notification', 'Student data is save{}'.format(path))
exportbtn = Button(DataEntryFrame, text=" Export Data ", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE,
                   bg='skyblue', bd=5,
                   activebackground='green', activeforeground='blue', command=Exportstudent)
exportbtn.pack(side=TOP, expand=True)


#######&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&___Exit___&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####################
def Exitstudent():
    print("you click Exit")
    exitbox = messagebox.askyesno("Notification", "Do you want to Exit")
    print(exitbox)
    if (exitbox == True):
        root.destroy()

exitbtn = Button(DataEntryFrame, text="Exit", width=25, font=('Ubuntu Mono', 20, 'bold'), relief=RIDGE, bg='skyblue',
                 bd=5,
                 activebackground='red', activeforeground='white', command=Exitstudent)
exitbtn.pack(side=TOP, expand=True)

###########################___Slider Word_Design___###################
ss = 'Welcome To PCE_PURNEA '
count = 0
text = ''
SliderLabel = Label(root, text=ss, bg='#031d2e', relief=RIDGE, font=('roman', 30, ' bold'), width=35,
                    borderwidth=5)
SliderLabel.place(x=400, y=3)
IntroLabelTick()
IntroLabelColorTick()

##########################___clock___###################################################

clock = Label(root, bg='wheat1', relief=RIDGE, font=('red', 15, 'italic bold'), activebackground='red', width=15,
              borderwidth=5, highlightcolor="green")
clock.place(x=1, y=1)
tick()

#########################___Created DataBase Botton___###########################################

connectbutton = Button(root, text="Connect Data Base", width=15, font=('red', 15, 'bold'),
                       borderwidth=4, bd=7, foreground="black", bg='sky blue', activebackground='green',
                       activeforeground='white', command=connectdb)
connectbutton.place(x=1325, y=4)
def help():
    help_s = Toplevel()
    # help_s.grab_set()
    help_s.geometry('540x250+500+200')
    help_s.resizable(False, False)
    help_s.config(bg='Black')
    label = Label(help_s, text="I am Shubham Kumar (ECE {2017}) and Reg No:-17104131027\n"
                               "if you facing any problems in Softwere you contacts on \t"   " \n whatapp(7319944888) or \n Email:- Er.shubhambhagat@gmail.com\n"
                               " \n\t\nMost Welcome For your Feedback""\n\n\n Thank You !!!",
                  font=('times', 15, 'bold'),
                  fg="white",
                  bg="black")
    label.pack()
colorss = ['gray', 'light grey', 'sky blue']
def helps():
    bg = random.choice(colorss)
    helpbox.config(bg=bg)
    helpbox.after(501, helps)
helpbox = Button(root, text="Info", width=5, font=('white', 10, 'italic bold'),
                 borderwidth=8, bd=6, bg='gray', activebackground='black',
                 activeforeground='red', command=help)
helpbox.place(x=1465, y=795)
helps()
root.mainloop()