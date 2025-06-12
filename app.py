from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/health')
def health():
    return 'Server is up and running'
app.run(debug=True, host='0.0.0.0', port=80)
