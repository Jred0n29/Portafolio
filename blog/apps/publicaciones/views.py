from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Post

#Lsitado de posts por fuera de la vista para hacer una sola consulta


def Home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post':post})

def Publicaciones(request,id):
    print(99999999999999999999)
    print(id)
    post = Post.objects.get(id = id)
    print(post.imagen)
    return render(request, 'texto.html', {'post':post} )