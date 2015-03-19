import MySQLdb
import numpy as np
import h5py

file = h5py.File("UBC_feeder.hdf5", "w")
comp_type = np.dtype([('Local Time', np.str_,19), ('Power Demand(kW)', float), ('Power Delivered(kW)', int), ('PF lag mean', float)])

db = MySQLdb.connect(host="", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 
# enter your query here
cur.execute("")

x = np.array([("0000000000000000000",1.1 ,1 , 1.1)], dtype = comp_type)

for row in cur.fetchall() :
	
	time = row[1].strftime("%Y-%m-%d %H:%M:%S")
	powerDemand = float(row[2])
	powerDelivered = row[3]
	PFLag = float(row[4])
	temp = np.array([(time, powerDemand, powerDelivered, PFLag)], dtype = comp_type)
	x = np.vstack((x,temp))
	
x = np.delete(x,0,0)

dset = file.create_dataset("mydataset", data = x, dtype = comp_type)
file.close()
