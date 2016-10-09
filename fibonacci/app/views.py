from django.shortcuts import render
from app.models import Fibonacci

# Create your views here.

def home(request):
    context = {}
    N = request.GET.get('fibonacci', None)
    if N:
        if Fibonacci.objects.filter(number=N).exists():
            obj = Fibonacci.objects.filter(number=N)
            print "existsexistsexistsexistsexists"
            value = obj[0].value
            context['fibonacci'] = value
            print context
        else:
            a,b = 1,1
            for i in range(int(N)-1):
                a,b = b,a+b
            context['fibonacci'] = a
            data = Fibonacci(number=N, value=a)
            data.save()
            print context
    return render(request, 'index.html', context)
    