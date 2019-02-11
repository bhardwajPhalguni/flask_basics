#cookies and session.......

from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape

app = Flask(__name__)
app.secret_key = 'abcdeffgaaaaaaaaaaaaaaaaaaaaaaaaa'

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        print("======{}=======".format(request.form))
        user = request.form['nm']
        age = request.form.get('age')
        print("=============age========{}".format(age))
        resp = make_response(render_template('readcookie.html', user=user, age = age))
        resp.set_cookie('userID', user)
        resp.set_cookie('Age', age)
        return resp
    else:
        print("==============a============")
        return redirect(url_for('index'))

@app.route('/getcookie', methods=['GET'])
def getcookie():
    print ("=====request.cookies======", request.cookies)
    name = request.cookies.get('userID')
    age = request.cookies.get('Age')
    return '<h1>welcome ' + name + '.</h1>' + '<h2> Your age is ' + age + '</h2>'

@app.route('/session/')
def index_session():
    print ("======session=======", session)
    cookies = request.cookies
    print ("==========cookies====", cookies)
    if 'username' in session:
        print ("==================session---a========")
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/session/logout'>click here to log out</a></b>"
    print ("==================session===b========")
    return "You are not logged in <br><a href = '/session/login/'></b>" + \
           "click here to log in</b></a>"

@app.route('/session/login/', methods=['GET', 'POST'])
def session_login():
    if request.method == 'POST':
        cookies = request.cookies
        print ("===login=======cookies====", cookies)
        print ("==================session_login===a=====", request.form)
        session['username'] = request.form['username']
        print ("==================session=====")
        return redirect(url_for('index_session'))
    print ("==================session_login===b=====")
    return '''

   <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p<<input type = submit value = Login /></p>
   </form>

   '''


@app.route('/session/logout')
def session_logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index_session'))

if __name__ == '__main__':
    app.run(debug=True)