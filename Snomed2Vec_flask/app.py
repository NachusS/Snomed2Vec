from flask import Flask, render_template, request
from Snomed2Vec import *

# Carga de Matrices globales con el Modelo Vectores.
w2vModel, SnomedWork = snomed2vec_load(0)
syn0, index2word, syn0norm = init_vars(SnomedWork)

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

app.run(
    host='0.0.0.0',
    port=5001,
    debug=True
)
