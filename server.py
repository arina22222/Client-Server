from flask import Flask, request, jsonify
import numbers;

app = Flask(__name__)

@app.route('/add', methods = ['PATCH'])

def add():
    
     
    first = request.headers.get("First","")
    second = request.headers.get("Second", " ") 

    try:
        a = int(first)        
    except  ValueError as e:
            return jsonify({"error":"'first' variable is not a number"}), 400
    
    try:
        b = int(second)        
    except  ValueError as e:
            return jsonify({"error":"'second' variable is not a number"}), 400
            
    
 

    result = a + b  
    return jsonify(result), 200 


    



@app.route('/substract', methods = ['PATCH'])
def substract():
    first = request.headers.get("First","")
    second = request.headers.get("Second", " ") 

    try:
        a = int(first)        
    except  ValueError as e:
            return jsonify({"error":"'first' variable is not a number"}), 400
    
    try:
        b = int(second)        
    except  ValueError as e:
            return jsonify({"error":"'second' variable  is not a number"}), 400
    
         

    result = int(first) - int(second)         
    return jsonify(result), 200


@app.route('/multiply', methods = ['PATCH'])
def multiply():
    first = request.headers.get("First","")
    second = request.headers.get("Second", " ") 

    try:
        a = int(first)        
    except  ValueError as e:
            return jsonify({"error":"'first' variable  is not a number"}), 400
    
    try:
        b = int(second)        
    except  ValueError as e:
            return jsonify({"error":"'second' variable  is not a number"}), 400
    
         

    result = int(first)*int(second)         
    return jsonify(result), 200

@app.route('/divide', methods = ['PATCH'])
def divide():
    first = request.headers.get("First","")
    second = request.headers.get("Second", " ") 

    try:
        a = int(first)        
    except  ValueError as e:
            return jsonify({"error":"'first' variable  is not a number"}), 400
    
    try:
        b = int(second)        
    except  ValueError as e:
            return jsonify({"error":"'second' variable  is not a number"}), 400
    

    result = int(first)/ int(second)  
               
    return jsonify(result), 200



if __name__=="__main__":
    app.run(host="127.0.0.1", port = 8080, debug = True )