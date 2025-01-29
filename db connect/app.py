from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for flash messages

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'root',  # Replace with your MySQL password
    'database': 'vips'  # The database name
}

# Route for the index page (register page)
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Check if the email already exists
            cursor.execute("SELECT * FROM login WHERE email = %s", (email,))
            if cursor.fetchone():
                flash('Email already registered. Please login.', 'error')
                return redirect('/')

            # Insert the new user into the database
            cursor.execute("INSERT INTO login (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, password))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect('/login')
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'error')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()    

    return render_template('reg.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Validate email and password
            cursor.execute("SELECT * FROM login WHERE email = %s AND password = %s", (email, password))
            user = cursor.fetchone()
            if user:
                return render_template('details.html')
               
            else:
                flash('Access denied. Invalid email or password.', 'error')
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'error')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()    
       
                
       

    return render_template('login.html')

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        age= request.form['age']


        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Validate email and password
            cursor.execute("INSERT INTO details (name, phone, age) VALUES (%s, %s, %s)", 
                           (name, phone, age))
            conn.commit()
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'error')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
        return redirect('/details')

    return render_template('details.html')


if __name__ == '__main__':
    app.run(debug=True)

