from flask import Flask, render_template,request,json
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/fileupload',methods=['POST'])
def fileupload():
    f=request.files['file']
    f.save(os.path.join('C:/Users/Ganith/Desktop/Ganith/Flask/data','input.txt'))
    data=request.form

    with open('data/metadata','w') as f:
        json.dump(data,f,indent=4)
    return data

if __name__ == "__main__":
    app.run(debug=True)