from flask import Flask, request, jsonify,render_template
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',       
        user='root',    
        password='root',
        database='vips' 
    )
    return conn
@app.route('/')
def wel():
    return render_template('index.html')

@app.route('/get_user_details', methods=['GET'])
def get_user_details():
    certificate_number = request.args.get('certificate_number')
    
    if not certificate_number:
        return jsonify({"error": "Certificate number is required"}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to fetch user details based on certificate number
        query = """
        SELECT name, phone_number, email, course_name, course_completion_date
        FROM certificates
        WHERE certificate_number = %s
        """
        
        cursor.execute(query, (certificate_number,))
        result = cursor.fetchone()

        # Check if the result is found
        if result:
            user_details = {
                "name": result[0],
                "phone_number": result[1],
                "email": result[2],
                "course_name": result[3],
                "course_completion_date": result[4].strftime('%Y-%m-%d')  
            }
            return jsonify(user_details)
        else:
            return jsonify({"error": "Certificate number not found"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500
    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
