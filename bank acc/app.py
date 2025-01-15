from flask import Flask, request, render_template , flash


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('index1.html')

@app.route('/welcome' ,methods=['post'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    if username == "isagi" and password == "1":
        return render_template('welcome.html')
    else:
        return render_template('404.html')
    # if username=="admin" and password=="admin":
    #     return"login successfull"
    # else:
    #     return'invalid.please try again'

    

@app.route('/check_balance', methods=[ 'post' ,'get'])
def balance_check():
    pin = request.form['pin']
    if pin == 1234:
        message =''
        balance = 1000
        name = f'{balance}'
        message = f'₹{name}'
        return render_template('balance.html' , message=message,pin=pin)


@app.route('/send', methods=['post','get'])
def send():
    return render_template('sendmoney.html')

    
@app.route('/send_money' , methods=['post','get'])
def transfer_money():
    balance = 1000
    sender = request.form['sender']
    receiver = request.form['receiver'] 
    amount = request.form['amount']
    if balance >= int(amount) :
        return render_template('paymentsuccessfully.html', sender=sender,receiver=receiver)
    else:
        return render_template('unsuccessfull.html')
    
@app.route('/accdetails')  
def acc():
    return render_template('accdetails.html')  

@app.route('/sign' , methods=['post','get'])
def out():
    return render_template('index1.html')






    


    
if __name__ == '__main__':
    app.run(debug=True)