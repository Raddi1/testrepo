import time
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from Auto.forms import ProductForm, RegistrationUserForm
from .models import Product, User


def caches(request):
    cache.set('key', 'value', timeout=60)
    for i in range(100):
        print(cache.get('key'))
        time.sleep(1)

        return HttpResponse("Cache set successfully!")




def index(request):
    visits = int(request.COOKIES.get('visit_count', 0))
    products = Product.objects.all()
    context = {
        'products': products,
        'stars': range(1, 6),
        'visits': visits + 1
    }
    response = render(request, 'Auto/index.html', context)
    response.set_cookie('visits', visits + 1, max_age=3600)
    return response


def add_pr(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, template_name='Auto/add.html', context={'form': form})


def register(request):
    if request.method == 'GET':
        form = RegistrationUserForm()
        return render(request, 'Auto/register.html', {'form': form})
    
    try:
        form = RegistrationUserForm(request.POST)
    except Exception as e:
        print(f"MEssage Error: {e}")

    if form.is_valid():
        user = form.save(commit=False)
        user.name = form.data['name']
        user.email = form.data['email']
        user.save
        return render(request, 'Auto/index.html', {'user': user})
    
    form = RegistrationUserForm()
    return render(request, 'Auto/reg.html', {'form': form})


def login(request):
    user = User.objects.get(id=1)
    login(request, user)
    return render(request, 'Auto/index.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def mail(request):
    send_mail(
        subject='test email',
        message='text message.',
        html_message= render_to_string('Auto/email_template.html'),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['xznoall@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Успішно відправлено!")
