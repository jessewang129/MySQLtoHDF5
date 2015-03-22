import MySQLdb
import numpy as np
import h5py
from Tkinter import *

master = Tk()

var_l = StringVar(master)
var_l.set("Kaiser Alpha Lab") 
var_y_s = StringVar(master)
var_y_s.set("2015")
var_m_s = StringVar(master)
var_m_s.set("01")
var_d_s = StringVar(master)
var_d_s.set("01")
var_y_e = StringVar(master)
var_y_e.set("2015")
var_m_e = StringVar(master)
var_m_e.set("01")
var_d_e = StringVar(master)
var_d_e.set("01")

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
months = ["01"]
for m in range (2, 13):
	if m < 10:
		months.append("0"+str(m))
	else:
		months.append(m)
		
month = OptionMenu(master, var_m_s, *months)
month.grid(row = 1, column = 4)

label_d = Label(master, text = "Day:")
label_d.grid(row = 1, column = 5)
days = ["01"]
for d in range(2, 32):
	if d< 10:
		days.append("0"+str(d))
	else: 
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
    
	file = h5py.File("Armada.hdf5", "w")
	comp_type = np.dtype([('Equipment Id', int), ('Time', np.str_,19), ('Average value', float), ('Max value', float), ('Mmin value', float)])
	
	db = MySQLdb.connect(host="Jesse-PC", # your host, usually localhost
                     user="Jesse", # your username
                      passwd="1234", # your password
                      db="armada") # name of the data base
	cur = db.cursor()
	
	if var_l.get() == "Kaiser Alpha Lab":
		site_id = 7		
	elif var_l.get() == "Kaiser Utiilty-AMPS80":
		site_id = 4
	elif var_l.get() == "LMRS-AMPS225":
		site_id = 6
	elif var_l.get() == "LMRS-AMPS80":
		site_id = 1
	elif var_l.get() == "NCE-AMPS80":
		site_id = 8
		
	start_date = "'"+str(var_y_s.get())+str(var_m_s.get())+str(var_d_s.get())+"000000'"
	end_date = "'"+str(var_y_e.get())+str(var_m_e.get())+str(var_d_e.get())+"000000'"
	
	x = np.array([(1,"0000000000000000000", 1.0, 1.0, 1.0)], dtype = comp_type)
	query = "SELECT e.equ_id, timestamp, average_value, max_value, min_value FROM equ_equipment e,equ_data_record_day d WHERE e.site_location_id ="+str(site_id)+" AND e.equ_id = d.equ_id AND timestamp >= "+start_date+" AND timestamp <= "+end_date
	print query
	cur.execute(query)
	
	for row in cur.fetchall() :
		equ_id = row[0]
		time = row[1].strftime("%Y-%m-%d %H:%M:%S")
		average = float(row[2])
		max = float(row[3])
		min = float(row[4])
		temp = np.array([(equ_id, time, average, max, min)], dtype = comp_type)
		x = np.vstack((x,temp))
	
	x = np.delete(x,0,0)
	
	dset = file.create_dataset(str(var_l.get()), data = x, dtype = comp_type)
	file.close()
	print "Complete"
	master.quit()
    
	
button = Button(master, text="Convert", command=convert)
button.grid(row = 5, sticky = E)
mainloop()



