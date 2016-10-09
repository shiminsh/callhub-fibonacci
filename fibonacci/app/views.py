from django.shortcuts import render
from app.models import Fibonacci
from django.core.cache import cache

# Create your views here.

fib_matrix = [[1,1],
              [1,0]]

def matrix_square(A, mod):
    return mat_mult(A,A,mod)


def mat_mult(A,B, mod):
  if mod is not None:
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0])%mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%mod],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%mod]]


def matrix_pow(M, power, mod):
    #Special definition for power=0:
    if power <= 0:
      return M

    powers =  list(reversed([True if i=="1" else False for i in bin(power)[2:]])) #Order is 1,2,4,8,16,...

    matrices = [None for _ in powers]
    matrices[0] = M

    for i in range(1,len(powers)):
        matrices[i] = matrix_square(matrices[i-1], mod)


    result = None

    for matrix, power in zip(matrices, powers):
        if power:
            if result is None:
                result = matrix
            else:
                result = mat_mult(result, matrix, mod)

    return result

def home(request):
    context = {}
    n = request.GET.get('fibonacci', None)
    key = str(n)
    if n:
        if cache.get(key):
            data = cache.get(key)
            context['fibonacci'] = data
        elif Fibonacci.objects.filter(number=n).exists():
            obj = Fibonacci.objects.filter(number=n)
            value = obj[0].value
            context['fibonacci'] = value
        elif int(n) < 1000000:
            a,b = 1,1
            for i in range(int(n)-1):
                a,b = b,a+b
            context['fibonacci'] = a
            data = Fibonacci(number=n, value=a)
            data.save()
            cache.set(key, str(a))
        else:
            ans = matrix_pow(fib_matrix, int(n), 1000000007)[0][1]
            context['fibonacci'] = ans
            data = Fibonacci(number=n, value=ans)
            data.save()
            cache.set(key, str(ans))
    return render(request, 'index.html', context)
