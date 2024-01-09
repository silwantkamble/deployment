#pip install flask 
from flask import Flask

# initilise the app
app=Flask(__name__)     #any name you can give

@app.route("/")
def home():
    return "hello, how are you"



@app.route("/blogs")
def blog():
    return "welcome to the home pages"

@app.route("/contact_us")
def gallary():
    return "please contact on phone:87961626xx , and email:xyz@gmail.com"

#run the app
app.run(debug=True)    #debug=True is for auto update of server