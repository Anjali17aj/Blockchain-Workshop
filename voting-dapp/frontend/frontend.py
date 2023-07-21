from flask import Flask, render_template,request,redirect,session

app=Flask(__name__) #flask object

@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port=5002,
        debug=True
    )