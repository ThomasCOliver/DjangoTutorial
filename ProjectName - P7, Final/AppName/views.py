from django.shortcuts import render, redirect
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse

def index(request):
	posts = Post.objects.all()
	context = {
		"posts": posts
	}
	return render(request, 'index.html', context)

def post(request):
	post = Post()
	post.text = request.POST['text']
	post.save()
	return redirect('/App/')