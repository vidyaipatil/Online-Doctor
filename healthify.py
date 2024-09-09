from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'healthify.com'



def check_login():
    email = None
    password = None
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        if((email == 'rudra@healthify.com' and password  == 'rudra123') or
           (email == 'bhagyashri@healthify.com' and password  == 'bhagu123') or
           (email == 'vidya@healthify.com' and password  == 'vidya123')):
            splitted_email = email.split('@')
            username = splitted_email[0].capitalize
            return (render_template(('m3.html'),name = username))
        else:
            alert_message = "Your login credentials are wrong!!! Try again"
            return render_template('m2.html', alert_message=alert_message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def loginpage():
    # previous_page = request.headers.get('Referer')
    
    return render_template('m1.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    return render_template('m2.html')

@app.route('/checkup', methods = ['GET', 'POST'])
def checkup():
    email = None
    password = None
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        if((email == 'rudra@healthify.com' and password  == 'rudra123') or
           (email == 'bhagyashri@healthify.com' and password  == 'bhagu123') or
           (email == 'vidya@healthify.com' and password  == 'vidya123')):
            splitted_email = email.split('@')
            username = splitted_email[0]
            return (render_template(('m3.html'),name = username))
        else:
            alert_message = "Your login credentials are wrong!!! Try again"
            return render_template(('m1.html'), alert_message=alert_message)

@app.route('/result')
def display_result():
    pass

    




if __name__ == "__main__":
    app.run(debug=True)