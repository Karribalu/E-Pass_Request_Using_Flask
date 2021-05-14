from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = 'Bala Subramanyam'
    return render_template('Index.html', title='Welcome', username=name)

if __name__ == '__main__':
    app.run()