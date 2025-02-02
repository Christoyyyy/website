from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send the email using EmailJS
    try:
        emailjs.send_form(
            service_id="service_4uznzkm",  # Replace with your service ID
            template_id="template_42gxubi",  # Replace with your template ID
            form_data=request.form
        )
        return jsonify({"message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
