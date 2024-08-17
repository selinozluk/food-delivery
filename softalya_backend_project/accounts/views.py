from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Kullanıcı Kayıt
def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        mobile = request.POST['mobile']

        user = User(name=name, address=address, email=email, password=password, mobile=mobile)
        user.save()
        return redirect('signin')  # Kayıttan sonra giriş sayfasına yönlendirme
    return render(request, 'accounts/signup.html')

# Kullanıcı Giriş
def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Başarılı giriş işlemi
                return redirect('homepage')  # Anasayfaya yönlendirme
            else:
                return render(request, 'accounts/signin.html', {'error': 'Geçersiz şifre'})
        except User.DoesNotExist:
            return render(request, 'accounts/signin.html', {'error': 'Kullanıcı bulunamadı'})
    return render(request, 'accounts/signin.html')

# Anasayfa Görüntüleme
def homepage_view(request):
    return render(request, 'accounts/homepage.html')
