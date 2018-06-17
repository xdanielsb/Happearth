from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from accounts.admin import UserCreationFormExtended
from django.core.mail import EmailMultiAlternatives 
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext

def signup(request):
  if request.user.is_superuser == False:
    return render(request, 'accounts/not_access_granted.html')
  if request.method == 'POST':
    form = UserCreationFormExtended(request.POST)
    if form.is_valid():
      user = form.save()
      mail_subject = 'Energy Monitor Application' 
      to_email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      user.email = to_email
      user.save()
      message = render_to_string('accounts/acc_content_message.html', {
        'user': user,
        'content': content,
      })
      email = EmailMultiAlternatives(
        mail_subject,
        message, 
        to=[to_email]
      )
      email.content_subtype = "html"
      email.send()
      return HttpResponse('The user {} was created succesufully. The email was sent to {}. '.format(user.username, user.email))
    return render(request, 'accounts/signup.html', {'form': form })
  else:
    form = UserCreationFormExtended()
    return render(request, 'accounts/signup.html', {'form': form})

class SearchView(ListView):
  template_name = "accounts/list.html"
  model = User

def handler404(request):
    response = render(request, 'accounts/404.html', {})
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'accounts/500.html', {})
    response.status_code = 500
    return response
