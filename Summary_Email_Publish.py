import datetime
import pandas as pd
from EMAIL_SENDING_SAMPLE import *
#import mysql.connector as condb

#conn = condb.connect(host="localhost",user="yuva",passwd="yuva",database="yuva")
from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://yuva:yuva@127.0.0.1/yuva')

# mycursor = conn.cursor()

# mycursor.execute("select * from employee")

# result = mycursor.fetchall()

sql_df = pd.read_sql('SELECT * FROM employee', engine)

print(sql_df.loc[0,'emp_name':'hire_date'])

body_text = "<h2>Employee Details</h2><table><tr><td>EmpId</td><td>Emp name</td><td>Hire Date</td></tr>"
#print(body_text)
print(len(sql_df.index))
for i in range(0,len(sql_df.index)):
	body_text = body_text + f"<tr><td>{sql_df.loc[i,'emp_id']}</td><td>{sql_df.loc[i,'emp_name']}</td><td>{sql_df.loc[i,'hire_date']}</td></tr>"

body_text = body_text + "</table>"
print(body_text)
notify_user(subject="Status for today", body=body_text)