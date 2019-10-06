from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index(name=None):
    # return "hello world"
    return render_template('index.html', name=None)

if __name__ == "__main__":
    app.run(debug=True)
