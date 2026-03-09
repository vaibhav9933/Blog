from django.shortcuts import render,redirect
from blog_main.forms import RegistrationForm
from blogs.models import Category
from blogs.models import Blog
from about_us.models import About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect

def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published', slug__isnull=False).exclude(slug='').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published', slug__isnull=False).exclude(slug='')

    #Fetching about us
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        # 'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request,'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can also log the user in immediately after registration if desired
            # from django.contrib.auth import login
            # login(request, user)
            return render(request, 'register.html', {'form': RegistrationForm(), 'success': True})
        else:
            print("Form is not valid")
    else:
        form = RegistrationForm()
    context={
        'form': form,
    }
    return render(request,'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'login.html', context)


def logout_view(request):
    """Log the user out and redirect to home."""
    auth.logout(request)
    return redirect('home')