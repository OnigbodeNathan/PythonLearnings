import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt
plt.show()
conn = sqlite3.connect('northwind.db')
cur = conn.cursor()
 
cur.execute('''SELECT * FROM employee''')
 
row = cur.fetchall()
#pd.read_sql_table('employee', sqlite3.connect('northwind.db'))
#pd.read_sql('northwind.db', conn)
#pd.read_html(io.StringIO('pom'))
calender =pd.read_csv("C:/Users/CWSLPT1/Downloads/Calendar.csv")
calender
calender.plot(figsize = (12,6))
pd.rev 
conn.close()