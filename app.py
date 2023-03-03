from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + lastname
        if firstname and lastname:
            return jsonify({'output': 'Your Name is ' + output + ', right?'})
        return jsonify({'error': 'Missing data!'})

    return render_template('index.html')


@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == "POST":
        a = request.form['a']
        b = request.form['b']
        c = float(a) + float(b)
        if a and b:
            return jsonify({'c':  c})
        return jsonify({'error': 'Missing data!'})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
