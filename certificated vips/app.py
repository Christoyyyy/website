from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='vips'
    )

@app.route('/')
def wel():
    return render_template('index.html', user_details=None, message="")

@app.route('/get_user_details', methods=['GET'])
def get_user_details():
    certificate_number = request.args.get('certificate_number')

    if not certificate_number:
        return render_template('index.html', user_details=None, message="Certificate number is required")

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # Fetch results as dictionary

        # Query to fetch user details based on certificate number
        query = """
        SELECT name, phone_number, email, domain, start_date, end_date
        FROM certificates
        WHERE certificate_number = %s
        """

        cursor.execute(query, (certificate_number,))
        result = cursor.fetchone()

        if result:
            user_details = {
                "name": result["name"],
                "phone_number": result["phone_number"],
                "email": result["email"],
                "domain": result["domain"],
                "start_date": result["start_date"],
                "end_date": result["end_date"],
            }
            return render_template('index.html', user_details=user_details, message="")
        else:
            return render_template('index.html', user_details=None, message="Certificate number not found")

    except mysql.connector.Error as err:
        return render_template('index.html', user_details=None, message=f"Database error: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
