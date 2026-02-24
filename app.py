import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def crear_tabla():
    conexion = sqlite3.connect("database/juegos.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            asunto TEXT,
            mensaje TEXT
        )
    """)

    conexion.commit()
    conexion.close()

# EJECUTAR LA CREACION DE TABLA
crear_tabla()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar():

    nombre = request.form["nombre"]
    correo = request.form["correo"]
    asunto = request.form["asunto"]
    mensaje = request.form["mensaje"]

    conexion = sqlite3.connect("database/juegos.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO mensajes (nombre, correo, asunto, mensaje) VALUES (?, ?, ?, ?)",
        (nombre, correo, asunto, mensaje)
    )

    conexion.commit()
    conexion.close()

    return redirect("/")

@app.route("/admin/mensajes")
def ver_mensajes():
    import sqlite3
    conexion = sqlite3.connect("database/juegos.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, correo, asunto, mensaje FROM mensajes ORDER BY id DESC")
    datos = cursor.fetchall()

    conexion.close()

    return render_template("mensajes.html", mensajes=datos)


    
if __name__ == "__main__":
    app.run(debug=True)


