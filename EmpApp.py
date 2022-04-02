from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'employee'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('www.intellipaat.com')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    date = request.form['currentDate1']
    time = request.form['currentTime1']
 

    insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s)"
    cursor = db_conn.cursor()

    cursor.execute(insert_sql, (emp_id, first_name, date, time))
    db_conn.commit()
    emp_num = emp_id
    emp_name = first_name
    date_now = date
    timenow = time

    cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name, id = emp_num, date_1 = date_now, time_1 =timenow )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
