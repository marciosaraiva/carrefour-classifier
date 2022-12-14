from flask import Flask, request
import project_functions as pf

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Marcio! Try to access my site: <a href=http://marciosaraiva.pythonanywhere.com/classify?url=link </a>'

@app.route('/classify')
def run_classification():
    try:
        url = request.args.get("url")
        classification = pf.get_classification(url)
        return {"Classification": classification}
    except Exception as e:
        detail = str(e)
        return {"Error": "Impossible to classify",
                "Error detail": detail}
