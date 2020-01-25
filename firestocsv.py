import sqlite3

conn = sqlite3.connect('FPA_FOD_20170508.sqlite')

#to export as csv file
with open("fires_class.csv", "w") as write_file:
	c = conn.cursor()
	i = 0
	write_file.write("STAT_CAUSE_CODE, DISCOVERY_DOY, DISCOVERY_DATE, LATITUDE, LONGITUDE, FIRE_SIZE_CLASS\n")
	for row in c.execute("SELECT STAT_CAUSE_CODE, DISCOVERY_DOY, DISCOVERY_DATE, LATITUDE, LONGITUDE, FIRE_SIZE_CLASS FROM Fires"):
		writeRow = ",".join([str(a) for a in row])
		write_file.write(writeRow+"\n")
		i += 1
          