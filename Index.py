from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os
from tkinter import messagebox
import tempfile
import re
import tkinter
import mysql


def main_p():

    global v1, v2, top
    top = Tk(className=" BILLING SOFTWARE")
    top.geometry("650x450")
    top['background'] = '#fff'
    canvas = tkinter.Canvas(top, width=550, height=550, bg='#fff')
    canvas.pack(fill="both", expand=True)
    im = (Image.open(
        r'C:\Users\DELL\Documents\python project ca1\cesar-couto-27HiryxnHJk-unsplash.jpg'))
    resize = im.resize((650, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize)
    canvas.create_image(0, 0, anchor="nw", image=img)
    # labels
    canvas.create_text(330, 60, text="BILLING SOFTWARE",
                       font=("Times new roman", 20), fill="black")

    v1, v2 = StringVar(), StringVar()  # variables to store data
    # first entry

    e1 = tkinter.Entry(top, textvariable=v1, width=30)
    e1.insert(0, "   Enter UserID")
    canvas.create_window(330, 150, window=e1)

    def note():
        if(len(v1.get()) != 6):
            messagebox.showerror("Error", "Enter valid login details")
        else:
            login()

    # second entry
    e2 = tkinter.Entry(top, textvariable=v2, width=30)
    e2.insert(0, "   Enter Password")
    canvas.create_window(330, 200, window=e2)

    button1 = tkinter.Button(top, font=("arial", 9), bg="black",
                             text="Log In", command=note, fg="white", width=5, cursor="hand2")
    button_window = canvas.create_window(300, 250, anchor="nw", window=button1)
    # button2 = tkinter.Button(top, text="Sign Up")
    # button_window = canvas.create_window(80, 300, anchor="nw", window=button2)

    top.mainloop()


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        # ============variables================================
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        # product categories list
        self.tax = ["Select tax", "With GST", "Without GST"]
        self.Category = ["Select Option", "Clothing", "LifeStyle", "Mobile"]
        self.SubCatClothing = ["Pant", "T-Shirt", "Shirt"]
        self.pant = ["Levis", "Mufti", "Spykar"]
        self.price_levis = 5000
        self.price_mufti = 7000
        self.price_spaykar = 8000

        self.T_shirt = ["Polo", "Roadster", "Jack&Jones"]
        self.price_polo = 1500
        self.price_Roadster = 1800
        self.price_JackJones = 1700

        self.Shirt = ["Peter England", "Louis Phillipe", "Park Avenue"]
        self.price_Peter = 2100
        self.price_Louis = 2700
        self.price_Park = 1740
# subcat lifstyle
        self.SubCatLifStyle = ["Bath Soap", "Face Cream", "Hair Oil"]
        self.Bath_soap = ["LifeBuy", "Lux", "Santoor", "Pearl"]
        self.price_life = 20
        self.price_lux = 20
        self.price_santoor = 20
        self.price_pearl = 30

        self.Face_cream = ["Fair&Lovely", "Ponds", "Olay", "Garnier"]
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay = 20
        self.price_garnier = 30

        self.Hair_oil = ["Parachute", "Jashmin", "Bajaj"]
        self.price_para = 25
        self.price_jashmin = 22
        self.price_bajaj = 30
# subcatmobiles
        self.SubCatMobiles = ["Iphone", "Samsung", "Xiome", "RealMe", "One+"]
        self.Iphone = ["Iphone_X", "Iphone_11", "Iphone_12"]
        self.price_ix = 40000
        self.price_i11 = 60000
        self.price_i22 = 85000

        self.Samsung = ["Samsung M16", "Samsung M12", "Samsung M21"]
        self.price_sm16 = 16000
        self.price_sm12 = 12000
        self.price_sm21 = 18000

        self.Xiome = ["Red11", "Redme-12", "RedmePro"]
        self.price_r11 = 11000
        self.price_r12 = 12000
        self.price_rpro = 9000

        self.RealMe = ["RealMe 12", "RealMe 13", "RealMe Pro"]
        self.price_rel12 = 25000
        self.price_rel13 = 22000
        self.price_relpro = 30000

        self.OnePlus = ["OnePlus1", "OnePlus2", "OnePlus3"]
        self.price_one1 = 45000
        self.price_one2 = 60000
        self.price_one3 = 45800

       # image1
        img = Image.open("images/proimg1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=500, height=130)

        # image2
        img_1 = Image.open("images/proimg2.jpg")
        img_1 = img_1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        lbl_img_1 = Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=500, y=0, width=500, height=130)

        # image3
        img_2 = Image.open("images/proimg3.jpg")
        img_2 = img_2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=1000, y=0, width=500, height=130)

        lbl_title = Label(self.root, text="BILLING SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=-50, y=120, width=1500, height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=175, width=1500, height=600)

        # Customer LabelFrame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=(
            "times new roman", 15, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=340, height=140)

        self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=(
            "arial", 12, "bold"), bg="white", bd=4)
        self.lbl_mob.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(
            Cust_Frame, textvariable=self.c_phon, font=("arial", 10, "bold"), width=24)
        self.entry_mob.grid(row=1, column=1, stick=W, padx=5, pady=2)

        self.lblCustName = Label(Cust_Frame, text="Customer Name", font=(
            "arial", 12, "bold"), bg="white", bd=4)
        self.lblCustName.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(
            Cust_Frame, textvariable=self.c_name, font=("arial", 10, "bold"), width=24)
        self.txtCustName.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.lblEmail = Label(Cust_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Email", bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(
            Cust_Frame, textvariable=self.c_email, font=("arial", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=(
            "times new roman", 15, "bold"), bg="white", fg="red")
        Product_Frame.place(x=360, y=5, width=580, height=140)
        # category
        self.lblCategory = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Select Category", bd=4)
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, value=self.Category, font=(
            "arial", 10, "bold"), width=20, state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, stick=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)
        # sub category
        self.lblSubCategory = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="SubCategory", bd=4)
        self.lblSubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.ComboSubCategory = ttk.Combobox(Product_Frame, font=(
            "arial", 10, "bold"), width=20, value=[""], state="readonly")
        self.ComboSubCategory.grid(row=1, column=1, stick=W, padx=5, pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        # product name
        self.lblproduct = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Product Name", bd=4)
        self.lblproduct.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame, textvariable=self.product, font=(
            "arial", 10, "bold"), width=20, state="readonly")
        self.ComboProduct.grid(row=2, column=1, stick=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.price)
        # price
        self.lblPrice = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame, textvariable=self.prices, font=(
            "arial", 10, "bold"), width=20, state="readonly")
        self.ComboPrice.grid(row=0, column=3, stick=W, padx=5, pady=2)
        # qty
        self.lblQty = Label(Product_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Quantity", bd=4)
        self.lblQty.grid(row=1, column=2, stick=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame, textvariable=self.qty, font=(
            "arial", 10, "bold"), width=20, state="readonly")
        self.ComboQty.grid(row=1, column=3, stick=W, padx=5, pady=2)

        # middle frame
        MiddleFrame = Frame(Main_Frame, bd=4)
        MiddleFrame.place(x=6, y=150, width=935, height=340)

        # image12
        img12 = Image.open("images/two.jpg")
        img12 = img12.resize((490, 340), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        lbl_img12 = Label(MiddleFrame, image=self.photoimg12)
        lbl_img12.place(x=0, y=-90, width=490, height=340)

        # image13
        img_13 = Image.open("images/one.jpg")
        img_13 = img_13.resize((490, 340), Image.ANTIALIAS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)
        lbl_img_13 = Label(MiddleFrame, image=self.photoimg_13)
        lbl_img_13.place(x=490, y=-80, width=500, height=340)

        # search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=950, y=15, width=500, height=40)

        self.lblBill = Label(Search_Frame, font=(
            "arial", 12, "bold"), fg="white", bg="red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, stick=W, padx=2)

        self.txt_Entry_Search = ttk.Combobox(
            Search_Frame, textvariable=self.search_bill, font=("arial", 10, "bold"), width=15)
        self.txt_Entry_Search.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.BtnSearch = Button(
            Search_Frame, command=self.find_bill, text="Search", font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        # rightframe bill area
        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Area", font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=950, y=45, width=380, height=350)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set,
                             bg="white", fg="blue", font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Billcounter label frame
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=(
            "times new roman", 15, "bold"), bg="white", fg="red")
        Bottom_Frame.place(x=0, y=375, width=1330, height=135)

        self.lblSubTotal = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="SubTotal", bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(Bottom_Frame, textvariable=self.sub_total, font=(
            "arial", 10, "bold"), width=23, state="readonly")
        self.EntrySubTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

        # self.EntrySubTotal = ttk.Entry(
        #     Bottom_Frame, font=("arial", 10, "bold"), width=23)
        # self.EntrySubTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Gov Tax", bd=4)
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txt_tax = ttk.Combobox(
            Bottom_Frame,  font=("arial", 10, "bold"), text="Select tax", width=20, value=self.tax)
        self.txt_tax.grid(row=1, column=1, stick=W, padx=5, pady=2)

        self.lblAmount = Label(Bottom_Frame, font=(
            "arial", 12, "bold"), bg="white", text="Total", bd=4)
        self.lblAmount.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtAmount = ttk.Entry(
            Bottom_Frame, textvariable=self.total, font=("arial", 10, "bold"), width=23)
        self.txtAmount.grid(row=2, column=1, stick=W, padx=5, pady=2)


# button frame
        Btn_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart = Button(
            Btn_Frame, command=self.AddItem, text="Add To Cart", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill = Button(
            Btn_Frame, command=self.gen_bill, text="Generate Bill", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)

        self.BtnSave = Button(
            Btn_Frame, command=self.save_bill, text="Save Bill", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(
            Btn_Frame,  command=self.iprint, text="Print", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(
            Btn_Frame, command=self.clear, text="Clear", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(
            Btn_Frame, command=self.root.destroy, text="Exit", height=2, font=("arial", 13, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        self.welcome()

        self.l = []
        # =========Fucntoin declaration

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\t\t\t\t\t Welcome To Cart")
        self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END, "\n=======================================")
        self.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(
            END, "\n=======================================\n")

    def check(self):
        if(len(self.c_phon.get()) != 10 or not(self.c_phon.get().isdigit())):
            messagebox.showerror("Error", "Enter valid Phone Number")
            return 0
        elif re.search(".+[@].+['.'].+", self.c_email.get()) is None:
            messagebox.showerror("Error", "Enter valid Email")
            return 0
        return 1

    def AddItem(self):
        if(self.check()):
            Tax = 1
            self.n = self.prices.get()
            self.m = self.qty.get()*self.n
            self.l.append(self.m)
            if self.product.get() == "":
                messagebox.showerror("Error", "Please Select the Product Name")
            else:
                self.textarea.insert(
                    END, f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
                self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
            if (self.txt_tax.get() == "With GST"):
                self.tax_input.set(
                    str('Rs.%2f' % ((((sum(self.l))-(self.prices.get()))*Tax) / 100)))
            else:
                self.tax_input.set(
                    str('Rs.0'))
            # else:
            # self.tax_input.set(int('Rs.%.2f' % (sum(self.l))))
                self.total.set(str("Rs.%.2f" % (
                    (sum(self.l)+((((sum(self.l))-(self.prices.get()))*Tax) / 100)))))

    def gen_bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Add Product to Cart")
        else:
            text = self.textarea.get(10.0, (10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(
                END, "\n=======================================")
            self.textarea.insert(
                END, f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(
                END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(
                END, f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(
                END, "\n=======================================")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save bill?")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open('bills/'+str(self.bill_no.get())+".txt", 'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo(
                "Saved", f"Bill No.:{self.bill_no.get()} saved successfully")

            f1.close()

    def iprint(self):
        q = self.textarea.get(1.0,  "end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename, 'w').write(q)
        os.startfile(filename, "print")

    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills/{i}', 'r')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found = "yes"
        if found == 'no':
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l = [0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()

    def Categories(self, event=""):
        if self.Combo_Category.get() == "Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get() == "LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get() == "Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self, event=""):
        if self.ComboSubCategory.get() == "Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
# tshirt shirt
        if self.ComboSubCategory.get() == "T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
            # lifestyle
        if self.ComboSubCategory.get() == "Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

            # mobile

        if self.ComboSubCategory.get() == "Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get() == "One+":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)

    def price(self, event=""):
        # pant
        if self.ComboProduct.get() == "Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Spaykar":
            self.ComboPrice.config(value=self.price_spaykar)
            self.ComboPrice.current(0)
            self.qty.set(1)
    # tshirt
        if self.ComboProduct.get() == "Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jach&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)
# shirt
        if self.ComboProduct.get() == "Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)
# soap
        if self.ComboProduct.get() == "LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)
# cream
        if self.ComboProduct.get() == "Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)
            # oil

        if self.ComboProduct.get() == "Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

            # mobiles

        if self.ComboProduct.get() == "Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "OnePlus2":
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get() == "OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)


def login():
    top.destroy()
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()


if __name__ == '__main__':
    main_p()
