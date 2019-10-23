from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def Cadastro(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()

        data_cadastro = Cadastro()
        data_cadastro.usuario = data_usuario
        data_cadastro.Nome = request.POST['nome']
        data_cadastro.Sobrenome = request.POST['sobrenome']
        data_cadastro.Endereco = request.POST['endereco']
        data_cadastro.save()

        args = {
            'sucesso': 'Cadastro efetuado com sucesso.'
        }

        return render(request, 'login.html', args)

    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        formulario_email = request.POST['email']
        formulario_senha = request.POST['senha']

        usuario_logado = Cadastro.objects.filter(usuario__email = formulario_email,
                                              usuario__senha = formulario_senha).first()

        if usuario_logado is not None:
            args = {
                'dados': usuario_logado
            }
            return render(request, 'index.html', args)
        else:
            args = {
                'msg': 'Credenciais inválidas, tente novamente.'
            }
            return render(request, 'login.html', args)

    return render(request, 'login.html')