from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product

# Create your views here.

def IndexView(request):
    return render(request,'index.html')

def BlogView(request):
    context = Product.products.all()
    return render(request,'blog.html', {'details' : context})



def DetailView(request, slug=None):
    detail = get_object_or_404(Product,slug=slug)
    return render(request, 'blog-post.html', {'detail': detail})




