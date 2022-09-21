## Projecto de Ripio

### Tecnologias usadas
- Django
- Django rest framework
- React
- Docker
- PostgreSQL

### Pasos para levantar el proyecto
- Tener docker / docker-compose instalado
- Situar una terminal en la raiz del proyecto (al nivel de docker-compose.yml)
- Ejecutar el comando *docker-compose up --build* (o *docker-compose up* si es la primera vez)
- Ejecutar comando *docker exec ripio_backend python manage.py migrate* para correr las migraciones
- Crear usuarios para probar el sistema (mediante admin de django o mediante *docker exec -ti ripio_backend python manage.py createsuperuser* la primera vez, da igual que sea superusuario)
    - nota: cada vez que se crea un usuario / moneda, se iniciaran wallets con balance 5, para realizar pruebas

### Urls

- localhost:3000 - Frontend
- localhost:8000 - API backend
- localhost:8000/admin - Admin de django. Util para crear usuarios y demas modelos
- localhost:8000/swagger - Documentacion de API con todos los endpoints