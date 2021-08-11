from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s'% name

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['username']
        #password = request.form('password')
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get['username']
       # password = request.args.get('passsword')
        return redirect(url_for('success',name = user))

@app.route('/log')
def page():
    return render_template('login.html')

@app.route('/main')
def mainn():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    return render_template('result.html',marks= score)

@app.route('/marks')
def marks():
    dict1 = {'physics':60,'chemistry':70,'maths':90}
    #print(dict1)
    return render_template('marks.html',marks=dict1)

if __name__ == '__main__':
    app.run(debug=True)