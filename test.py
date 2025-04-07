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
            db.session.remove()
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
            db.session.close()

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

    def test_modificar_evento(self):
        """Prueba la modificación de un evento existente"""
        # Primero crear un evento
        self.test_crear_evento()
        
        # Modificar el evento
        fecha_modificada = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%dT%H:%M')
        response = self.app.post(f'/evento/{self.evento_id}/editar', data={
            'titulo': 'Evento Modificado',
            'descripcion': 'Nueva descripción del evento',
            'fecha': fecha_modificada,
            'ubicacion': 'Nueva ubicación'
        }, follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que el evento se haya modificado
        with app.app_context():
            evento = Evento.query.get(self.evento_id)
            self.assertEqual(evento.titulo, 'Evento Modificado')
            self.assertEqual(evento.descripcion, 'Nueva descripción del evento')
            self.assertEqual(evento.ubicacion, 'Nueva ubicación')

    def test_cancelar_evento(self):
        """Prueba la cancelación de un evento"""
        # Primero crear un evento
        self.test_crear_evento()
        
        # Cancelar el evento
        response = self.app.post(f'/evento/{self.evento_id}/cancelar', follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que el evento se haya cancelado
        with app.app_context():
            evento = Evento.query.get(self.evento_id)
            self.assertEqual(evento.estado, 'cancelado')
            
            # Verificar que las invitaciones se hayan actualizado
            invitaciones = Invitacion.query.filter_by(evento_id=self.evento_id).all()
            for invitacion in invitaciones:
                self.assertEqual(invitacion.estado, 'cancelado')

    def test_listar_eventos(self):
        """Prueba el listado de eventos"""
        self.login_admin()
        
        # Crear varios eventos
        fechas = [
            datetime.now() + timedelta(days=i)
            for i in range(1, 4)
        ]
        
        eventos_creados = []
        for i, fecha in enumerate(fechas, 1):
            response = self.app.post('/evento/nuevo', data={
                'titulo': f'Evento {i}',
                'descripcion': f'Descripción del evento {i}',
                'fecha': fecha.strftime('%Y-%m-%dT%H:%M'),
                'ubicacion': f'Ubicación {i}'
            }, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            eventos_creados.append(f'Evento {i}')
        
        # Obtener listado de eventos
        response = self.app.get('/eventos', follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que todos los eventos creados estén en la lista
        for titulo in eventos_creados:
            self.assertIn(titulo.encode('utf-8'), response.data)

    def test_buscar_eventos(self):
        """Prueba la búsqueda de eventos"""
        self.login_admin()
        
        # Crear eventos con diferentes características
        eventos = [
            {
                'titulo': 'Conferencia Tech',
                'descripcion': 'Evento sobre tecnología',
                'fecha': (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%dT%H:%M'),
                'ubicacion': 'Sala A'
            },
            {
                'titulo': 'Workshop de Python',
                'descripcion': 'Taller práctico de programación',
                'fecha': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M'),
                'ubicacion': 'Sala B'
            }
        ]
        
        for evento in eventos:
            response = self.app.post('/evento/nuevo', data=evento, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
        
        # Realizar búsqueda por término
        response = self.app.get('/eventos/buscar?q=Python', follow_redirects=True)
        
        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Verificar que solo aparezca el evento de Python
        self.assertIn('Workshop de Python'.encode('utf-8'), response.data)
        self.assertNotIn('Conferencia Tech'.encode('utf-8'), response.data)

    # 2. PRUEBAS DE USABILIDAD

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
        """Prueba TC-012: Protección de Contraseñas"""
        with app.app_context():
            # Obtener el usuario admin
            admin = Usuario.query.get(self.admin_id)
            # Verificar que la contraseña no esté almacenada en texto plano
            self.assertNotEqual(admin.password_hash, 'admin123')
            # Verificar que la verificación de contraseña funcione
            self.assertTrue(admin.check_password('admin123'))
            self.assertFalse(admin.check_password('contraseña_incorrecta'))

    def test_acceso_no_autorizado(self):
        """Prueba TC-013: Control de Acceso"""
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
        """Prueba TC-015: Protección de Datos de Usuario"""
        # Iniciar sesión como usuario normal
        self.login_usuario()
        
        # Intentar acceder a los datos de otro usuario
        response = self.app.get(f'/usuario/{self.admin_id}/perfil', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se redirija al dashboard con mensaje de error
        self.assertIn('Acceso denegado'.encode('utf-8'), response.data)
        
        # Verificar que solo se muestren los datos del usuario actual
        response = self.app.get(f'/usuario/{self.usuario_id}/perfil', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verificar que se muestren los datos del usuario actual
        self.assertIn('Usuario Test'.encode('utf-8'), response.data)
        
        # Verificar que los datos sensibles estén protegidos
        self.assertNotIn('usuario123'.encode('utf-8'), response.data)

    def test_csrf_proteccion(self):
        """Prueba TC-014: Protección CSRF"""
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