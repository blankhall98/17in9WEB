#IMPORTS ----------
from flask import Flask, render_template, redirect, url_for

#APP CONFIG ----------
app = Flask(__name__)

#ROUTES ----------
@app.route('/')
def index():
    return render_template('index.html')


#MAIN ----------
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()