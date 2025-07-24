from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session to work

def init_db():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()

        # Drop the table if it already exists (only for development)
        cur.execute("DROP TABLE IF EXISTS providers")

        # Recreate the providers table with a password column
        cur.execute('''CREATE TABLE providers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            service TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')

        # Create other tables (only if they don’t already exist)
        cur.execute('''CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY,
            customer_name TEXT,
            service TEXT,
            provider_id INTEGER,
            date TEXT
        )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY,
            booking_id INTEGER,
            rating INTEGER,
            comment TEXT
        )''')
init_db()

# Sample service requests (for service provider homepage)
service_requests = [
    {"customer_name": "Rahul", "details": "Need help fixing ceiling fan"},
    {"customer_name": "Neha", "details": "AC repair required"},
]

# Home
@app.route('/')
def role_selection():
    return render_template('role_selection.html')

@app.route('/home')
def index():
    return render_template("index.html")

# Register Service Provider
@app.route('/register_service_provider', methods=["GET", "POST"])
def register_service_provider():
    if request.method == "POST":
        name = request.form['name']
        service = request.form['service']
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("database.db") as con:
            con.execute("INSERT INTO providers (name, service, email, password) VALUES (?, ?, ?, ?)",
                        (name, service, email, password))

        return render_template('service_provider_homepage.html',
                               name=name, email=email,
                               service=service, requests=service_requests)
    return render_template("register_service_provider.html")

# Register Customer
@app.route('/register_customer', methods=['GET', 'POST'])
def register_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Optionally save customer to DB here
        session['name'] = name
        session['email'] = email
        return render_template('customer_homepage.html')
    return render_template('register_customer.html')


# Customer Homepage
@app.route('/customer_homepage')
def customer_homepage():
    return render_template('customer_homepage.html')


# Profile
@app.route('/profile')
def profile():
    # Replace with actual user fetching logic
    user = {
        'name': session.get('name'),  # Assuming stored in session after login
        'email': session.get('email'),
        'phone': '1234567890',
        'address': '123 Main Street'
    }
    return render_template('profile.html', user=user)

# Update Profile
@app.route('/update_profile', methods=['POST'])
def update_profile():
    # logic to update user's info
    # (extract from request.form and save to database)
    return redirect(url_for('profile'))


# Book a Service
@app.route('/book', methods=["GET", "POST"])
def book():
    if request.method == "POST":
        customer = request.form['customer']
        service = request.form['service']
        provider_id = request.form['provider_id']
        date = request.form['date']
        with sqlite3.connect("database.db") as con:
            con.execute("INSERT INTO bookings (customer_name, service, provider_id, date) VALUES (?, ?, ?, ?)",
                        (customer, service, provider_id, date))
        return redirect("/")
    providers = sqlite3.connect("database.db").cursor().execute("SELECT * FROM providers").fetchall()
    return render_template("booking.html", providers=providers)

# Leave Feedback
@app.route('/feedback', methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        booking_id = request.form['booking_id']
        rating = request.form['rating']
        comment = request.form['comment']
        with sqlite3.connect("database.db") as con:
            con.execute("INSERT INTO feedbacks (booking_id, rating, comment) VALUES (?, ?, ?)",
                        (booking_id, rating, comment))
        return redirect("/")
    bookings = sqlite3.connect("database.db").cursor().execute("SELECT * FROM bookings").fetchall()
    return render_template("feedback.html", bookings=bookings)

# Admin Dashboard
# @app.route('/admin')
# def admin():
#     db = sqlite3.connect("database.db")
#     cur = db.cursor()
#     providers = cur.execute("SELECT * FROM providers").fetchall()
#     bookings = cur.execute("SELECT * FROM bookings").fetchall()
#     feedbacks = cur.execute("SELECT * FROM feedbacks").fetchall()
#     return render_template("admin.html", providers=providers, bookings=bookings, feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
