from django.test import TestCase

# Create your tests here.
import time
n=10
for i in range(n):
    print('\r输出%d'%i,end='')
    time.sleep(0.5)
