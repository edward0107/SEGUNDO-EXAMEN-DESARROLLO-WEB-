from django.shortcuts import render, redirect
from .models import Usuario, Video
from .forms import UsuarioForm, VideoForm

# Página de créditos
def creditos(request):
    return render(request, 'cursos/creditos.html')

# Videos
def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'cursos/videos_list.html', {'videos': videos})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos_list')
    else:
        form = VideoForm()
    return render(request, 'cursos/video_form.html', {'form': form})

# Usuarios
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cursos/usuarios_list.html', {'usuarios': usuarios})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuarioForm()
    return render(request, 'cursos/usuario_form.html', {'form': form})
