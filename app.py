from flask import Flask,render_template,request
from model import get_response,predict_class
import json
app=Flask(__name__)
intents = json.loads(open("intents.json").read())
   
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def bot_response():
    userTxt=request.args.get('msg')
    
    ints=predict_class(userTxt)
    return get_response(ints,intents)

if __name__=='__main__':
    app.run(debug=True)