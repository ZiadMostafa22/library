from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='a', password='1234'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))




app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'







@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

       
        if any(user.username == username for user in users):
            return "Username already taken!", 400

       
        new_user = User(id=len(users) + 1, username=username, password=password)
        users.append(new_user)
        return redirect(url_for('login'))  

    return render_template('signup.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)  
        
        username = request.form['username']
        password = request.form['password']

       
        user = next((x for x in users if x.username == username), None)
        
        if user and user.password == password:
           
            session['user_id'] = user.id
            return redirect(url_for('home')) 

       
        return "Invalid username or password", 400  

    return render_template('login.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/freebooks')
def freebooks():
    return render_template('freebooks.html')


@app.route('/home')
def home():
      return render_template('home.html')

@app.route('/buybooks')
def buybooks():
    return render_template('buybooks.html')

if __name__ == '__main__':
    app.run(debug=True)