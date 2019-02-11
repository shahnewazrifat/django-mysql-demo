from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Hello, from DevSpaces!</h2> <br><a href='/admin'>Login</a>")
