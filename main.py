
import mysql.connector
from tkinter import *
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style

style.use("ggplot")


def search():

    xList_temp.clear()
    xList_humi.clear()
    xList_pres.clear()
    yList.clear()

    a1.clear()
    a2.clear()
    a3.clear()

    q11 = q1.get() + " " + q2.get()
    q22 = q3.get() + " " + q4.get()

    mydb = mysql.connector.connect(
        host="192.168.1.90",
        user="mysql_user2",
        passwd="cycol101",
        database="DB_POMIARY"
    )
    c = mydb.cursor()
    c.execute("SELECT TEMP, HUMI, PRES, DATETIME FROM TAB_POMIARY WHERE DATETIME >= %s AND DATETIME <= %s", (q11, q22))
    results = c.fetchall()
    for row in results:
        xList_temp.append(row[0])
        xList_humi.append(row[1])
        xList_pres.append(row[2])
        yList.append(str(row[3]))

    a1.set_title("Temperatura [°C]")
    a2.set_title("Wilgotność [%]")
    a3.set_title("Ciśnienie atmosferyczne [hPa]")
    a1.plot(yList, xList_temp, "b", marker="o")
    a2.plot(yList, xList_humi, "r", marker="o")
    a3.plot(yList, xList_pres, "g", marker="o")

    f1.autofmt_xdate()
    f2.autofmt_xdate()
    f3.autofmt_xdate()

    f1.tight_layout()
    f2.tight_layout()
    f3.tight_layout()

    canvas1.draw()
    canvas2.draw()
    canvas3.draw()

    maxtemp = max(xList_temp)
    lab3.config(text=str(maxtemp)+"°C")
    maxpres = max(xList_pres)
    lab15.config(text=str(maxpres)+" hPa")
    maxhumi = max(xList_humi)
    lab9.config(text=str(maxhumi)+"%")
    mintemp = min(xList_temp)
    lab7.config(text=str(mintemp)+"°C")
    minhumi = min(xList_humi)
    lab13.config(text=str(minhumi)+"%")
    minpres = min(xList_pres)
    lab19.config(text=str(minpres)+" hPa")


window = tk.Tk()

window.title("Stacja meteorologiczna")
window.geometry("1400x750")
window.iconbitmap(r'C:\Users\cygan\Downloads\sunny_weather_icon_150663.ico')
window.resizable(False, False)

xList_temp = [0]
xList_humi = [0]
xList_pres = [0]
yList = [0]
f1 = Figure(figsize=(25, 3), dpi=55)
a1 = f1.add_subplot(1, 1, 1)
f2 = Figure(figsize=(25, 3), dpi=55)
a2 = f2.add_subplot(1, 1, 1)
f3 = Figure(figsize=(25, 3), dpi=55)
a3 = f3.add_subplot(1, 1, 1)
q1 = StringVar()
q2 = StringVar()
q3 = StringVar()
q4 = StringVar()

maxtemp = 0
maxpres = 0
maxhumi = 0
mintemp = 0
minhumi = 0
minpres = 0


wrapper1 = tk.LabelFrame(window, text="Wyszukiwanie")
wrapper1.pack(fill="both", expand="True", padx=20, pady=10)

label = Label(wrapper1)
label.pack(side=LEFT, padx=150)
label1 = Label(wrapper1, text="Data")
label1.pack(side=LEFT, padx=10)
entry1 = Entry(wrapper1, textvariable=q1)
entry1.pack(side=LEFT, padx=6)
label2 = Label(wrapper1, text="Godzina")
label2.pack(side=LEFT, padx=6)
entry2 = Entry(wrapper1, textvariable=q2)
entry2.pack(side=LEFT, padx=6)
label3 = Label(wrapper1, text="Data")
label3.pack(side=LEFT, padx=6)
entry3 = Entry(wrapper1, textvariable=q3)
entry3.pack(side=LEFT, padx=6)
label4 = Label(wrapper1, text="Godzina")
label4.pack(side=LEFT, padx=6)
entry4 = Entry(wrapper1, textvariable=q4)
entry4.pack(side=LEFT, padx=6)
button1 = Button(wrapper1, text="Szukaj", command=search)
button1.pack(side=LEFT, padx=10)


wrapper2 = tk.LabelFrame(window, text="Wykresy")
wrapper2. pack(fill="both", expand="True", padx=20, pady=5)

a1.set_title("Temperatura [°C]")
a2.set_title("Wilgotność [%]")
a3.set_title("Ciśnienie atmosferyczne [hPa]")

canvas1 = FigureCanvasTkAgg(f1, wrapper2)
canvas1.get_tk_widget().pack(pady=10)
canvas2 = FigureCanvasTkAgg(f2, wrapper2)
canvas2.get_tk_widget().pack(pady=10)
canvas3 = FigureCanvasTkAgg(f3, wrapper2)
canvas3.get_tk_widget().pack(pady=10)

wrapper3 = tk.LabelFrame(window, text="Informacje")
wrapper3. pack(fill="both", expand="True", padx=20, pady=10)
lab1 = Label(wrapper3)
lab1.pack(side=LEFT, padx=30)
lab2 = Label(wrapper3, text="Maksymalna temperatura")
lab2.pack(side=LEFT, padx=10)
lab3 = Label(wrapper3, text=str(maxtemp)+"°C")
lab3.pack(side=LEFT, padx=6)
lab6 = Label(wrapper3, text="Minimalna temperatura")
lab6.pack(side=LEFT, padx=10)
lab7 = Label(wrapper3, text=str(mintemp)+"°C")
lab7.pack(side=LEFT, padx=6)
lab8 = Label(wrapper3, text="Maksymalna wilgotność")
lab8.pack(side=LEFT, padx=10)
lab9 = Label(wrapper3, text=str(maxhumi)+"%")
lab9.pack(side=LEFT, padx=6)
lab12 = Label(wrapper3, text="Minimalna wilgotność")
lab12.pack(side=LEFT, padx=10)
lab13 = Label(wrapper3, text=str(minhumi)+"%")
lab13.pack(side=LEFT, padx=6)
lab14 = Label(wrapper3, text="Makasymalne ciśnienie")
lab14.pack(side=LEFT, padx=10)
lab15 = Label(wrapper3, text=str(maxpres)+" hPa")
lab15.pack(side=LEFT, padx=6)
lab18 = Label(wrapper3, text="Minimalne ciśnienie")
lab18.pack(side=LEFT, padx=10)
lab19 = Label(wrapper3, text=str(minpres)+" hPa")
lab19.pack(side=LEFT, padx=6)

window.mainloop()



