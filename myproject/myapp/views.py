from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
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

  features = Feature.objects.all()
  return render(request, 'index.html', {'features': features})


def counter(request):
  text = request.POST['text']
  amount_of_words = len(text.split())
  return render(request, 'counter.html', {'amount': amount_of_words})