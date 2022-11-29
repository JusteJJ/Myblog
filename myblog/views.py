from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['proclaim_date']

class ArticlesDetailView(DetailView):
	model = Post
	template_name = 'articles.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'addarticle.html'
	#fields = '__all__'
	#fields = ('author','title', 'body')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'addcategory.html'
	fields = '__all__'
	#fields = ('author','title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'editpost.html'
	#fields = ['title', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'deletearticle.html'
	success_url = reverse_lazy('home')