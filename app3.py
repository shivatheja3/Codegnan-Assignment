from flask import Flask,request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db1=SQLAlchemy(app)


class myapp(db1.Model):
     sno=db1.Column(db1.Integer,primary_key=True)
     Sname=db1.Column(db1.String(100))
     Scollege=db1.Column(db1.String(100))
     
     def __repr__(self) -> str:
          return f"{self.sno}-{self.Sname}"




@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        college=request.form['college']
        todo=myapp(name=name,college=college)
        db.session.add(todo)
        db.session.commit()    
    allTodo=myapp.query.all()
    #print(allTodo)
    return render_template('index.html',allTodo=allTodo)

@app.route('/update')
def something():
    allTodo=myapp.query.all()
    print(allTodo)
    return 'something'
@app.route('/delete/<int:sno>')
def delete(sno):
    odo=myapp.query.filter_by(sno=sno).first()
    db.session.delete(odo)
    db.session.commit() 
    return redirect("/")



if __name__ == '__main__':
    app.run(debug=True)