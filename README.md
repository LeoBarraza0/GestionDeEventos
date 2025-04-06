# Sistema de Gestión de Eventos

Una aplicación web desarrollada con Flask para la gestión de eventos e invitaciones.

## Características

- Registro y autenticación de usuarios
- Creación y gestión de eventos
- Sistema de invitaciones
- Interfaz intuitiva y responsive
- Pruebas automatizadas

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd sistema-gestion-eventos
```

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Iniciar la aplicación:
```bash
python app.py
```

2. Abrir el navegador y acceder a:
```
http://localhost:5000
```

## Pruebas

Para ejecutar las pruebas:
```bash
pytest tests.py
```

## Estructura del Proyecto

```
sistema-gestion-eventos/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── tests.py           # Pruebas
├── templates/         # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── registro.html
│   ├── dashboard.html
│   └── nuevo_evento.html
└── README.md
```

## Seguridad

- Las contraseñas se almacenan de forma segura usando hash
- Protección contra CSRF en formularios
- Autenticación requerida para rutas protegidas
- Validación de datos de entrada

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 