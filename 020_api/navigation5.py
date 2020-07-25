#perception -> Decision ->Navigation
from flask import Flask
import requests
import time

#r = requests.post('https://httpbin.org/post', data = {'key':'value'})
#print(r.text)
from pismart.amateur import PiSmart
from time import sleep
def setup():
global my_pismart
my_pismart= PiSmart()
# If one of the motor is reversed, change its False to True
my_pismart.MotorA_reversed = False
my_pismart.MotorA_reversed = False
def end():
my_pismart.end()
def loop():
my_pismart.MotorA = 60 # Set MotorA speed 60

r = requests.get('http://0.0.0.0:5002/envoyerMsg')
print("request received from decision module at ")
reqdecision=time.time()
print(reqdecision)
print(r.text)
a=float(r.text)
print(a)

print("temps d'envoi d'une requete from decision to navigation")
reqdecnav=reqdecision-a
#print(reqdecnav)

app = Flask(__name__)

execdecision = requests.get('http://0.0.0.0:5002/envoyerMsg1')
reqperceptiondeci = requests.get('http://0.0.0.0:5002/envoyerMsg2')


@app.route('/')
def hello_world():
    return "hello from navigation module"



c=float(reqperceptiondeci.text)
d=float(execdecision.text)

print("req from perception to decision")
print(c)
print("execution decision")
print(d)
print("req from decision to navigation")
print(reqdecnav)

print("temps d'execution de chemin total")
print(c+d+reqdecnav)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)