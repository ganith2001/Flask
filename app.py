from flask import Flask, render_template,request,json
import os


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home',methods=['POST'])
def hello_world():
    f=request.files['file']
    f.save(os.path.join('C:/Users/Ganith/Desktop/Ganith/Flask/data','input.txt'))
    data=request.form

    with open('data/metadata','w') as f:
        json.dump(data,f,indent=4)
    return data

if __name__ == "__main__":
    app.run(debug=True)