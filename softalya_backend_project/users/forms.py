from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Kullanıcı Adı',
        max_length=150,
        help_text='Gerekli. 150 karakter veya daha az. Harfler, rakamlar ve @/./+/-/_ karakterleri kabul edilir.'
    )
    password1 = forms.CharField(
        label='Şifre',
        strip=False,
        widget=forms.PasswordInput,
        help_text='Şifreniz diğer kişisel bilgilerinizle çok benzer olmamalıdır. En az 8 karakter içermelidir. Çok yaygın bir şifre olmamalıdır. Tamamen sayısal olmamalıdır.'
    )
    password2 = forms.CharField(
        label='Şifreyi Onayla',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Doğrulama için aynı şifreyi tekrar girin.'
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Eğer varsayılan kullanıcı modelini kullanılıyorsa
        fields = ('username', 'password1', 'password2')
