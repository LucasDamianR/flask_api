# coding: utf-8
from flask import Flask
from flask import request
import numpy as np
import datetime
import pyodbc
import pandas as pd
import numpy as np
import json
import time
import os
import math


app = Flask(__name__)
#
@app.route('/sumar', methods=['POST','GET'])
def sumar():
    #EDIT 
    
    data = request.get_json()
    A = data["a"]
    B = data["b"] 
    resultado = f"La suma de {A} + {B} es = {A+B}"
    return resultado


@app.route('/mul', methods=['POST','GET'])
def mul():
    #EDIT 
    
    data = request.get_json()
    A = data["a"]
    B = data["b"]
    resultado = f"La multiplicación entre {A} * {B} es = {A*B}"
    return resultado


@app.route('/divi', methods=['POST','GET'])
def divide():
    #EDIT 
    
    data = request.get_json()
    A = data["a"]
    B = data["b"]
    if B == 0 : return f"No se puede dividir por cero ({A} /{B})"
    resultado = f"La división entre {A} / {B} es = {A/B}"
    return resultado



@app.route('/restar', methods=['POST','GET'])
def restar():
    #EDIT 
    
    data = request.get_json()
    
    A = data["a"]
    B = data["b"]
    resultado = f"La resta de {A} - {B} es = {A-B}"
    return resultado


@app.route('/pow', methods=['POST','GET'])
def pote():
    #EDIT 
    
    data = request.get_json()
    
    A = data["a"]
    
    resultado = f" Cuadrados perfectos {[i**2 for i in A]}"
    
    return resultado

@app.route('/raiz',methods=['POST','GET'])
def raiz():
    data = request.get_json()
    
    A = data["a"]

    return f" Raíces cuadradas {[math.sqrt(i) for i in A]}"
    

    
    


if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)
    
#app.run()

