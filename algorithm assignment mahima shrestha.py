from tkinter import *
from tkinter import ttk
import tkinter.ttk
import tkinter.messagebox
import numbers
import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',user='root',passwd='Fire1234//',database="softwarica")

    mycursor=con.cursor()

except mysql.connector.DatabaseError as e:
    print(e)


window=Tk() #creating main window
window.configure(background='thistle2')
window.geometry('600x600')
window.title('Student information system')
window.resizable(0,0)
class frame7():
    def __init__(self,window):
        self.window=window
        self.frame1=Frame(window,bd=4,relief=RIDGE,bg='thistle2')
        self.frame1.place(x=100,y=50,width=410,height=50)

        self.sortcombo = ttk.Combobox(window, font=15, width=9) #sortcombo is defined here for unit testing
        self.sortcombo['values'] = (" First Name", "Last Name", "Contact", "Course", "Student Id")
        self.sortcombo.set(' First Name')

        self.searchbox = ttk.Combobox(window, font=('Times', 12))#searchbox defined for unit tetsting
        self.searchbox['values'] = ("First name", "Last name", 'Contact',
                                    "Course", "Student Id")
        self.searchbox.set('First name')

        self.student_table = ttk.Treeview(window,
                                          columns=('First_name', 'Last_name', 'Contact', 'Course', 'student_id'))
        self.textentry = Entry(window, font=14, width=15, bd=2)

        self.label=Label(self.frame1,text="Welcome to Student Information System",font=('Arial',16),bg="thistle2")
        self.label.place(x=11,y=10)

        self.photo = PhotoImage(file="photo3.gif") #adding photo on main window
        self.photolabel = Label(window, image=self.photo)
        self.photolabel.photo = self.photo
        self.photolabel.place(x=150, y=130, width=300, height=200)

        self.frame2=Frame(window,relief=RIDGE,bg="Thistle2") # creating frame for buttons
        self.frame2.place(x=70,y=350,width=500,height=100)

        self.button=Button(self.frame2,text="Search data",font=('Times',16),bg="linen",command=self.search)
        self.button.place(x=10,y=10,width=100)

        self.button1=Button(self.frame2,text="INSERT",font=('Times',16),bg="linen",command=self.insert_info)
        self.button1.place(x=130,y=10,width=100)

        self.button2 = Button(self.frame2, text="UPDATE", font=('Times', 16), bg="linen",command=self.update_win)
        self.button2.place(x=240, y=10, width=100)

        self.button3 = Button(self.frame2, text="DELETE", font=('Times', 16), bg="linen",command=self.delete)
        self.button3.place(x=350, y=10, width=100)

    def insert_info(self):
        newwin=Toplevel() #toplevel window for insert
        newwin.title('Insert Data')
        newwin.geometry('1200x1000')
        newwin.resizable(0,0)
        newwin.configure(bg="thistle")


        self.newwin=newwin
        window.withdraw()

        self.newframe=Frame(newwin,bd=4,relief=RIDGE,bg="thistle2")
        self.newframe.place(x=480,y=25,width=250,height=60)

        self.label1=Label(self.newframe,text="Insert the required data",bg="thistle2",font=("Times",16))
        self.label1.place(x=10,y=10)

        self.newframe1 = Frame(newwin, bd=4, relief=RIDGE, bg='alice blue')
        self.newframe1.place(x=20, y=100, width=650, height=600)

        scrollbarx = Scrollbar(self.newframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.newframe1, orient=VERTICAL)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.newframe1,
                                          columns=('First_name', 'Last_name', 'Contact', 'Course', 'student_id'),
                                          xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

        self.student_table.heading('First_name', text='First Name')
        self.student_table.heading('Last_name', text='Last Name')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('student_id', text='student id')
        self.student_table['show'] = 'headings'

        self.student_table.column('First_name', width=160)
        self.student_table.column('Last_name', width=160)
        self.student_table.column('Contact', width=160)
        self.student_table.column('Course', width=160)
        self.student_table.column('student_id', width=160)

        scrollbarx.config(command=self.student_table.xview)
        scrollbary.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind('<ButtonRelease-1>',self.pointer)

        self.newframe3 = Frame(newwin, bg='thistle', bd=4, relief=RIDGE)
        self.newframe3.place(x=700, y=100, width=400, height=400)

        self.label2=Label(self.newframe3,text="Personal information",font=("Times",14),bg="thistle")
        self.label2.place(x=10,y=5)

        label1 = Label(self.newframe3, text='First_name:', bg='thistle', font=('Times', 14))
        label1.place(x=10, y=35)

        self.entry_fn = Entry(self.newframe3, width=15, font=14, bg='azure', bd=3)
        self.entry_fn.place(x=120, y=35)

        last_name = Label(self.newframe3, text="Last_name:", bg='thistle', font=('Times', 14))
        last_name.place(x=10, y=70)

        self.entry_ln = Entry(self.newframe3, width=15, font=14, bg='azure', bd=3)
        self.entry_ln.place(x=120, y=70)

        contact = Label(self.newframe3, text="Contact:", bg='thistle', font=('Times', 14))
        contact.place(x=10, y=110)

        self.entry_ad = Entry(self.newframe3, width=15, font=14, bg='azure', bd=3)
        self.entry_ad.place(x=120, y=110)

        degree = Label(self.newframe3, text='Course:', bg='thistle', font=('Times', 14))
        degree.place(x=10, y=150)
        self.combo1 = ttk.Combobox(self.newframe3, font=15, width=14)
        self.combo1['values'] = ("Bsc.Computing", "Bsc.Ethical Hacking", "Bsc.Multimedia")
        self.combo1.place(x=120, y=150)

        student_id = Label(self.newframe3, text='student id:', bg='thistle', font=('Times', 14))
        student_id.place(x=10, y=190)

        self.entry_st = Entry(self.newframe3, width=15, font=14, bg='azure', bd=3)
        self.entry_st.place(x=120, y=190)

        self.clear = Button(self.newframe3, text="CLEAR", font=('Times', 14), bg='linen',command=self.clear_info)
        self.clear.place(x=200, y=240)

        self.insert = Button(self.newframe3, text='INSERT', font=('Times', 14), bg='linen',command=self.insert_info2)
        self.insert.place(x=80, y=240)

        self.sortby = Label(self.newframe3, text="Sort by:", font=('Times', 16), bg="thistle")
        self.sortby.place(x=20, y=300)

        self.sortcombo = ttk.Combobox(self.newframe3, font=15, width=9)
        self.sortcombo['values'] = (" First Name", "Last Name", "Contact", "Course", "Student Id")
        self.sortcombo.set(' First Name')
        self.sortcombo.place(x=100, y=300)

        self.sortbutton = Button(self.newframe3, text="SORT", font=("Times", 12), bg="linen",command=self.sort_info)
        self.sortbutton.place(x=230, y=300)

        self.backbutt=Button(newwin,text='Back',font=("Times",13),bg="linen",command=self.on_back)
        self.backbutt.place(x=30,y=40)
        self.select()
        newwin.mainloop()
    def on_back(self):
        window.deiconify()
        self.newwin.withdraw()

    def insert_info2(self):
        First_name = self.entry_fn.get()
        Last_name = self.entry_ln.get()
        Contact = self.entry_ad.get()
        student_id = self.entry_st.get()
        Degree = self.combo1.get()

        if not First_name:#error handling
            tkinter.messagebox.showinfo('Info', 'Fill the  entry')
            return

        if not First_name.isalpha():#if the name is not alphabet it shows an error
            tkinter.messagebox.showinfo('Info', 'You cannot enter integer and symbols in First Name')
            return
        if not Last_name:# shows error when entry is not filled
            tkinter.messagebox.showinfo('Info', 'Fill Last name entry')
            return
        if not Last_name.isalpha():#shows error when value is not alphabet
            tkinter.messagebox.showinfo('Info', 'You cannot enter integer and symbols in Last Name')
            return
        if not Contact:#shows error when entry is not filled
            tkinter.messagebox.showinfo('Info', 'Fill Contact entry')
            return
        if not student_id:#shows error when entry is not filled
            tkinter.messagebox.showinfo('Info', 'Fill student id entry')
            return
        if not Contact.isdigit():#shows error when contact is not number
            tkinter.messagebox.showinfo('Info', 'You cannot enter string and symbols in Contact')
            return

        # if len(str(Contact)) != 10:
        #     tkinter.messagebox.showinfo('Info', 'Your contact should be 10 digits')
        #     return
        if not student_id.isdigit():#shows error when student id is not number
            tkinter.messagebox.showinfo('Info', 'You cannot enter string and symbols in student id')
            return

        if not Degree:#shows error when entry is not filled
            tkinter.messagebox.showinfo('Info', 'Fill the degree entry')
            return

        query = 'insert into tkintertbl1 values(%s,%s,%s,%s,%s)'
        values = (First_name, Last_name, Contact, Degree, student_id)

        mycursor.execute(query, values)
        tkinter.messagebox.showinfo('Data inserted', 'Your data has been inserted succesfully')
        con.commit()

        self.select()
        self.clear_info()


    def select(self):
        query = "select * from tkintertbl1"
        mycursor.execute(query)
        results = mycursor.fetchall()
        if len(results) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for result in results:
            self.student_table.insert('', END, values=result)
            con.commit()

    def clear_info(self):
        self.entry_fn.delete(0, END)
        self.entry_ln.delete(0, END)
        self.entry_st.delete(0, END)
        self.entry_ad.delete(0, END)
        self.combo1.delete(0, END)

    def pointer(self,event):
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            self.clear_info()
            self.entry_fn.insert(0, row[0])
            self.entry_ln.insert(0, row[1])
            self.entry_ad.insert(0, row[2])
            self.combo1.insert(0, row[3])
            self.entry_st.insert(0, row[4])
        except IndexError:
            pass

    def partition(self, data, low, high):#algorithm for sorting
        sort_combo = self.sortcombo.get()
        if sort_combo == " First Name":
            column_index = 0
        elif sort_combo == "Last Name":
            column_index = 1
        elif sort_combo == "Contact":
            column_index = 2
        elif sort_combo == "Course":
            column_index = 3
        elif sort_combo == "Student Id":
            column_index = 4
        else:
            column_index = 5
        i = (low - 1)
        pivot = data[high][column_index]
        for j in range(low, high):
            if data[j][column_index] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return (i + 1)

    def quick_sort(self, data, low, high):
        if low < high:
            pi = self.partition(data, low, high)
            self.quick_sort(data, low, pi - 1)

            self.quick_sort(data, pi + 1, high)

    def sort_info(self):
        a = 'SELECT * FROM tkintertbl1'
        mycursor.execute(a)
        list_rows = mycursor.fetchall()
        self.quick_sort(list_rows, 0, len(list_rows) - 1)
        self.student_table.delete(*self.student_table.get_children())
        for m in list_rows:
            self.student_table.insert('', 'end', values=m)
            con.commit()

    def update_win(self):#update window
        newwin1=Toplevel()
        newwin1.title('Update Data')
        newwin1.geometry('1200x1000')
        newwin1.resizable(0, 0)
        newwin1.configure(bg="thistle")

        self.newwin1=newwin1
        window.withdraw()

        self.newwinfr = Frame(newwin1, bd=4, relief=RIDGE, bg="thistle2")
        self.newwinfr.place(x=480, y=25, width=250, height=60)

        self.label1 = Label(self.newwinfr, text="Update the required data", bg="thistle2", font=("Times", 16))
        self.label1.place(x=10, y=10)

        self.newwinfr1 = Frame(newwin1, bd=4, relief=RIDGE, bg='alice blue')
        self.newwinfr1.place(x=20, y=100, width=650, height=600)

        scrollbarx = Scrollbar(self.newwinfr1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.newwinfr1, orient=VERTICAL)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.newwinfr1,
                                          columns=('First_name', 'Last_name', 'Contact', 'Course', 'student_id'),
                                          xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

        self.student_table.heading('First_name', text='First Name')
        self.student_table.heading('Last_name', text='Last Name')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('student_id', text='student id')
        self.student_table['show'] = 'headings'

        self.student_table.column('First_name', width=160)
        self.student_table.column('Last_name', width=160)
        self.student_table.column('Contact', width=160)
        self.student_table.column('Course', width=160)
        self.student_table.column('student_id', width=160)

        scrollbarx.config(command=self.student_table.xview)
        scrollbary.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.newwinfr2 = Frame(newwin1, bg='thistle', bd=4, relief=RIDGE)
        self.newwinfr2.place(x=700, y=100, width=400, height=400)

        self.label2 = Label(self.newwinfr2, text="Personal information", font=("Times", 14), bg="thistle")
        self.label2.place(x=10, y=5)

        label1 = Label(self.newwinfr2, text='First_name:', bg='thistle', font=('Times', 14))
        label1.place(x=10, y=35)

        self.entry_fn = Entry(self.newwinfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_fn.place(x=120, y=35)

        last_name = Label(self.newwinfr2, text="Last_name:", bg='thistle', font=('Times', 14))
        last_name.place(x=10, y=70)

        self.entry_ln = Entry(self.newwinfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_ln.place(x=120, y=70)

        contact = Label(self.newwinfr2, text="Contact:", bg='thistle', font=('Times', 14))
        contact.place(x=10, y=110)

        self.entry_ad = Entry(self.newwinfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_ad.place(x=120, y=110)

        degree = Label(self.newwinfr2, text='Course:', bg='thistle', font=('Times', 14))
        degree.place(x=10, y=150)
        self.combo1 = ttk.Combobox(self.newwinfr2, font=15, width=14)
        self.combo1['values'] = ("Bsc.Computing", "Bsc.Ethical Hacking", "Bsc.Multimedia")
        self.combo1.place(x=120, y=150)

        student_id = Label(self.newwinfr2, text='student id:', bg='thistle', font=('Times', 14))
        student_id.place(x=10, y=190)

        self.entry_st = Entry(self.newwinfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_st.place(x=120, y=190)

        self.clear = Button(self.newwinfr2, text="CLEAR", font=('Times', 14), bg='linen', command=self.clear_info)
        self.clear.place(x=200, y=240)

        self.update = Button(self.newwinfr2, text='UPDATE', font=('Times', 14), bg='linen', command=self.update1)
        self.update.place(x=80, y=240)

        self.sortby = Label(self.newwinfr2, text="Sort by:", font=('Times', 16), bg="thistle")
        self.sortby.place(x=20, y=300)

        self.sortcombo = ttk.Combobox(self.newwinfr2, font=15, width=9
                                      )
        self.sortcombo['values'] = (" First Name", "Last Name", "Contact", "Course", "Student Id")
        self.sortcombo.set(' First Name')
        self.sortcombo.place(x=100, y=300)

        self.sortbutton = Button(self.newwinfr2, text="SORT", font=("Times", 12), bg="linen", command=self.sort_info)
        self.sortbutton.place(x=230, y=300)
        self.backbutt = Button(newwin1, text='Back', font=("Times", 13), bg="linen", command=self.back_ut)
        self.backbutt.place(x=30, y=40)

        self.select()
        self.select()
    def back_ut(self):
        window.deiconify()
        self.newwin1.withdraw()

    def update1(self):
        try:
            query = 'UPDATE tkintertbl1 SET First_name=%s,Last_name=%s,Contact=%s,degree=%s WHERE student_id=%s'
            First_name = self.entry_fn.get()
            Last_name = self.entry_ln.get()
            Contact = self.entry_ad.get()
            Degree = self.combo1.get()
            student_id = self.entry_st.get()

            if not First_name:
                tkinter.messagebox.showinfo('Info', 'Select the data to be updated')
                return

            if not First_name.isalpha():
                tkinter.messagebox.showinfo('Info', 'You cannot enter integer and symbols in First Name')
                return
            if not Last_name:
                tkinter.messagebox.showinfo('Info', 'Fill Last name entry')
                return
            if not Last_name.isalpha():
                tkinter.messagebox.showinfo('Info', 'You cannot enter integer and symbols in Last Name')
                return
            if not Contact:
                tkinter.messagebox.showinfo('Info', 'Fill Contact entry')
                return
            if not student_id:
                tkinter.messagebox.showinfo('Info', 'Fill student id entry')
                return
            if not Contact.isdigit():
                tkinter.messagebox.showinfo('Info', 'You cannot enter string and symbols in Contact')
                return

            # if len(str(Contact)) != 10:
            #     tkinter.messagebox.showinfo('Info', 'Your contact should be 10 digits')
            #     return
            if not student_id.isdigit():
                tkinter.messagebox.showinfo('Info', 'You cannot enter string and symbols in student id')
                return

            if not Degree:
                tkinter.messagebox.showinfo('Info', 'Fill the degree entry')
                return

            values = (First_name, Last_name, int(Contact), Degree, int(student_id))

            mycursor.execute(query, values)
            con.commit()

            tkinter.messagebox.showinfo('Success', 'Data updated successfully')
            self.clear_info()
            self.select()
        except ValueError:
            tkinter.messagebox.showerror('Error','Select the data to be updated')

    def delete(self):#delete window
        newwin2 = Toplevel()
        newwin2.title('Delete Data')
        newwin2.geometry('1200x1000')
        newwin2.resizable(0, 0)
        newwin2.configure(bg="thistle")

        self.newwin2=newwin2
        window.withdraw()

        self.delfr = Frame(newwin2, bd=4, relief=RIDGE, bg="thistle2")
        self.delfr.place(x=480, y=25, width=250, height=60)

        self.label1 = Label(self.delfr, text="Delete the required data", bg="thistle2", font=("Times", 16))
        self.label1.place(x=10, y=10)

        self.delfr1 = Frame(newwin2, bd=4, relief=RIDGE, bg='alice blue')
        self.delfr1.place(x=20, y=100, width=650, height=600)

        scrollbarx = Scrollbar(self.delfr1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.delfr1, orient=VERTICAL)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.delfr1,
                                          columns=('First_name', 'Last_name', 'Contact', 'Course', 'student_id'),
                                          xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

        self.student_table.heading('First_name', text='First Name')
        self.student_table.heading('Last_name', text='Last Name')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('student_id', text='student id')
        self.student_table['show'] = 'headings'

        self.student_table.column('First_name', width=160)
        self.student_table.column('Last_name', width=160)
        self.student_table.column('Contact', width=160)
        self.student_table.column('Course', width=160)
        self.student_table.column('student_id', width=160)

        scrollbarx.config(command=self.student_table.xview)
        scrollbary.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.phtot1=PhotoImage(file="del1.gif")
        self.labelpho=Label(newwin2,image=self.phtot1)
        self.labelpho.place(x=800,y=100,width=240,height=150)
        self.delfr2 = Frame(newwin2, bg='thistle', bd=4, relief=RIDGE)
        self.delfr2.place(x=750, y=270, width=400, height=400)

        self.label2 = Label(self.delfr2, text="Personal information", font=("Times", 14), bg="thistle")
        self.label2.place(x=10, y=5)

        label1 = Label(self.delfr2, text='First_name:', bg='thistle', font=('Times', 14))
        label1.place(x=10, y=35)

        self.entry_fn = Entry(self.delfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_fn.place(x=120, y=35)

        last_name = Label(self.delfr2, text="Last_name:", bg='thistle', font=('Times', 14))
        last_name.place(x=10, y=70)

        self.entry_ln = Entry(self.delfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_ln.place(x=120, y=70)

        contact = Label(self.delfr2, text="Contact:", bg='thistle', font=('Times', 14))
        contact.place(x=10, y=110)

        self.entry_ad = Entry(self.delfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_ad.place(x=120, y=110)

        degree = Label(self.delfr2, text='Course:', bg='thistle', font=('Times', 14))
        degree.place(x=10, y=150)
        self.combo1 = ttk.Combobox(self.delfr2
                                   , font=15, width=14)
        self.combo1['values'] = ("Bsc.Computing", "Bsc.Ethical Hacking", "Bsc.Multimedia")
        self.combo1.place(x=120, y=150)

        student_id = Label(self.delfr2, text='student id:', bg='thistle', font=('Times', 14))
        student_id.place(x=10, y=190)

        self.entry_st = Entry(self.delfr2, width=15, font=14, bg='azure', bd=3)
        self.entry_st.place(x=120, y=190)

        self.clear = Button(self.delfr2, text="CLEAR", font=('Times', 14), bg='linen', command=self.clear_info)
        self.clear.place(x=200, y=240)

        self.update = Button(self.delfr2, text='DELETE', font=('Times', 14), bg='linen', command=self.delete_data)
        self.update.place(x=80, y=240)
        self.sortby = Label(self.delfr2, text="Sort by:", font=('Times', 16), bg="thistle")
        self.sortby.place(x=20, y=300)

        self.sortcombo = ttk.Combobox(self.delfr2, font=15, width=9
                                      )
        self.sortcombo['values'] = (" First Name", "Last Name", "Contact", "Course", "Student Id")
        self.sortcombo.set(' First Name')
        self.sortcombo.place(x=100, y=300)

        self.sortbutton = Button(self.delfr2, text="SORT", font=("Times", 12), bg="linen", command=self.sort_info)
        self.sortbutton.place(x=230, y=300)
        self.backbutt = Button(newwin2, text='Back', font=("Times", 13), bg="linen", command=self.back_but)
        self.backbutt.place(x=30, y=40)
        self.select()

    def back_but(self):
        window.deiconify()
        self.newwin2.withdraw()
    def delete_data(self):
        try:
            student_id = int(self.entry_st.get())
            query = 'DELETE FROM tkintertbl1 WHERE student_id=%s'
            values = (student_id,)
            mycursor.execute(query, values)
            self.select()

            con.commit()
            tkinter.messagebox.showinfo('Success', ' Data deleted successfully')
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Select the data to be deleted')


    def search(self):
        newwin4 = Toplevel()
        newwin4.title('Search Data')
        newwin4.geometry('1200x1000')
        newwin4.resizable(0, 0)
        newwin4.configure(bg="thistle")

        self.newwin4=newwin4
        window.withdraw()

        self.newframe = Frame(newwin4, bd=4, relief=RIDGE, bg="thistle2")
        self.newframe.place(x=480, y=25, width=250, height=60)

        self.label1 = Label(self.newframe, text="Search the required data", bg="thistle2", font=("Times", 16))
        self.label1.place(x=10, y=10)

        self.newframe1 = Frame(newwin4, bd=4, relief=RIDGE, bg='alice blue')
        self.newframe1.place(x=20, y=100, width=650, height=600)

        scrollbarx = Scrollbar(self.newframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.newframe1, orient=VERTICAL)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.newframe1,
                                          columns=('First_name', 'Last_name', 'Contact', 'Course', 'student_id'),
                                          xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)

        self.student_table.heading('First_name', text='First Name')
        self.student_table.heading('Last_name', text='Last Name')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('student_id', text='student id')
        self.student_table['show'] = 'headings'

        self.student_table.column('First_name', width=160)
        self.student_table.column('Last_name', width=160)
        self.student_table.column('Contact', width=160)
        self.student_table.column('Course', width=160)
        self.student_table.column('student_id', width=160)

        scrollbarx.config(command=self.student_table.xview)
        scrollbary.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind('<ButtonRelease-1>')

        self.photo1=PhotoImage(file="search.gif")
        self.photolabel1=Label(newwin4,image=self.photo1)
        self.photolabel1.place(x=780,y=150,width=250,height=200)

        self.framesearch=Frame(newwin4,bg="thistle2",bd=4,relief=RIDGE)
        self.framesearch.place(x=720,y=380,width=430,height=160)

        self.searchby=Label(self.framesearch,text='Search by:',font=('Times',15),bg='thistle2')
        self.searchby.place(x=20,y=20)

        self.searchbox=ttk.Combobox(self.framesearch,font=('Times',12))
        self.searchbox['values']=("First name","Last name",'Contact',
                             "Course","Student Id")
        self.searchbox.set('First name')
        self.searchbox.place(x=120,y=20)
        self.searchtext=Label(self.framesearch,text="Search:",font=('Times',15),bg='thistle2')
        self.searchtext.place(x=20,y=60)

        self.textentry=Entry(self.framesearch,font=14,width=15,bd=2)
        self.textentry.place(x=100,y=60)

        searchbutton=Button(self.framesearch,text='Search',font=('Times',14),bg='lavender blush',
                            command=self.search_info)
        searchbutton.place(x=150,y=100)
        self.shoebutton=Button(self.framesearch,text='Show data',font=('Times',14),bg="lavenderblush",command=self.select)
        self.shoebutton.place(x=20,y=100)

        self.backbutt = Button(newwin4, text='Back', font=("Times", 13), bg="linen", command=self.back)
        self.backbutt.place(x=30, y=40)
        self.select()
    def back(self):
        window.deiconify()
        self.newwin4.withdraw()
    def search_info(self, mylist=None):
        if not mylist:
            query = 'select * from tkintertbl1'
            mycursor.execute(query)
            list_rows = mycursor.fetchall()

        else:
            list_rows = mylist
        # self.quick_sort(list_rows, 0, len(list_rows)- 1)
        self.student_table.delete(*self.student_table.get_children())

        entry_mt = self.textentry.get()
        comb = self.searchbox.get()
        if comb == "First name":
            column_index = 0

        elif comb == "Last name":
            column_index = 1
        elif comb == "Contact":
            column_index = 2
            entry_mt = int(self.textentry.get())
        elif comb == "Course":
            column_index = 3
        elif comb == "Student Id":
            column_index = 4
            entry_mt = int(self.textentry.get())
        else:
            column_index = 5

        result = []
        for xyz in list_rows:
            if entry_mt == xyz[column_index]:
                result.append(xyz)
        for xyz in result:
            self.student_table.insert('', 'end', values=xyz)

        if not result:
            tkinter.messagebox.showinfo('Error', 'Data not found.')

        return result

if __name__=="__main__":
    win=frame7(window)
    window.mainloop()
