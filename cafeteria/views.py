from django.shortcuts import render, redirect
from .models import Product, Event, Branch, Comment


def home(request):
    latest_products = Product.objects.all()[:3]
    context = {'products': latest_products}
    return render(request, 'cafeteria/home.html', context)


def about(request):
    return render(request, 'cafeteria/about.html')


def menu(request):
    products = Product.objects.all()
    return render(request, 'cafeteria/menu.html', {'products': products})


def events(request):
    events = Event.objects.all()
    return render(request, 'cafeteria/events.html', {'events': events})


def branches(request):
    branches = Branch.objects.all()
    return render(request, 'cafeteria/branches.html', {'branches': branches})


def comment(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        email = request.POST.get('email')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(author=author, email=email, content=content)
            return redirect('cafeteria:home')
    return render(request, 'cafeteria/comment.html')
