#pip install flask 
from flask import Flask,render_template

# initilise the app
app=Flask(__name__)     #any name you can give

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/input")
def blog():
    return render_template('input.html')

@app.route("/contact_us")
def gallary():
    return render_template('contact.html')

#run the app
app.run(debug=True)    #debug=True is for auto update of server