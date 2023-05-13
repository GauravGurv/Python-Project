from tkinter import ttk
from tkinter import *
import mysql.connector

class LMS:
    def __init__(self,root):  # define constructer, root is used to naming window(you can change the name as per your convienent)
        self.root = root
        self.root.geometry("1600x800+0+0")  # fill the size of window("resoulation" + x-axis + y-axis)

        # Established a connection between database and mysql.connector
        conn = mysql.connector.connect(host="localhost", username="root", password="HEFD", database="project_work")

        data = conn.cursor()

        # import a table name on particular database
        data.execute('SELECT * FROM project_work.hms_records')

        # ===============================Variables=========================================
        self.member_var = StringVar()
        self.ref_no_var = StringVar()
        self.pid_var = StringVar()
        self.p_name_var = StringVar()
        self.p_fname_var = StringVar()
        self.p_mname_var = StringVar()
        self.add_var = StringVar()
        self.mob_var = StringVar()
        self.daysonadmit_var = StringVar()
        self.daysonrelease_var = StringVar()
        self.d_name1_var = StringVar()
        self.d_name2_var = StringVar()
        self.d_name3_var = StringVar()
        self.noofdays_var = StringVar()
        self.chambertype_var = StringVar()
        self.totalamount_var = StringVar()
        self.paid_var = StringVar()
        self.dues_var = StringVar()
        self.final_var = StringVar()


        # Label((text=label name), (bg=background color), (fg=forground color), (bd=border,border style),(font=font family),(padding is used to padx & pady))
        title = Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", bg="GreenYellow", fg="black", bd=15, relief=RIDGE, font=("times new roman", 20, "bold"), padx=2, pady=6)
        title.pack(side=TOP, fill=X)  # packing to label(side position, x-axis)

        # frame(window, border, border-style, padding x-axis, bg color)
        frame = Frame(self.root, bd=5, relief=RIDGE, padx=5, bg="GreenYellow")
        frame.place(x=0, y=50, relwidth=1, relheight=1)
        # frame.place(x=0, y=70, width=1530, height=400)  # frame.placeing(position of frame in window, set height and width of them)

        # -----------------------------DataFrame Left-----------------------------------
        # (DataFrameposition=(Lable of frame(frame title, bg,fg,bd,font)))
        DataFrameLeft = LabelFrame(frame, text="Petient Information", bg="GreenYellow", fg="black", bd=10, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=2, width=900, height=370)  # Display data farme in left position with dimension from axis and set height and width

        # ---------------------------1st Row------------------------------
        # label--make a label of text and we should show up on grid format for our convient
        lblMember = Label(DataFrameLeft, bg='GreenYellow',textvariable=self.member_var, text='Member Type', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        # ttk is important module to call combobox from calling of framename
        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("times new roman", 12, "bold"),width=27, state='readonly')  # state is used to freeze value on readable or writable
        comMember['value'] = ('Admin staff', 'Patient', 'Staff')  # it Pass the tuple of records
        comMember.current(1)
        comMember.grid(row=0, column=1)

        lblref_no = Label(DataFrameLeft, bg='GreenYellow', text='#Reff No.', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblref_no.grid(row=1, column=0, sticky=W)  # Row indicate of position column indicates direction
        txtref_no = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.ref_no_var, width=29)
        txtref_no.grid(row=1, column=1)

        lblpid = Label(DataFrameLeft, bg='GreenYellow', text='ID No.', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpid.grid(row=2, column=0, sticky=W)
        txtpid = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.pid_var, width=29)
        txtpid.grid(row=2, column=1)

        lblp_name = Label(DataFrameLeft, bg='GreenYellow', text='Patient Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblp_name.grid(row=3, column=0, sticky=W)
        txtp_name = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.p_name_var, width=29)
        txtp_name.grid(row=3, column=1)

        lblp_fname = Label(DataFrameLeft, bg='GreenYellow', text='Patient Father Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblp_fname.grid(row=4, column=0, sticky=W)
        txtp_fname = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.p_fname_var, width=29)
        txtp_fname.grid(row=4, column=1)

        lblp_mname = Label(DataFrameLeft, bg='GreenYellow', text='Patient Mother Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblp_mname.grid(row=5, column=0, sticky=W)
        txtp_mname = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.p_mname_var, width=29)
        txtp_mname.grid(row=5, column=1)

        lblAdd = Label(DataFrameLeft, bg='GreenYellow', text='Address', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAdd.grid(row=6, column=0, sticky=W)
        txtAdd = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.add_var, width=29)
        txtAdd.grid(row=6, column=1)

        lblmob = Label(DataFrameLeft, bg='GreenYellow', text='Mobile No.', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblmob.grid(row=7, column=0, sticky=W)
        txtmob = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.mob_var, width=29)
        txtmob.grid(row=7, column=1)

        lbldoa = Label(DataFrameLeft, bg='GreenYellow', text='Date of Admit', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbldoa.grid(row=8, column=0, sticky=W)
        txtdoa = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.daysonadmit_var, width=29)
        txtdoa.grid(row=8, column=1)

        lbldor = Label(DataFrameLeft, bg='GreenYellow', text='Date of Release', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbldor.grid(row=9, column=0, sticky=W)
        txtdor = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.daysonrelease_var, width=29)
        txtdor.grid(row=9, column=1)

        # ---------------------------2nd Row------------------------------

        lbld_name1 = Label(DataFrameLeft, bg='GreenYellow', text='1 Doctor Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbld_name1.grid(row=1, column=2, sticky=W)
        comdoc1 = ttk.Combobox(DataFrameLeft, textvariable=self.d_name1_var, font=("times new roman", 12, "bold"),width=27, state='readonly')  # state is used to freeze value on readable or writable
        comdoc1['value'] = ('Dr. Siddhartha Mukherjee', 'Dr. Naresh Trehan', 'Dr. Sudhansu Bhattacharyya',' Dr. Surbhi Anand','Dr. Ashish Sabharwal',
                            'Dr. Sanjay Sachdeva','Dr. Aditya Gupta',' Dr. H. S. Chhabra','Dr. Gaurav Kharya','Dr. Mohamed Rela')  # it Pass the tuple of records
        comdoc1.grid(row=1, column=3)

        lbld_name2 = Label(DataFrameLeft, bg='GreenYellow', text='2 Doctor Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbld_name2.grid(row=2, column=2, sticky=W)
        comdoc2 = ttk.Combobox(DataFrameLeft, textvariable=self.d_name2_var, font=("times new roman", 12, "bold"),width=27, state='readonly')  # state is used to freeze value on readable or writable
        comdoc2['value'] = ('Dr. Siddhartha Mukherjee', 'Dr. Naresh Trehan', 'Dr. Sudhansu Bhattacharyya',' Dr. Surbhi Anand','Dr. Ashish Sabharwal',
                            'Dr. Sanjay Sachdeva','Dr. Aditya Gupta',' Dr. H. S. Chhabra','Dr. Gaurav Kharya','Dr. Mohamed Rela')
        comdoc2.grid(row=2, column=3)

        lbld_name3 = Label(DataFrameLeft, bg='GreenYellow', text='3 Doctor Name', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbld_name3.grid(row=3, column=2, sticky=W)
        comdoc3 = ttk.Combobox(DataFrameLeft, textvariable=self.d_name3_var, font=("times new roman", 12, "bold"),width=27, state='readonly')  # state is used to freeze value on readable or writable
        comdoc3['value'] = ('Dr. Siddhartha Mukherjee', 'Dr. Naresh Trehan', 'Dr. Sudhansu Bhattacharyya',' Dr. Surbhi Anand','Dr. Ashish Sabharwal',
                            'Dr. Sanjay Sachdeva','Dr. Aditya Gupta',' Dr. H. S. Chhabra','Dr. Gaurav Kharya','Dr. Mohamed Rela')  # it Pass the tuple of records
        comdoc3.grid(row=3, column=3)

        lblnod = Label(DataFrameLeft, bg='GreenYellow', text='No of Days', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblnod.grid(row=4, column=2, sticky=W)
        txtnod = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.noofdays_var, width=29)
        txtnod.grid(row=4, column=3)

        lblctype = Label(DataFrameLeft, bg='GreenYellow', text='Chamber Type', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblctype.grid(row=5, column=2, sticky=W)
        comctype = ttk.Combobox(DataFrameLeft, textvariable=self.chambertype_var, font=("times new roman", 12, "bold"),width=27, state='readonly')  # state is used to freeze value on readable or writable
        comctype['value'] = ('Common Area','Private Room','AC Room','2in Bed Room','Luxury Room')
        comctype.current(0)
        comctype.grid(row=5, column=3)

        lbltotal = Label(DataFrameLeft, bg='GreenYellow', text='Total Amount:', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbltotal.grid(row=6, column=2, sticky=W)
        txttotal = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.totalamount_var, width=29)
        txttotal.grid(row=6, column=3)

        lblpaid = Label(DataFrameLeft, bg='GreenYellow', text='Paid:',font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpaid.grid(row=7, column=2, sticky=W)
        txtpaid = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.paid_var, width=29)
        txtpaid.grid(row=7, column=3)

        lbldues = Label(DataFrameLeft, bg='GreenYellow', text='Dues:', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbldues.grid(row=8, column=2, sticky=W)
        txtdues = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.dues_var, width=29)
        txtdues.grid(row=8, column=3)

        lblfinal = Label(DataFrameLeft, bg='GreenYellow', text='Final Amount', font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblfinal.grid(row=9, column=2, sticky=W)
        txtfinal = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.final_var, width=29)
        txtfinal.grid(row=9, column=3)

        # -----------------------------DataFrame Right-----------------------------------
        DataFrameRight = LabelFrame(frame, text="Specialisation", bg="GreenYellow", fg="black", bd=10, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=2, width=610, height=370)

        self.txtBox = Text(DataFrameRight, font=("times new roman", 12, "bold"), width=40, height=18, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')

        listBooks = ['Adult Kidney Transplant','Anaesthesia','Blood Bank','Bone Marrow Transplant (Stem Cell Transplant)','Breast Cancer',
                     'Cardiac Surgery','Cardiac Surgery - Paediatric','Paediatric','Cardiology','Cardiology - Paediatric','Clinical Nutrition & Dietetics',
                     'Cranio Maxillo Facial Surgery','Critical Care','Dental Sciences','Dermatology And Cosmetology','Diabetology','Electrophysiology',
                     'Emergency Medicine','Endocrinology','ENT(Ear, Nose, Throat)','Family Medicine','Gastrointestinal Oncology','General Surgery','Genetics',
                     'Geriatrics','Gynaecology - Oncology','Haemato Oncology','Haematology','Head & Neck Surgery - Oncology','Heart Transplant',
                     'Hepatology & Liver Transplantation','Infectious Diseases','Integrative Oncology','Internal Medicine','Interventional Radiology',
                     'Kidney Transplant - Paediatric','Liver Transplant & HPB Surgery','Medical Gastroenterology','Medical Labs','Medical Oncology',
                     'Microbiology','Neonatal Surgery','Neonatology','Nephrology','Neurology','Neurology - Paediatric','Neurosurgery','NICU & PICU',
                     'Nuclear Medicine','Obstetrics & Gynaecology','Oncology','Oncology - Paediatric','Ophthalmology','Ortho - Oncology','Orthopaedics',
                     'Paediatric ENT(Ear, Nose, Throat)','Paediatric Liver Transplantation','Paediatric Nephrology','Paediatric Neurosurgery','Paediatric Thoracic & Vascular Surgery',
                     'Paediatrics','Paediatrics Surgery','Pain & Palliative Care','Pathology','Pediatric Dental Sciences','Pediatric Developmental','Pediatric Endocrinology',
                     'Pediatric Gastroenterology & Hepatology','Pediatric Orthopaedics','Pediatrics Pulmonology','Physical Medicine And Rehabilitation',
                     'Physiotherapy & Rehabilitation','Plastic Surgery','Psychiatry & Clinical Psychology','Pulmonology','Radiation Oncology',
                     'Radiology','Reproductive Medicine','Rheumatology','Rheumatology - Paediatric','Robotic Surgery','Speech And Swallow Rehabilitation',
                     'Spine Surgery','Surgical Gastroenterology','Surgical Oncology','Thoracic Surgery','Uro - Oncology','Urology','Vascular Surgery',
                     ]

        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=28, height=16)
        # Listbox.bind('<<ListBoxSelect>>', SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        # -----------------------------Button Frame-----------------------------------
        # frame(window, border, border-style, padding x-axis, bg color)
        framebutton = Frame(self.root, bd=5, relief=RIDGE, padx=20, bg="white")
        framebutton.place(x=0, y=430, width=1530, height=60)  # frame.placeing(position of frame in window, set height and width of them)

        btnAddData = Button(framebutton, text="Add Data", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=0, padx=14)
        btnAddData = Button(framebutton, text="Show Data", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=1,padx=14)
        btnAddData = Button(framebutton, text="Update", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=2, padx=14)
        btnAddData = Button(framebutton, text="Delete", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=3, padx=14)
        btnAddData = Button(framebutton, text="Reset", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=4, padx=14)
        btnAddData = Button(framebutton, text="Exit", font=("times new roman", 12, "bold"), width=20, bg="Green", fg='white', padx=14, pady=10)
        btnAddData.grid(row=0, column=5, padx=14)

        # -----------------------------Information Frame-------------------------------
        # frame(window, border, border-style, padding x-axis, bg color)
        frameDetails = Frame(self.root, bd=8, relief=RIDGE, padx=5, bg="GreenYellow")
        frameDetails.place(x=0, y=480, relwidth=1, relheight=0.4)  # frame.placeing(position of frame in window, set height and width of them)

        xscroll = ttk.Scrollbar(frameDetails, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(frameDetails, orient=VERTICAL)

        self.library_table = ttk.Treeview(frameDetails, columns=("ref_no", "pid", "p_name", "p_fname", "p_mname", "add", "mob", "daysonadmit", "daysonrelease",
                                                                 "d_name1", "d_name2", "d_name3", "noofdays", "chambertype", "totalamount", "paid","dues","final"))

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("ref_no", text="Refrence No.",anchor=CENTER)
        self.library_table.heading("pid", text="Patient Id",anchor=CENTER)
        self.library_table.heading("p_name", text="Patient Full Name",anchor=CENTER)
        self.library_table.heading("p_fname", text="Patient Father Name",anchor=CENTER)
        self.library_table.heading("p_mname", text="Patient Mother Name",anchor=CENTER)
        self.library_table.heading("add", text="Address",anchor=CENTER)
        self.library_table.heading("mob", text="Mobile No.",anchor=CENTER)
        self.library_table.heading("daysonadmit", text="Days On Admit",anchor=CENTER)
        self.library_table.heading("daysonrelease", text="Days On Release",anchor=CENTER)
        self.library_table.heading("d_name1", text="Doctor Name1",anchor=CENTER)
        self.library_table.heading("d_name2", text="Doctor Name2",anchor=CENTER)
        self.library_table.heading("d_name3", text="Doctor Name3",anchor=CENTER)
        self.library_table.heading("noofdays", text="Numbers of Days",anchor=CENTER)
        self.library_table.heading("chambertype", text="Chamber of Type",anchor=CENTER)
        self.library_table.heading("totalamount", text="Total Amount",anchor=CENTER)
        self.library_table.heading("paid", text="Total Paid",anchor=CENTER)
        self.library_table.heading("dues", text="Total Dues",anchor=CENTER)
        self.library_table.heading("final", text="Final Amount",anchor=CENTER)

        self.library_table["show"] = "headings"
        self.library_table.pack(side=TOP,fill=BOTH, expand=1)


        self.library_table.column("ref_no", width=50)
        self.library_table.column("pid", width=60)
        self.library_table.column("p_name", width=200)
        self.library_table.column("p_fname", width=200)
        self.library_table.column("p_mname", width=200)
        self.library_table.column("add", width=300)
        self.library_table.column("mob", width=100)
        self.library_table.column("daysonadmit", width=100)
        self.library_table.column("daysonrelease", width=100)
        self.library_table.column("d_name1", width=200)
        self.library_table.column("d_name2", width=200)
        self.library_table.column("d_name3", width=200)
        self.library_table.column("noofdays", width=40)
        self.library_table.column("chambertype", width=150)
        self.library_table.column("totalamount", width=100)
        self.library_table.column("paid", width=100)
        self.library_table.column("dues", width=100)
        self.library_table.column("final", width=100)


if __name__ == "__main__":
    root = Tk()
    obj = LMS(root)  # making obj of LMS
    root.mainloop()  # it is used to load and hold the screen otherwise it close within 1 sec.
