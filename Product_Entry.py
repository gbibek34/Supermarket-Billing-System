from tkinter import *
from tkinter import ttk
from Query import query

class productEntry:
    def __init__(self, window):
        self.wn=window
        self.wn.title('Product Entry')
        self.wn.geometry("1055x545+200+100")
        self.exe=query()

    #==================================================Frames===================================================
        self.entry_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.entry_frame.place(x=10, y=10, width=430, height=530)
        self.table_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.table_frame.place(x=450, y=10, width=600, height=530)
        self.option_frame = Frame(self.entry_frame, relief=GROOVE, bd=5)
        self.option_frame.place(x=0, y=470, width=420, height=50)

    #==================================================Labels===================================================
        self.pdctid_lbl = Label(self.entry_frame, text='Product ID :',font=('arial', 11))
        self.pdctid_lbl.place(x=20,y=20)
        self.pdctcategory_lbl = Label(self.entry_frame, text='Category :',font=('arial', 11))
        self.pdctcategory_lbl.place(x=20,y=70)
        self.pdctname_lbl = Label(self.entry_frame, text='Product Name :',font=('arial', 11))
        self.pdctname_lbl.place(x=20,y=120)
        self.qty_lbl = Label(self.entry_frame, text='Quantity :',font=('arial', 11))
        self.qty_lbl.place(x=20,y=170)
        self.perpiece_lbl = Label(self.entry_frame, text='Per piece :',font=('arial', 11))
        self.perpiece_lbl.place(x=20,y=220)

    #==================================================Entry Data===================================================
        self.pdctid_val = StringVar()
        self.pdctname_val = StringVar()
        self.qty_val = StringVar()
        self.amt_val = StringVar()

    #==================================================Entry===================================================
        self.pdctid_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.pdctid_val, state="readonly")
        self.pdctid_ent.place(x=190,y=25)
        self.pdctcategory_ent = ttk.Combobox(self.entry_frame, font=('arial', 12), width=20, state='readonly')
        self.pdctcategory_ent['values']=("Chocolate","Vegetable","Cosmetic")
        self.pdctcategory_ent.place(x=190,y=75)
        self.pdctname_ent = Entry(self.entry_frame, font=('arial', 12), width=22,textvariable=self.pdctname_val)
        self.pdctname_ent.place(x=190,y=125)
        self.qty_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.qty_val)
        self.qty_ent.place(x=190,y=175)
        self.perpiece_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.amt_val)
        self.perpiece_ent.place(x=190,y=225)

    #==================================================Buttons===================================================
        self.add_btn = Button(self.entry_frame, text='ADD', height=2, width=12 ,command=self.add)
        self.add_btn.place(x=70,y=320)
        self.update_btn = Button(self.entry_frame, text='UPDATE', height=2, width=12, command=self.update)
        self.update_btn.place(x=190,y=320)
        self.delete_btn = Button(self.entry_frame, text='DELETE', height=2, width=12, command=self.delete)
        self.delete_btn.place(x=310,y=320)
        self.reset_btn = Button(self.entry_frame, text='RESET', height=2, width=24, command=self.reset)
        self.reset_btn.place(x=150, y=380)
        self.logout_btn = Button(self.option_frame, text='LOGOUT', height=2, width=12)
        self.logout_btn.pack(side=RIGHT)

    #==================================================Tree View===================================================
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.product_tbl = ttk.Treeview(self.table_frame,
                                       columns=("pid", "pcategory", "pname", "qty", "per_piece", "amt"),
                                       xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.product_tbl.yview, bg='#9BC01C')
        self.product_tbl.heading("pid",text="ID")
        self.product_tbl.heading("pcategory",text="Category")
        self.product_tbl.heading("pname",text="Product Name")
        self.product_tbl.heading("qty", text="Quantity")
        self.product_tbl.heading("per_piece", text="Per piece")
        self.product_tbl.heading("amt", text="Amount")
        self.product_tbl['show']='headings'
        self.product_tbl.column("pid", width=5)
        self.product_tbl.column("pcategory", width=50)
        self.product_tbl.column("pname", width=160)
        self.product_tbl.column("qty", width=10)
        self.product_tbl.column("per_piece", width=10)
        self.product_tbl.column("amt", width=40)
        self.product_tbl.pack(fill=BOTH, expand='1')
        self.fetch()

    #==================================================Methods===================================================
    def add(self):
        self.exe.add_items(self.pdctcategory_ent.get(),self.pdctname_val.get(), self.qty_val.get(), self.amt_val.get())
        self.fetch()

    def update(self):
        self.exe.update_items(self.pdctcategory_ent.get(), self.pdctname_val.get(), self.qty_val.get(), self.amt_val.get(),
        self.pdctid_val.get())
        self.fetch()
        return True

    def delete(self):
        self.exe.delete_items(self.pdctid_val.get())
        self.reset()
        self.fetch()

    def reset(self):
        self.pdctid_val.set('')
        self.pdctcategory_ent.set('')
        self.pdctname_val.set('')
        self.qty_val.set('')
        self.amt_val.set('')

    def fetch(self):
        data = self.exe.fetch_items()
        self.product_tbl.delete(*self.product_tbl.get_children())
        for i in data:
            self.product_tbl.insert("","end", value=i)
        self.product_tbl.bind('<Double-1>',self.select)
    
    def fill(self):
        self.reset()
        self.pdctid_val.set(self.row[0])
        self.pdctcategory_ent.set(self.row[1])
        self.pdctname_val.set(self.row[2])
        self.qty_val.set(self.row[3])
        self.amt_val.set(self.row[4])

    def select(self, event):
        self.row = self.product_tbl.item(self.product_tbl.selection(), "values")
        self.id = self.row[0]
        self.fill()




window=Tk()
productEntry(window)
window.mainloop()
