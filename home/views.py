from django.shortcuts import render
from . models import *
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

# c = Count(like = 0, dislike = 0)
# c.save()

class Home(View):

    def get(self, request, *args, **kwargs):
        count = Count.objects.get(pk=1)
        # print(count[0])
        like = count.like
        dislike = count.dislike 
        return render(request, 'home/index.html', {'like' : like, 'dislike' : dislike})


class IncLike(View):
    def post(self, request, *args, **kwargs):
        count = Count.objects.get(pk =1)
        count.like = count.like+1
        count.save()
        return render(request, 'home/index.html', {'like' : count.like, 'dislike' : count.dislike})

class IncDisike(View):
    def post(self, request, *args, **kwargs):
        count = Count.objects.get(pk =1)
        count.dislike = count.dislike+1
        count.save()
        return render(request, 'home/index.html', {'like' : count.like, 'dislike' : count.dislike})
      

