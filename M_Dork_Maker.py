# Coded By MuhammedTr768
# hackersmtt@gmail.com
# TurkHackTeam - MuhammedTr768
from tkinter import *
from tkinter import messagebox

pen = Tk()
pen.title('M Dork Maker')
pen.geometry('500x400')

def kontrol():
    sonuc["text"] = "site:" + entry.get(), "filetype:" + entry2.get(), "intitle:" + entry3.get(), "intext:" + entry4.get(), "inurl:" + entry5.get()
    filecreat = open("mdork.txt", "w")
    filecreat.write(sonuc["text"])
    filecreat.close()
girbt = Button(pen, text="Gir", command=kontrol)
girbt.pack()

sad = Label(pen, text="Site Adı ve Uzantısını Girin:")
sad.pack()

entry = Entry(pen, width=15)
entry.pack()

dtip = Label(pen, text="Dosya Tipini Seçin")
dtip.pack()

entry2 = Entry(pen, width=15)
entry2.pack()

sbas = Label(pen, text="Site Başlığını Seçin")
sbas.pack()

entry3 = Entry(pen, width=15)
entry3.pack()

sicerik = Label(pen, text="Sitenin İçerisinde Yazmasını İstediğiniz Şeyi Girin:")
sicerik.pack()

entry4 = Entry(pen, width=15)
entry4.pack()

urlicer = Label(pen, text="URL'nin İçerisinde Yazmasını İstediğiniz Şeyi Girin:")
urlicer.pack()

entry5 = Entry(pen, width=15)
entry5.pack()

sonuc = Label(pen, text="")
sonuc.pack()


pen.mainloop()