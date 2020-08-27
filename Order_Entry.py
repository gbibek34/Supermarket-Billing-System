from tkinter import *
from tkinter import ttk
from Query import query

class orderEntry():
    def __init__(self, window):
        self.wn = window
        self.wn.title("Order Entry")
        self.wn.geometry("1055x500+200+100")
        self.exe=query()
        self.cost_val=StringVar()
        self.qty_val=StringVar()

        #======================================================Frames======================================================
        self.entry_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.entry_frame.place(x=10, y=10, width=430, height=485)
        self.product_frame = Frame(self.wn, relief=GROOVE, bd=5)
        self.product_frame.place(x=450, y=10, width=600, height=485)
        self.table_frame = Frame(self.product_frame)
        self.table_frame.place(x=0, y=0, width=590, height=420)
        self.option_frame = Frame(self.entry_frame, relief=GROOVE, bd=5)
        self.option_frame.place(x=0, y=425, width=420, height=50)

        #======================================================Labels======================================================
        self.category_lbl = Label(self.entry_frame, text='Category :', font=('arial', 11))
        self.category_lbl.place(x=20, y=20)
        self.name_lbl = Label(self.entry_frame, text='Name :', font=('arial', 11))
        self.name_lbl.place(x=20, y=70)
        self.available_lbl = Label(self.entry_frame, text='Availability :', font=('arial', 11))
        self.available_lbl.place(x=20, y=120)
        self.qty_lbl = Label(self.entry_frame, text='Quanity :', font=('arial', 11))
        self.qty_lbl.place(x=20, y=170)
        self.cost_lbl = Label(self.entry_frame, text='Cost :', font=('arial', 11))
        self.cost_lbl.place(x=20, y=220)
        self.username_lbl = Label(self.product_frame, text='User :', font=('arial', 11))
        self.username_lbl.place(x=5, y=435)

        #======================================================Entry======================================================
        self.category_ent = ttk.Combobox(self.entry_frame, font=('arial', 12), width=20, state='readonly')
        self.category_ent['values']=("Chocolate","Vegetable","Cosmetic")
        self.category_ent.place(x=150, y=20)
        self.name_ent = ttk.Combobox(self.entry_frame, font=('arial', 12), width=20, state='readonly')
        self.name_ent['values']=()
        self.name_ent.place(x=150, y=70)
        self.available_ent = Label(self.entry_frame, text='', font=('arial', 12))
        self.available_ent.place(x=150, y=120)
        self.qty_ent = Entry(self.entry_frame, font=('arial', 12), width=22, textvariable=self.qty_val)
        self.qty_ent.place(x=150, y=170)
        self.cost_ent = Entry(self.entry_frame, font=('arial', 12), width=22, state='readonly',
                              relief=FLAT,textvariable=self.cost_val)
        self.cost_ent.place(x=150, y=220)
        self.username_ent = Entry(self.product_frame, font=('arial', 20), width=25)
        self.username_ent.place(x=50, y=430)
        self.category_ent.bind("<<ComboboxSelected>>",self.cateogry)

        #======================================================Buttons=====================================================
        self.addtocart_btn = Button(self.entry_frame, text='ADD TO CART', height=2, width=22, command=self.addtocart)
        self.addtocart_btn.place(x=40, y=300)
        self.updatecart_btn = Button(self.entry_frame, text='UPDATE CART', height =2, width =22, command=self.updatecart)
        self.updatecart_btn.place(x=210, y=300)
        self.remove_btn = Button(self.entry_frame, text='REMOVE FROM CART', height=2, width=22,command=self.deletecart)
        self.remove_btn.place(x=40, y=350)
        self.reset_btn = Button(self.entry_frame, text='RESET', height=2, width=22, command=self.reset)
        self.reset_btn.place(x=210, y=350)
        self.bill_btn = Button(self.product_frame, text='BILL ITEMS', height=2, width=12, command=self.bill)
        self.bill_btn.place(x=480, y=425)

        #==================================================Tree View===================================================
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.billing_tbl = ttk.Treeview(self.table_frame,
                                        columns=("pcategory", "pname", "qty", "amt"),
                                        xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.billing_tbl.yview, bg='#9BC01C')
        self.billing_tbl.heading("pcategory", text="Category")
        self.billing_tbl.heading("pname", text="Product Name")
        self.billing_tbl.heading("qty", text="Quantity")
        self.billing_tbl.heading("amt", text="Amount")
        self.billing_tbl['show'] = 'headings'
        self.billing_tbl.column("pcategory", width=60)
        self.billing_tbl.column("pname", width=100)
        self.billing_tbl.column("qty", width=10)
        self.billing_tbl.column("amt", width=40)
        self.billing_tbl.pack(fill=BOTH, expand='1')
        self.listitems()

    #==================================================Methods===================================================
    def addtocart(self):
        self.exe.addtocart_items(self.category_ent.get(), self.name_ent.get(), self.qty_val.get(), self.cost_val.get())
        self.listitems()
        self.reset()

    def updatecart(self):
        self.exe.updatecart_items(self.qty_val.get(), self.cost_val.get(), self.id)
        self.listitems()
        self.reset()
        return True

    def deletecart(self):
        self.exe.deletecart_items(self.id)
        self.reset()
        self.listitems()

    def reset(self):
        self.category_ent.set('')
        self.name_ent.set('')
        self.qty_val.set('')
        self.available_ent.config(text='')
        self.cost_val.set('')

    def listitems(self):
        data = self.exe.fetchcart_items()
        self.billing_tbl.delete(*self.billing_tbl.get_children())
        for i in data:
            self.billing_tbl.insert("","end", value=(i[1],i[2],i[3],i[5],i[4]),text=i[0])
        self.billing_tbl.bind('<Double-1>',self.select)

    def select(self, event):
        self.row = self.billing_tbl.item(self.billing_tbl.selection(), "values")
        self.id = self.billing_tbl.item(self.billing_tbl.selection(), "text")
        self.fill()

    def fill(self):
        self.reset()
        self.category_ent.set(self.row[0])
        self.name_ent.set(self.row[1])
        self.qty_val.set(self.row[2])
        self.cost_val.set(self.row[4])

    def cateogry(self, event):
        data = self.exe.fetch_category(self.category_ent.selection_get())
        self.name_ent['values'] = data
        self.name_ent.bind("<<ComboboxSelected>>",self.name)

    def name(self, event):
        self.data = self.exe.fetch_name(self.name_ent.selection_get())
        self.available_ent.config(text=self.data[0][0])
        self.cost_val.set(self.data[0][1])

    def bill(self):
        self.exe.clear_tbl()
        self.listitems()


window = Tk()
orderEntry(window)
window.mainloop()
