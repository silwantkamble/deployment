#pip install flask 
from flask import Flask

# initilise the app
app=Flask(__name__)     #any name you can give

@app.route("/")
def home():
    return "hello, how are you"
#run the app
app.run()