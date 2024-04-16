from django.contrib import admin
from .models import Libro

# Register your models here.
admin.site.register(Libro)
# Al registrar el modelo creo un usuario con el siguiente comando
# python manage.py createsuperuser 
# USER = FaGa
# Email = fabricio.galarza@outlook.com
# Password = 1234

