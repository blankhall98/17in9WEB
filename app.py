#IMPORTS ----------
from flask import Flask, render_template, redirect, url_for

#APP CONFIG ----------
app = Flask(__name__)

#ROUTES ----------

### main pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ods')
def sdgs():
    return render_template('sdg-base.html')

@app.route('/limites')
def limits():
    return render_template('pb-base.html')

@app.route('/modelo')
def model():
    return render_template('model-base.html')

@app.route('/tesis')
def thesis():
    return render_template('thesis-base.html')

#MAIN ----------
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()