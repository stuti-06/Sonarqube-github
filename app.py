from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def home():
    """
    home fun
    """
    return "<h1>Welcome to Home page<h1/>"
 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
has context menu
