from django.shortcuts import render
from blog_main.forms import RegistrationForm
from blogs.models import Category
from blogs.models import Blog
from about_us.models import About



def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status = 'Published')

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