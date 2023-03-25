from flask import Flask, render_template
app = Flask(__name__)

#En la función return render_template(‘index.html’)

@app.route("/")
def student_webpage():
    #Crear una variable
    name = 'Rodrigo'
    # Pasar la variable en la plantilla
    return render_template('website.html', student_name = name)
app.run(debug=True)