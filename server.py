from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  
fruits = ['strawberry', 'raspberry', 'blackberry', 'apple']
total=0

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout(fruits=fruits,total=total):
    
    dt_string = datetime.now().strftime("%B %d %Y %H:%M:%S")
    c_fruits=[]

    for fruit in fruits:
        
        if int(form_dict[fruit]) > 0:
            total += int(form_dict[fruit])
            c_fruits.append(fruit)
            
    print(request.form)
    print(f"Charging {form_dict['first_name']} {form_dict['last_name']} for {total} fruits")
    return render_template("checkout.html" ,fruits=c_fruits, total=total, date = dt_string)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    