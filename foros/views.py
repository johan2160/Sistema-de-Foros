from django.shortcuts import render

# La página del index variará según el tipo de usuario y su estado de registro.
def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarLogin(request):
    return render(request, 'login.html')

def mostrarSignup(request):
    return render(request, 'signup.html')

def mostrarPerfilUsuario(request):
    return render(request, 'perfil_usuario.html')

def mostrarEditarPerfilUsuario(request):
    return render(request, 'editar_perfil_usuario.html')

def mostrarForo(request):
    return render(request, 'ver_foro.html')

def mostrarCrearComentario(request):
    return render(request, 'crear_comentario.html')

def mostrarEditarComentario(request):
    return render(request, 'editar_comentario.html')

def mostrarCrearForo(request):
    return render(request, 'crear_foro.html')

def mostrarEditarForo(request):
    return render(request, 'editar_foro.html')

def mostrarCrearTematica(request):
    return render(request, 'crear_tematica.html')

def mostrarEditarTematica(request):
    return render(request, 'editar_tematica.html')

def mostrarGestionarUsuario(request):
    return render(request, 'gestionar_usuario.html')

def mostrarHistorialAcciones(request):
    return render(request, 'historial_acciones.html')