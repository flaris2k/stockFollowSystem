from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os

isTR = True
#BU RESOURCE PATHLAR SADECE PYINSTALLER İÇİN
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




class item():
	def __init__(self,name,stock,price,barcode):
		self.name = name
		self.stock = stock
		self.price = price
		self.barcode = barcode
class System(item):
	def __init__(self,name,stock,price,barcode):
		super().__init__(name,stock,price,barcode)

	def addItem(self):
		file = open("database.txt","a")
		if self.name != "" and self.stock !="" and self.price != "" and self.barcode !="":
			file.write(self.name+"-"+self.stock+"-"+self.price+"-"+self.barcode+"\n")
		file.close()
		
	def listItem(self):
		file = open("database.txt","r")
		for item in tw.get_children():	
			tw.delete(item)
		while True:
			line = file.readline().split("-")

			try:
				tw.insert("",END,values= (line[0],line[1],line[2],line[3]))
			except IndexError:
				break

		file.close()
	def searchItem(self,search):
		self.search = search
		file = open("database.txt","r")
		global data
		data = 0
		if searchCombo.get() == "İsim" or searchCombo.get() == "Name": data=0
		elif searchCombo.get() == "Stok" or searchCombo.get() == "Stock": data=1
		elif searchCombo.get() == "Fiyat" or searchCombo.get() == "Price": data=2
		elif searchCombo.get() == "Barkod" or searchCombo.get() == "Barcode": data=3
		for item in tw.get_children():
			tw.delete(item)
		while True:
			if search == "":
				break
			line = file.readline()
			lineSplit = line.split("-")
			try:
				if search in lineSplit[data]:
					tw.insert("",END,values = (lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3]))
			except IndexError:
				break
			if line == "":
				break
		file.close()
	def delItem(self):
		target = self.name+"-"+self.stock+"-"+self.price+"-"+self.barcode+"\n"
		ourText = ""
		file = open("database.txt","r")
		while True:
			line = file.readline()
			if line == target:
				pass
			elif line == "" or line == "\n":
				file.close()
				file = open("database.txt","w")
				file.write(ourText)
				break
			else:
				ourText += line
		file.close()
	def chgLang(self):
		global isTR

		if self.name == "englishmode":
			lb.config(image=tkimeg)
			searchCombo.set("Select Search Type")
			encomboList=["Name","Stock","Price","Barcode"]
			searchCombo.config(values=encomboList)

			addBtn.config(image=piAddImgen)
			deleteBtn.config(image=piDelImgen)
			searchBtn.config(image=piSearchImgen)
			resetBtn.config(image=piResetImgen)


		elif self.name == "turkishmode":
			lb.config(image=tkimg)
			searchCombo.set("Arama Tipini Seçiniz")
			comboList=["İsim","Stok","Fiyat","Barkod"]
			searchCombo.config(values=comboList)

			addBtn.config(image=piAddImgtr)
			deleteBtn.config(image=piDelImgtr)
			searchBtn.config(image=piSearchImgtr)
			resetBtn.config(image=piResetImgtr)
			

root = Tk()
root.iconbitmap(resource_path2("ic.ico"))
root.geometry("1420x820")
root.title("Stok Takip Programı")
root.resizable(False,False)


pitr = Image.open(resource_path2("image_1tr.png"))
pien = Image.open(resource_path2("image_1en.png"))
tkimg = ImageTk.PhotoImage(pitr)
tkimeg = ImageTk.PhotoImage(pien)

piAdd = Image.open(resource_path2("addBTNtr.png"))
piAddImgtr = ImageTk.PhotoImage(piAdd)
piSearch = Image.open(resource_path2("deleteBTNtr.png"))
piSearchImgtr = ImageTk.PhotoImage(piSearch)
piDel = Image.open(resource_path2("searchBTNtr.png"))
piDelImgtr = ImageTk.PhotoImage(piDel)
piReset = Image.open(resource_path2("resetBTNtr.png"))
piResetImgtr = ImageTk.PhotoImage(piReset)

piAdden = Image.open(resource_path2("addBTNen.png"))
piAddImgen = ImageTk.PhotoImage(piAdden)
piSearchen = Image.open(resource_path2("deleteBTNen.png"))
piSearchImgen = ImageTk.PhotoImage(piSearchen)
piDelen = Image.open(resource_path2("searchBTNen.png"))
piDelImgen = ImageTk.PhotoImage(piDelen)
piReseten = Image.open(resource_path2("resetBTNen.png"))
piResetImgen = ImageTk.PhotoImage(piReseten)


