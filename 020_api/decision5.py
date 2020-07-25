from __future__ import print_function	# For Py2/3 compatibility
import eel
from flask import Flask
import requests
app = Flask(__name__)
@app.route("/",methods=['GET'])
def predict12():
    # Set web files folder
    eel.init('')
    @eel.expose  # Expose this function to Javascript
    def say_hello_py():
        fram1 = requests.get('http://0.0.0.0:5001/')
        return fram1
    say_hello_py()
    eel.myFunction()  # Call a Javascript function
    print(eel.myFunction())
    #print(type(eel.myFunction()))
    eel.start('hello.html')
    response = app.response_class(
        response=eel.myFunction() ,
        status=200
    )
    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

