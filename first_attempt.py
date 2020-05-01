from flask import Flask, request ,render_template
from flask_mysqldb import  MySQL
from flask import jsonify
#import yaml


app = Flask(__name__)
# configure db
#db= yaml.load(open(db.yaml))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'school'

mysql = MySQL(app)

# @app.route('/',methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        roll_stu = userDetails['roll']
        name_stu = userDetails['name12']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student_details(roll_no , name) VALUES(%s, %s)",(roll_stu, name_stu))
        result=cur.execute("SELECT LAST_INSERT_ID()")
        if result > 0:
            last_id = cur.fetchall()
        mysql.connection.commit()

        cur.close()
        return render_template('show_record.html',last_userid=last_id)
    return render_template('index.html')

@app.route('/update',methods=['GET','POST'])
def update_data():
    if request.method == 'POST':
        update_Details = request.form
        stu_id= update_Details['id']
        roll_up = update_Details['up_roll']
        name_up = update_Details['up_name12']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE student_details SET roll_no = %s,name= %s WHERE record_id = %s",(roll_up,name_up,stu_id))
        mysql.connection.commit()
        cur.close()
        return 'update successful'
    return render_template('update.html')

@app.route('/delete/<int:del_id>', methods = ['GET'])
def delete(del_id):

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student_details WHERE record_id=%s", (del_id,))
    mysql.connection.commit()
    cur.close()
    return 'success'
@app.route('/detect_prime', methods = ['GET','POST'])
def prime():
    flag=1
    if request.method== 'POST':
        prime_Details = request.form
        number_1 = prime_Details['prime']
        print(number_1)
        my_res=check_prime(int(number_1))

        # if my_res==1:
        #     return 'not prime'
        # elif my_res==2:
        #     return ' enter number greater then 1m'
        # else:
        #     return 'prime'
        dict1={number_1:my_res}
        return jsonify(dict1)

    return render_template('prime.html')




def check_prime(n):
    flag=0
    i=2
    if n>1000000:
        while i<n:
            if float(n%i)==0:
                flag=1
                print(i)
                print(n%i)
                print('not a prime')
                break
            i=i+1
        if flag==1:
            return 'not prime'
        else:
            return 'prime'
    else:
        return 'enter number greater then 1m'






if __name__ == '__main__':
    app.run(debug=True)

