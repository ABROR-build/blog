from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


class BlogListView(View):
    def get(self, request):
        blogs = Post.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'home.html', context=context)


class BlogCreateView(View):
    def get(self, request):
        create_form = PostForm()
        context = {
            'form': create_form
        }
        return render(request, 'post_create.html', context=context)

    def post(self, request):
        create_form = PostForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('blogs:home')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'post_create.html', context=context)


class BlogUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        update_form = PostForm(instance=post)
        context = {
            'form': update_form
        }
        return render(request, 'update.html', context=context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        update_form = PostForm(request.POST, request.FILES, instance=post)
        if update_form.is_valid():
            update_form.save()
            return redirect('blogs:home')
        else:
            context = {
                'form': update_form
            }
            return render(request, 'update.html', context=context)