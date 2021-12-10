from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField(label='*Ваше имя', min_length=2, widget=forms.TextInput(attrs={"class": "form-control name", "placeholder":"Введите имя"}), required=True)
    email = forms.EmailField(label='*Ваш е-mail', min_length=5, widget=forms.EmailInput(attrs={"class": "form-control letter", "placeholder":"Введите почту"}), required=True)
    content = forms.CharField(label='*Текст', min_length=5, widget=forms.Textarea(attrs={"class": "form-control text", "rows": 5, "placeholder":"Введите текст"}), required=True)

