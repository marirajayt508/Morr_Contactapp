from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="contacts"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#Loading Home Page

@app.route("/",methods=['GET','POST'])
def cntd():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("index.html",datas=res)

@app.route("/userus/<string:id>",methods=['GET','POST'])
def update1(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        sql="update users set name=%s,email=%s where id=%s"
        con.execute(sql,[name,email,id])
        mysql.connection.commit()
        con.close()
    return render_template("print.html")

@app.route("/set",methods=['GET','POST'])
def set():
    return render_template("adduser.html")
    
@app.route("/delt/<string:id>",methods=['GET','POST'])
def delt(id):
    con=mysql.connection.cursor()
    sql="delete from users where id=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return render_template("condel.html")



@app.route("/update/<string:id>",methods=['GET','POST'])
def update(id):
     con=mysql.connection.cursor()
     sql="SELECT * FROM users WHERE id=%s"
     con.execute(sql,[id])
     res=con.fetchall()
     return render_template("update.html",datas=res)


@app.route("/adduser",methods=['GET','POST'])
def print():
    if request.method=='POST':
       name=request.form['name']
       email=request.form['email']
       con=mysql.connection.cursor()
       sql="insert into users (name,email) value (%s,%s)"
       con.execute(sql,[name,email])
       mysql.connection.commit()
       con.close()   
    return render_template("addsuccess.html")   

@app.route("/search",methods=['GET','POST'])
def srch():
    if request.method=='POST':
       srch=request.form['srch']
       con=mysql.connection.cursor()
       sql="SELECT * FROM users WHERE name=%s || email=%s"
       con.execute(sql,[srch,srch])
       res=con.fetchall()
    return render_template("search.html",email=res)  

    
if(__name__=='__main__'):
    app.run(debug=True)
