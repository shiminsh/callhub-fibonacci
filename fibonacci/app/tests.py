from django.test import TestCase
from app.models	import Fibonacci
from app.views import matrix_pow, fib_matrix

# Create your tests here.
class FibonacciTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    # test case for small number
    def test_index2(self):
        resp = self.client.get('/?fibonacci=6')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('fibonacci' in resp.context)
        self.assertEqual(resp.context['fibonacci'], 8)
    
    # test case for big number
    def test_index3(self):
        resp = self.client.get('/?fibonacci=1000000')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('fibonacci' in resp.context)
        self.assertEqual(resp.context['fibonacci'], 918091266)


     # models test
    def create_fibonacci(self, number="10", value="55"):
        return Fibonacci.objects.create(number=number, value=value)

    def test_fibonacci_creation(self):
        f = self.create_fibonacci()
        self.assertTrue(isinstance(f, Fibonacci))
        self.assertEqual(f.__unicode__(), f.number)

    # views function test case
    def test_views_function(self):
    	data = matrix_pow(fib_matrix, int(10000000), 1000000007)[0][1]
    	print data
    	self.assertEqual(data, 490189494)
