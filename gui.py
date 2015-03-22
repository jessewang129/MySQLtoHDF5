from Tkinter import *
master = Tk()

var_l = StringVar(master)
var_l.set("Kaiser Alpha Lab") 
var_y_s = StringVar(master)
var_y_s.set("2015")
var_m_s = StringVar(master)
var_m_s.set("1")
var_d_s = StringVar(master)
var_d_s.set("1")
var_y_e = StringVar(master)
var_y_e.set("2015")
var_m_e = StringVar(master)
var_m_e.set("1")
var_d_e = StringVar(master)
var_d_e.set("1")

label_l = Label(master, text = "Select location:")
label_l.grid(row = 0, sticky = E)
location = OptionMenu(master, var_l, "Kaiser Alpha Lab", "Kaiser Utiilty-AMPS80", "LMRS-AMPS225", "LMRS-AMPS80", "NCE-AMPS80")
location.grid(row = 0, column = 1)

label_y = Label(master, text = " Staring Date:	Year:")
label_y.grid(row = 1, column = 1,sticky = W)
year = OptionMenu(master, var_y_s, "2013", "2014", "2015")
year.grid(row = 1, column = 2)

label_m = Label(master, text = "Month:")
label_m.grid(row = 1, column = 3)
months = ["1"]
for m in range (2, 13):
	months.append(m)
month = OptionMenu(master, var_m_s, *months)
month.grid(row = 1, column = 4)

label_d = Label(master, text = "Day:")
label_d.grid(row = 1, column = 5)
days = ["1"]
for d in range(2, 32):
	days.append(d)
day = OptionMenu(master, var_d_s, *days)
day.grid(row = 1, column = 6)

label_y = Label(master, text = " Ending Date:	Year:")
label_y.grid(row = 2, column = 1,sticky = W)
year = OptionMenu(master, var_y_e, "2013", "2014", "2015")
year.grid(row = 2, column = 2)

label_m = Label(master, text = "Month:")
label_m.grid(row = 2, column = 3)
month = OptionMenu(master, var_m_e, *months)
month.grid(row = 2, column = 4)

label_d = Label(master, text = "Day:")
label_d.grid(row = 2, column = 5)
day = OptionMenu(master, var_d_e, *days)
day.grid(row = 2, column = 6)

def convert():
    print "Complete"
    master.quit()
	
button = Button(master, text="Convert", command=convert)
button.grid(row = 5, sticky = E)
mainloop()



