from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render,redirect
from django.contrib import messages
from mysite import settings

def homepage(request):
    return render(request, 'myapp/homepage.html')

def excursions(request):
    return render(request, 'myapp/excursions.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            fcd = form.cleaned_data
            Name = fcd['Name']
            content = fcd['content']
            email = fcd['email']
            mail = send_mail(f' Тема: Экскурсии', f'Имя клиента: {Name}\nПочта клиента: {email}\n\n{content}', settings.EMAIL_HOST_USER, settings.RECIPIENT_EMAIL, fail_silently=False)
            if mail == True:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contacts')
            else:
                messages.error(request, 'Ошибка отправки' )
        else:
             messages.error(request, 'Форма невалидна' )
    else:
        form = ContactForm()
    return render(request, 'myapp/contacts.html', {"form": form})

def galery(request):
    return render(request, 'myapp/galery.html')


    

    
