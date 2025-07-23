from django.shortcuts import render

PROJETOS = [
    {
        "titulo": "Projeto 1",
        "descricao": "Descrição do Projeto 1",
        "link": "#",
        "imagem": "/static/blog/img/projeto.png"
    },
    {
        "titulo": "Projeto 2",
        "descricao": "Descrição do Projeto 2",
        "link": "#",
        "imagem": "/static/blog/img/projeto.png"
    },
    {
        "titulo": "Projeto 3",
        "descricao": "Descrição do Projeto 3",
        "link": "#",
        "imagem": "/static/blog/img/projeto.png"
    }
]

def index(request):
    title_page = "Página principal"
    return render(request, 'blog/index.html', {
        "title_page": title_page,
        "projetos": PROJETOS
    })