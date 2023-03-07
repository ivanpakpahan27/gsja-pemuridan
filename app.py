from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index():    
    return render_template('beranda.html')

if __name__ == '__main__':
    app.run(debug=True)
