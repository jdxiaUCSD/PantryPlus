from flask import Flask, url_for, render_template, session, request, flash, redirect

app = Flask(__name__, template_folder = 'templates', static_folder= 'static', static_url_path= '/')
app.secret_key = 'Some Key'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        if (username == 'Jayden' and password == 'Xia'):
            flash('Login Successful!')
            return render_template('dashboard.html', username = username)
        else: flash('Login Failed')
    return render_template('login.html')

@app.route('/log_out')
def log_out():
    session.pop('_flashes', None)
    flash('Logout Successful')
    return redirect(url_for('login'))


if __name__ == '__main__':
    #Host, port, debug mode
    #Debug allow the app deployment to update automatically
    app.run(host='0.0.0.0', port=5006, debug=True)