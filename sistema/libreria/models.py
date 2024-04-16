from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True, )
    descripcion = models.TextField(null=True, verbose_name="Descripción")
    #Despues de crear el modelo se corre la siguiente instrucción
    # python manage.py makemigrations
    # luego se corre el siguiente comnado
    # python manage.py magrate

    # Se muestra información del libro en el admin
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripción:" + self.descripcion
        return fila

    # Borra la imagen de un libro
    def delete(self, using=None, keep_parents=False):
        #Borra imagen fisica de la carpeta S
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
