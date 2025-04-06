import unittest
from app import app, db, Usuario, Evento, Invitacion
from datetime import datetime, timedelta
from flask_login import login_user, logout_user
import json

class EventFlowTests(unittest.TestCase):
    def setUp(self):
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        # Crear contexto de aplicación
        with app.app_context():
            # Eliminar y recrear la base de datos
            db.drop_all()
            db.create_all()
            
            # Crear usuario administrador de prueba
            admin = Usuario(
                email='admin@test.com',
                nombre='Admin Test',
                es_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Crear usuario normal de prueba
            usuario = Usuario(
                email='usuario@test.com',
                nombre='Usuario Test',
                es_admin=False
            )
            usuario.set_password('usuario123')
            db.session.add(usuario)
            
            db.session.commit()
            
            # Guardar IDs para uso posterior
            self.admin_id = admin.id
            self.usuario_id = usuario.id

    def tearDown(self):
        # Limpiar después de las pruebas
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def login_admin(self):
        # Iniciar sesión como administrador
        return self.app.post('/login', data={
            'email': 'admin@test.com',
            'password': 'admin123'
        }, follow_redirects=True)

    def login_usuario(self):
        # Iniciar sesión como usuario normal
        return self.app.post('/login', data={
            'email': 'usuario@test.com',
            'password': 'usuario123'
        }, follow_redirects=True)

    def logout(self):
        # Cerrar sesión
        return self.app.get('/logout', follow_redirects=True)

    # 1. PRUEBAS DE FUNCIONALIDAD PRINCIPAL

    def test_crear_evento(self):
        """Prueba la creación de un evento por un administrador"""
        self.login_admin()
        
        # Crear un evento
        fecha_evento = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M')
        response = self.app.post('/evento/nuevo', data={
            'titulo': 'Evento de Prueba',
            'descripcion': 'Descripción del evento de prueba',
            'fecha': fecha_evento,
            'ubicacion': 'Ubicación de prueba'
        }, follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que el evento se haya creado en la base de datos
        with app.app_context():
            evento = Evento.query.filter_by(titulo='Evento de Prueba').first()
            self.assertIsNotNone(evento)
            self.assertEqual(evento.descripcion, 'Descripción del evento de prueba')
            self.assertEqual(evento.ubicacion, 'Ubicación de prueba')
            self.assertEqual(evento.organizador_id, self.admin_id)
            
            # Guardar el ID del evento para pruebas posteriores
            self.evento_id = evento.id

    def test_invitar_usuario(self):
        """Prueba el envío de invitaciones a usuarios"""
        # Primero crear un evento
        self.test_crear_evento()
        
        # Enviar invitación
        response = self.app.post(f'/evento/{self.evento_id}/invitar', data={
            'email': 'usuario@test.com'
        }, follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que la invitación se haya creado
        with app.app_context():
            invitacion = Invitacion.query.filter_by(
                evento_id=self.evento_id,
                email_invitado='usuario@test.com'
            ).first()
            self.assertIsNotNone(invitacion)
            self.assertEqual(invitacion.estado, 'pendiente')
            self.assertEqual(invitacion.usuario_id, self.usuario_id)
            
            # Guardar el ID de la invitación para pruebas posteriores
            self.invitacion_id = invitacion.id

    def test_responder_invitacion(self):
        """Prueba la respuesta a una invitación"""
        # Primero crear un evento e invitar a un usuario
        self.test_invitar_usuario()
        
        # Cerrar sesión de admin e iniciar sesión como usuario normal
        self.logout()
        self.login_usuario()
        
        # Aceptar la invitación
        response = self.app.post(f'/invitacion/{self.invitacion_id}/responder', data={
            'respuesta': 'aceptado'
        }, follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que la invitación se haya actualizado
        with app.app_context():
            invitacion = Invitacion.query.get(self.invitacion_id)
            self.assertEqual(invitacion.estado, 'aceptado')
            self.assertIsNotNone(invitacion.fecha_respuesta)

    # 2. PRUEBAS DE USABILIDAD

    def test_acceso_dashboard_sin_login(self):
        """Prueba que no se pueda acceder al dashboard sin iniciar sesión"""
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija a la página de login
        self.assertIn('Iniciar Sesion'.encode('utf-8'), response.data)

    def test_acceso_evento_admin_sin_permiso(self):
        """Prueba que un usuario normal no pueda acceder a funciones de administrador"""
        # Crear un evento como admin
        self.test_crear_evento()
        
        # Cerrar sesión de admin e iniciar sesión como usuario normal
        self.logout()
        self.login_usuario()
        
        # Intentar acceder a la gestión de invitaciones del evento
        response = self.app.get(f'/evento/{self.evento_id}/invitaciones', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija al dashboard con mensaje de error
        self.assertIn('No tienes permiso'.encode('utf-8'), response.data)

    def test_navegacion_intuitiva(self):
        """Prueba que la navegación sea intuitiva para diferentes tipos de usuarios"""
        # Probar navegación para usuario normal
        self.login_usuario()
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que no aparezcan opciones de administrador
        self.assertNotIn('Gestionar Usuarios'.encode('utf-8'), response.data)
        
        # Probar navegación para administrador
        self.logout()
        self.login_admin()
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que aparezcan todas las opciones de administrador
        self.assertIn('Gestionar Usuarios'.encode('utf-8'), response.data)
        self.assertIn('Gestionar Invitaciones'.encode('utf-8'), response.data)

    # 3. PRUEBAS DE SEGURIDAD

    def test_proteccion_contraseña(self):
        """Prueba que las contraseñas estén protegidas"""
        with app.app_context():
            # Obtener el usuario admin
            admin = Usuario.query.get(self.admin_id)
            # Verificar que la contraseña no esté almacenada en texto plano
            self.assertNotEqual(admin.password_hash, 'admin123')
            # Verificar que la verificación de contraseña funcione
            self.assertTrue(admin.check_password('admin123'))
            self.assertFalse(admin.check_password('contraseña_incorrecta'))

    def test_acceso_no_autorizado(self):
        """Prueba que no se pueda acceder a rutas protegidas sin autenticación"""
        # Intentar acceder a la gestión de usuarios sin iniciar sesión
        response = self.app.get('/admin/usuarios', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija a la página de login
        self.assertIn('Iniciar Sesion'.encode('utf-8'), response.data)
        
        # Iniciar sesión como usuario normal
        self.login_usuario()
        
        # Intentar acceder a la gestión de usuarios como usuario normal
        response = self.app.get('/admin/usuarios', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija al dashboard con mensaje de error
        self.assertIn('Acceso denegado'.encode('utf-8'), response.data)

    def test_proteccion_datos_usuario(self):
        """Prueba que los datos del usuario estén protegidos"""
        # Crear un evento como admin
        self.test_crear_evento()
        
        # Cerrar sesión de admin e iniciar sesión como usuario normal
        self.logout()
        self.login_usuario()
        
        # Intentar acceder a los datos del evento como usuario normal
        response = self.app.get(f'/evento/{self.evento_id}/invitaciones', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija al dashboard con mensaje de error
        self.assertIn('No tienes permiso'.encode('utf-8'), response.data)

    def test_csrf_proteccion(self):
        """Prueba la protección CSRF en formularios"""
        # Habilitar CSRF para esta prueba
        app.config['WTF_CSRF_ENABLED'] = True
        
        # Iniciar sesión como admin
        self.login_admin()
        
        # Intentar crear un evento sin token CSRF
        fecha_evento = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M')
        response = self.app.post('/evento/nuevo', data={
            'titulo': 'Evento sin CSRF',
            'descripcion': 'Descripción del evento',
            'fecha': fecha_evento,
            'ubicacion': 'Ubicación'
        }, follow_redirects=True)
        
        # Verificar que la solicitud sea rechazada
        self.assertEqual(response.status_code, 400)
        
        # Deshabilitar CSRF nuevamente para otras pruebas
        app.config['WTF_CSRF_ENABLED'] = False

if __name__ == '__main__':
    unittest.main() 