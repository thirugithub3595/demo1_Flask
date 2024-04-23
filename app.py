#this is configuration file 

from flask import Flask # this is a flask package 

app=Flask(__name__)

@app.route('/')#default api view function
def home():
    return "this is home"


@app.route('/s2s/api/signup')
def user_signup():
    return "this is signup page"



if __name__ =="__main__":
    app.run(debug=True)
