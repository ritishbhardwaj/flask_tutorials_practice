from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
    return "hello world hi"

# from controller import user_controller,product_controller
from controller import *
 

if __name__ == "__main__":
    app.run(debug=True)

