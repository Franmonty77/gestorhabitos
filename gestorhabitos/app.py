from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)

#Ruta de inicio de la página
@app.route("/")
def inicio():
    return "<h1>Bienvenido al gestor de hábitos</h1><a href='/nuevo'>Añadir nuevo hábito</a>"

#Ruta para crear nuevo hábito
@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_habito():
    mensaje=""
    if request.method=="POST":
        nombre_habito=request.form["nombre_habito"]
        conexion=sqlite3.connect("habitos.db")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO habitos (nombre) VALUES (?)",(nombre_habito,))
        conexion.commit()
        conexion.close()
        mensaje="Hábito guardado correctamente"
    return render_template("nuevo.html",mensaje=mensaje)

    #Visualizar habitos
@app.route("/habitos")
def ver_habitos():
    conn = sqlite3.connect("habitos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habitos")
    habitos = cursor.fetchall()
    conn.close()
    return render_template("habitos.html", habitos=habitos)


#Linea necesario para ver si esta siendo ejecutado correctamente
if __name__ == "__main__":
    app.run(debug=True)
