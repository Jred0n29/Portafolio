from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

class Autor(models.Model):
    id = models.AutoField(primary_key=True,blank=False,null=False)
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellido = models.CharField(max_length=50,blank=False,null=False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250,blank=False,null=False)
    contenido = RichTextField()
    frase = RichTextField()
    resumen = models.CharField(max_length=250,blank=False,null=False)
    tema = models.CharField(max_length=250,blank=False,null=False)
    autor_id = models.ForeignKey(Autor,on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(blank=False,null=False)
    imagen = models.ImageField(upload_to="imagenes",  blank=True,null=True)
    estado = models.BooleanField(blank=False,null=False)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo