from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Base de datos
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)

# Modelo
class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

# Rutas
@app.route('/')
def listar():
    personas = Session().query(Persona).all()
    return render_template('listar.html', personas=personas)

@app.route('/mostrar/<int:id>')
def mostrar(id):
    persona = Session().query(Persona).filter_by(id=id).first()
    return render_template('mostrar.html', persona=persona)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        persona = Persona(nombre=nombre, apellido=apellido)
        Session().add(persona)
        Session().commit()
        return redirect(url_for('listar'))
    return render_template('crear.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = Session().query(Persona).filter_by(id=id).first()
    if request.method == 'POST':
        persona.nombre = request.form['nombre']
        persona.apellido = request.form['apellido']
        Session().commit()
        return redirect(url_for('listar'))
    return render_template('editar.html', persona=persona)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Session().query(Persona).filter_by(id=id).first()
    Session().delete(persona)
    Session().commit()
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)
