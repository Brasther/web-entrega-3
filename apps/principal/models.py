from django.db import models
from django.contrib.auth.models import User  #
from django.db import models, IntegrityError

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        txt = "Nombre: {0} - Id: {1}"
        return txt.format(self.nombre_categoria,self.id_categoria)

class Producto(models.Model):
    sku = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen_url = models.ImageField(upload_to='imagenesProducto')

    def __str__(self):
        txt = "N° {0} - Stock: {1} - nombre: {2}"
        return txt.format(self.sku,self.stock, self.nombre)




class Envio(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre_envio = models.CharField(max_length=50)
    correo = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        txt = "Rut: {0} - Nombre: {1} "
        return txt.format(self.rut,self.nombre_envio)    
    
#-----------------------------------


    