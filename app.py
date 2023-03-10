#IMPORTS ----------
from flask import Flask, render_template, redirect, url_for

### self-made imports
from static.info.sdg.sdg import SDG
from static.info.pb.pb import PB

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
    return render_template('pb-base.html',pb=PB)

@app.route('/modelo')
def model():
    return render_template('model-base.html')

@app.route('/tesis')
def thesis():
    return render_template('thesis-base.html')

@app.route('/onwork')
def onwork():
    return render_template('onwork.html')

@app.route('/ods/<sdg_id>')
def sdg(sdg_id):
    return render_template('specific-sdg.html',sdg=SDG[sdg_id],id=int(sdg_id))

@app.route('/limites/<limit_id>')
def limit(limit_id):
    return render_template('specific-pb.html',pb=PB[limit_id])

#MAIN ----------
def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()