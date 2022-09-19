from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.secret_key="Secret Key"

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/crudOperations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db1=SQLAlchemy(app)

class Data(db1.Model):
     id1=db1.Column(db1.Integer,primary_key=True)
     Sname=db1.Column(db1.String(100))
     Scollege=db1.Column(db1.String(100))
     
     def __init__(self,name,college):
          self.name=name
          self.college=college
     
     
@app.route("/",methods=['GET','POST'])
def index():
     if request.method=='POST':
          userDetails=request.formname
          name=userDetails['name']
          email=userDetails['college']
     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)