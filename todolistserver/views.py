from django.shortcuts import render
# Create your views here.
def index(request):
    print 'jump to index'
    request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'index.html')