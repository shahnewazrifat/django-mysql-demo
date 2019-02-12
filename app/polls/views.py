from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2 align='center'>Your app and DevSpace are running in the CLOWD!</h2> <div align='center'><a href='/admin'>Login</a></div>")
