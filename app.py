from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Modelos
class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128))
    es_admin = db.Column(db.Boolean, default=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    eventos = db.relationship('Evento', backref='organizador', lazy=True)
    invitaciones = db.relationship('Invitacion', backref='invitado', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)
    organizador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    invitaciones = db.relationship('Invitacion', backref='evento', lazy=True)

class Invitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    email_invitado = db.Column(db.String(120), nullable=False)
    estado = db.Column(db.String(20), default='pendiente')
    fecha_respuesta = db.Column(db.DateTime, nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Decorador para verificar si el usuario es administrador
def admin_required(f):
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.es_admin:
            flash('Acceso denegado. Se requieren privilegios de administrador.')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nombre = request.form.get('nombre')
        
        if Usuario.query.filter_by(email=email).first():
            flash('El email ya está registrado')
            return redirect(url_for('registro'))
        
        usuario = Usuario(email=email, nombre=nombre)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()
        
        flash('Registro exitoso')
        return redirect(url_for('login'))
    
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)
            return redirect(url_for('dashboard'))
        
        flash('Email o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    eventos = []
    invitaciones = Invitacion.query.filter_by(usuario_id=current_user.id).all()
    
    # Si es admin, puede ver todos los eventos que ha creado
    if current_user.es_admin:
        eventos = Evento.query.filter_by(organizador_id=current_user.id).all()
    
    return render_template('dashboard.html', eventos=eventos, invitaciones=invitaciones)

@app.route('/evento/nuevo', methods=['GET', 'POST'])
@login_required
@admin_required
def nuevo_evento():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        fecha = datetime.strptime(request.form.get('fecha'), '%Y-%m-%dT%H:%M')
        ubicacion = request.form.get('ubicacion')
        
        evento = Evento(
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            ubicacion=ubicacion,
            organizador_id=current_user.id
        )
        db.session.add(evento)
        db.session.commit()
        
        flash('Evento creado exitosamente')
        return redirect(url_for('dashboard'))
    
    return render_template('nuevo_evento.html')

@app.route('/evento/<int:evento_id>/invitar', methods=['GET', 'POST'])
@login_required
@admin_required
def invitar(evento_id):
    evento = Evento.query.get_or_404(evento_id)
    if evento.organizador_id != current_user.id:
        flash('No tienes permiso para invitar a este evento')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        usuario = Usuario.query.filter_by(email=email).first()
        
        invitacion = Invitacion(
            evento_id=evento_id,
            email_invitado=email,
            usuario_id=usuario.id if usuario else None
        )
        db.session.add(invitacion)
        db.session.commit()
        
        flash('Invitación enviada exitosamente')
        return redirect(url_for('dashboard'))
    
    return render_template('invitar.html', evento=evento)

@app.route('/invitacion/<int:invitacion_id>/responder', methods=['POST'])
@login_required
def responder_invitacion(invitacion_id):
    invitacion = Invitacion.query.get_or_404(invitacion_id)
    if invitacion.usuario_id != current_user.id:
        flash('No tienes permiso para responder a esta invitación')
        return redirect(url_for('dashboard'))
    
    respuesta = request.form.get('respuesta')
    if respuesta in ['aceptado', 'rechazado']:
        invitacion.estado = respuesta
        invitacion.fecha_respuesta = datetime.now()
        db.session.commit()
        flash(f'Has {respuesta} la invitación')
    
    return redirect(url_for('dashboard'))

@app.route('/admin/invitaciones')
@login_required
@admin_required
def gestionar_invitaciones():
    # Obtener todas las invitaciones de los eventos creados por el admin
    eventos_ids = [evento.id for evento in Evento.query.filter_by(organizador_id=current_user.id).all()]
    invitaciones = Invitacion.query.filter(Invitacion.evento_id.in_(eventos_ids)).all()
    
    return render_template('admin/invitaciones.html', invitaciones=invitaciones)

@app.route('/admin/usuarios')
@login_required
@admin_required
def gestionar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('admin/usuarios.html', usuarios=usuarios)

@app.route('/admin/usuario/<int:usuario_id>/toggle-admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    if usuario.id != current_user.id:  # No permitir que un admin se quite sus propios privilegios
        usuario.es_admin = not usuario.es_admin
        db.session.commit()
        flash(f'Estado de administrador de {usuario.nombre} actualizado')
    return redirect(url_for('gestionar_usuarios'))

@app.route('/invitacion/<token>')
def ver_invitacion(token):
    # Aquí implementarías la lógica para verificar el token y mostrar la invitación
    # Por ahora, redirigimos al login
    return redirect(url_for('login'))

@app.route('/evento/<int:evento_id>/invitaciones')
@login_required
@admin_required
def gestionar_invitaciones_evento(evento_id):
    evento = Evento.query.get_or_404(evento_id)
    if evento.organizador_id != current_user.id:
        flash('No tienes permiso para gestionar las invitaciones de este evento.', 'danger')
        return redirect(url_for('dashboard'))
    
    invitaciones = Invitacion.query.filter_by(evento_id=evento_id).all()
    return render_template('admin/invitaciones_evento.html', evento=evento, invitaciones=invitaciones)

if __name__ == '__main__':
    with app.app_context():
        # Eliminar todas las tablas existentes
        db.drop_all()
        # Crear todas las tablas nuevamente
        db.create_all()
        
        # Crear un usuario administrador por defecto
        admin = Usuario(
            email='admin@george.com',
            nombre='Administrador',
            es_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        
    app.run(debug=True) 