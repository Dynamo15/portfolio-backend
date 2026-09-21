# Portfolio Backend

API REST para el perfil público del portafolio, enlaces sociales y tecnologías.

## Requisitos

- Python 3.13 o superior
- PostgreSQL

## Configuración

1. Crea y activa un entorno virtual.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Copia `.env.example` a `.env` y completa las credenciales de PostgreSQL.
4. Inicia el servidor con `uvicorn app.main:app --reload`.

La aplicación crea las tablas al arrancar y asegura un único Profile inicial que
puede actualizarse con `PUT /profile/`.

Para desarrollo, React/Vite está permitido desde `http://localhost:5173`. Para
agregar orígenes, define `CORS_ORIGINS` en `.env` como una lista separada por
comas, por ejemplo: `http://localhost:5173,https://example.com`.

## Documentación

Con el servidor activo, Swagger está disponible en `http://localhost:8000/docs`.

Los recursos terminados son:

- `GET` y `PUT /profile/`
- CRUD de `/social-links/`
- CRUD de `/skills/`

Projects permanece intencionalmente pendiente de diseño e implementación.