flagtr = Image.open(resource_path2("flag_tr.png"))
flagtrImg = ImageTk.PhotoImage(flagtr)

flagen = Image.open(resource_path2("flag_en.png"))
flagenImg = ImageTk.PhotoImage(flagen)



lb=Label(root,image=tkimg)
lb.place(relx=0,rely=0)




nameEntry=Entry(root,width=20,font=("Bahnschrift",12))
nameEntry.place(x=112,y=273)

stockEntry=Entry(root,width=20,font=("Bahnschrift",12))
stockEntry.place(x=112,y=312)

priceEntry=Entry(root,width=20,font=("Bahnschrift",12))
priceEntry.place(x=112,y=349)

barcodeEntry=Entry(root,width=20,font=("Bahnschrift",12))
barcodeEntry.place(x=112,y=387)

searchEntry=Entry(root,width=20,font=("Bahnschrift",12))
searchEntry.place(x=112,y=607)
comboList=["İsim","Stok","Fiyat","Barkod"]
searchCombo = ttk.Combobox(root,width=18,font = ("Bahnschrift",12),values=comboList)
searchCombo.set("Arama Tipini Seçiniz")
searchCombo.place(x=112,y=565)
def addFunc():
	sys = item(nameEntry.get(),stockEntry.get(),priceEntry.get(),barcodeEntry.get())
	System.addItem(sys)
	sys = item("","","","")
	System.listItem(sys)
def searchFunc():
	sys = item("","","","")
	System.searchItem(sys,searchEntry.get())
def resetFunc():
	sys = item("","","","")
	System.listItem(sys)
def delFunc():
	sys = item(nameEntry.get(),stockEntry.get(),priceEntry.get(),barcodeEntry.get())
	System.delItem(sys)
	sys = item("","","","")
	System.listItem(sys)
def chgFunc(modeSelection):
	
	if modeSelection == "en":
		sys = item("englishmode","","","")
		System.chgLang(sys)
	elif modeSelection == "tr":
		sys = item("turkishmode","","","")
		System.chgLang(sys)



trBtn = Button(root,image=flagtrImg,relief=SUNKEN,borderwidth=0,bg="#ababab",activebackground="#ababab",command=lambda:chgFunc("tr"))
trBtn.place(x=1310,y=37)

enBtn = Button(root,image=flagenImg,relief=SUNKEN,borderwidth=0,bg="#ababab",activebackground="#ababab",command=lambda:chgFunc("en"))
enBtn.place(x=1220,y=37)


addBtn = Button(root,image=piAddImgtr,borderwidth=0,bg="#ababab",activebackground="#ababab",relief=SUNKEN,command=addFunc)
addBtn.place(x=72,y=420)

deleteBtn = Button(root,image=piDelImgtr,borderwidth=0,bg="#ababab",activebackground="#ababab",relief=SUNKEN,command= searchFunc)
deleteBtn.place(x=72,y=640)

searchBtn = Button(root,image=piSearchImgtr,borderwidth=0,bg="#ababab",activebackground="#ababab",relief=SUNKEN,command = delFunc)
searchBtn.place(x=72,y=460)

resetBtn = Button(root,image=piResetImgtr,borderwidth=0,bg="#ababab",activebackground="#ababab",relief=SUNKEN,command = resetFunc)
resetBtn.place(x=72,y=680)

cList = ["Ürün Adı","Stok","Fiyat","Barkod"]
stt = ttk.Style()
stt.configure("Treeview",font=("Bahnschrift",12))
stt.configure("Treeview.Heading",font=("Bahnschrift",12),foreground="red")
tw = ttk.Treeview(root,height=28)
tw["column"] = cList

tw.column("#0",width=0,stretch=NO)
tw.column("Ürün Adı",minwidth=410,width= 410,anchor=CENTER)
tw.column("Stok",minwidth=110,width= 110,anchor=CENTER)
tw.column("Fiyat",minwidth=160,width= 160,anchor = CENTER)
tw.column("Barkod",minwidth=300,width= 300,anchor=CENTER)

tw.heading("#0",text="")
tw.heading("Ürün Adı",text="Ürün Adı")
tw.heading("Stok",text="Stok")
tw.heading("Fiyat",text="Fiyat")
tw.heading("Barkod",text="Barkod")
tw.place(x=393,y=178)

sys = item("","","","")
System.listItem(sys)
root.mainloop()