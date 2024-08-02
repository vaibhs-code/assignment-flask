from flask import Flask, redirect, request , url_for , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


def login_success(name,age):
    if age>= 18:
        return("can vote")
    else:
        return("cannot vote")
    
@app.route('/login',methods =['POST','GET'])
def login():
   if request.method == 'POST':
       user= request.form['username']
       Age =int( request.form['userage'])
       return login_success(name=user,age= Age)
   #else:
      # user= request.args.get('username')
      # Age= request.args.get('userage')
      # return redirect(url_for('login_success',name= user,age=Age))
if __name__ == '__main__':
    app.run()