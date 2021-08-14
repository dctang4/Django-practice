from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
  features = Feature.objects.all()
  return render(request, 'index.html', {'features': features})

  # name = 'Jack'
  # context = {
  #   'name': 'Patrick',
  #   'age': 23,
  #   'nationality': 'British'
  # }
  # return render(request, 'index.html', context)

  # feature1 = Feature()
  # feature1.id = 0
  # feature1.name = 'Fast'
  # feature1.is_true = True
  # feature1.details = 'Our service is very quick'

  # feature2 = Feature()
  # feature2.id = 1
  # feature2.name = 'Reliable'
  # feature2.is_true = True
  # feature2.details = 'Our service is very reliable'

  # feature3 = Feature()
  # feature3.id = 2
  # feature3.name = 'Easy To Use'
  # feature3.is_true = False
  # feature3.details = 'Our service is very easy to use'

  # feature4 = Feature()
  # feature4.id = 3
  # feature4.name = 'Affordable'
  # feature4.is_true = True
  # feature4.details = 'Our service is very affordable'

  # feature5 = Feature()
  # feature5.id = 4
  # feature5.name = 'Trustworthy'
  # feature5.is_true = False
  # feature5.details = 'Our service is very trustworthy'

  # features = [feature1, feature2, feature3, feature4]

  # return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2, 'feature3': feature3, 'feature4': feature4})

def counter(request):
  posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
  return render(request, 'counter.html', {'posts': posts})
  # text = request.POST['text']
  # amount_of_words = len(text.split())
  # return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Already Used')
        return redirect('register')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username Already Used')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else: 
      messages.info(request, 'Password Not the Same')
      return redirect('register')

  else:
    return render(request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password =request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Credentials Invalid')
      return redirect('login')

  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/')

def post(request, pk):
  return render(request, 'post.html', {'pk': pk})