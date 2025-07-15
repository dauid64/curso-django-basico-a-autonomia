from django.http import HttpResponse

def index(request):
    return HttpResponse(
        """
            <h1>Bem vindo ao Blog!</h1>
        """
    )