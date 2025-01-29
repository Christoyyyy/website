from flask import Flask, render_template, request, jsonify
import razorpay

app = Flask(__name__)

# Razorpay API credentials
RAZORPAY_KEY_ID = "rzp_test_d8q1G8gHxnECjw"
RAZORPAY_KEY_SECRET = "mq9m6hU9H6UGZxnZP84OrTsR"

# Razorpay client instance
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


@app.route('/')
def home():
    return render_template('index.html', key_id=RAZORPAY_KEY_ID)


@app.route('/create_order', methods=['POST'])
def create_order():
    try:
        amount = int(request.form['amount']) * 100  # Convert to paise
        currency = "INR"
        receipt = "receipt_1"

        # Create Razorpay order
        order = razorpay_client.order.create({
            "amount": amount,
            "currency": currency,
            "receipt": receipt,
            "payment_capture": 1  # Automatic capture
        })

        return jsonify(order)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/payment_success', methods=['POST'])
def payment_success():
    try:
        payment_id = request.form['razorpay_payment_id']
        order_id = request.form['razorpay_order_id']
        signature = request.form['razorpay_signature']

        # Verify the payment signature
        razorpay_client.utility.verify_payment_signature({
            "razorpay_order_id": order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature
        })

        return "Payment successful!"
    except Exception as e:
        return f"Payment verification failed: {str(e)}", 400


if __name__ == '__main__':
    app.run(debug=True)
