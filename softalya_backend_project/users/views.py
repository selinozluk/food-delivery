from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Address
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Özel formu buraya import ediyoruz
from django.contrib.auth.forms import AuthenticationForm

# Ana Sayfa (Home) Fonksiyonu
def home(request):
    return render(request, 'home.html')

# Kullanıcı Kayıt (Register) Fonksiyonu
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız oluşturuldu, {username}! Giriş yapabilirsiniz.')
            auth_login(request, user)  # Kayıt olduktan sonra otomatik giriş
            return redirect('home')  # Kayıt sonrası ana sayfaya yönlendirme
        else:
            messages.error(request, 'Kayıt işleminde bir hata oluştu.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Kullanıcı Giriş (Login) Fonksiyonu
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Tekrar hoş geldiniz, {user.username}!')
            return redirect('home')  # Ana sayfaya yönlendirme
        else:
            messages.error(request, 'Giriş bilgileri hatalı, lütfen tekrar deneyin.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Adres Ekleme Fonksiyonu
@login_required
def add_address(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')
        user = request.user

        Address.objects.create(
            name=name,
            last_name=last_name,
            phone_number=phone_number,
            description=description,
            user=user
        )
        messages.success(request, 'Adres başarıyla eklendi!')
        return redirect('get_addresses')  # Adresleri görüntüleme sayfasına yönlendirme
    return JsonResponse({"error": "Invalid method"}, status=405)

# Adresleri Getirme Fonksiyonu
@login_required
def get_addresses(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'users/addresses.html', {'addresses': addresses})  # Şablona yönlendirme

# Adres Güncelleme Fonksiyonu
@login_required
def update_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)
    if request.method == 'POST':
        address.name = request.POST.get('name', address.name)
        address.last_name = request.POST.get('last_name', address.last_name)
        address.phone_number = request.POST.get('phone_number', address.phone_number)
        address.description = request.POST.get('description', address.description)
        address.save()
        messages.success(request, 'Adres başarıyla güncellendi!')
        return redirect('get_addresses')  # Güncelleme sonrası adres sayfasına yönlendirme
    return JsonResponse({"error": "Invalid method"}, status=405)

# Adres Silme Fonksiyonu
@login_required
def delete_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)
    if request.method == 'POST':  # Form ile silme işlemi
        address.delete()
        messages.success(request, 'Adres başarıyla silindi!')
        return redirect('get_addresses')  # Silme sonrası adres sayfasına yönlendirme
    return JsonResponse({"error": "Invalid method"}, status=405)
