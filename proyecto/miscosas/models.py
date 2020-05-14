from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.contrib.postgres.fields import ArrayField

tamano = {'pequena': 30,
            'mediana': 40,
            'grande': 50}

estilous = {'oscuro': {'color_letra': 'white', 'fondo_cabec': 'fondo_cabecera_oscuro.jpg',
                        'fondo': 'fondo_oscuro.jpg'},
            'ligero': {'color_letra': 'black', 'fondo_cabec': 'fondo_cabecera2.jpg',
                        'fondo': 'fondo.jpg'}}
# Create your models here.
class Alimentador(models.Model):
    tipo = models.CharField(max_length=10, default="")
    nombre = models.CharField(max_length=64)
    enlace = models.TextField(default="") #al canal o al subreddit
    elegido = models.BooleanField(default=True)
    id_canal = models.CharField(max_length=64, default="")
    #en el caso del reddit sera igual al nombre del subrredit

    def __str__(self):
        return self.nombre

    def count_likes(self):
        count = 0
        for item in self.item_set.all():
            count = item.count_likes() + count
        return count

    def total_it(self):
        return self.item_set.all().count()



#class LastAlim(Alimentador):

# class estiloPag(models.Model):
#     color_letra = models.CharField(max_length=10)
#     fondo_cabec = models.CharField(max_length=20)

class PagUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="img_users")
    tamLetra =  models.CharField(max_length=10, default='mediana')
    estilo = models.CharField(default='ligero', max_length=100)
    #alimentadores = ArrayField(ArrayField(Alimentador))


class Item(models.Model):
    titulo = models.CharField(max_length=64)
    enlace = models.TextField()
    descrip = models.TextField()
    alimentador =  models.ForeignKey(Alimentador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def count_likes(self):
        count = 0
        for like in self.like_set.all():
            count = like.boton + count
        return count

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)
    texto =  models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return "Comentario del item:"+self.item.titulo


class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    boton = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "Like de "+ self.usuario.username +" en el item: "+self.item.titulo
