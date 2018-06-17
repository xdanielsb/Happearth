from django.shortcuts import render
from django.views.generic import TemplateView
from house.models import  House
from house.forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string
from django.shortcuts import redirect

class VList(TemplateView):
  template_name = 'house/list.html'
  def get_context_data(self, *args, **kwargs):
    houses = House.objects.all()
    return {'houses': houses}

class VConfirm(TemplateView):
  template_name = 'house/message_confirmation.html'

def vEmail(request, to=""):
  if request.user.is_superuser == False:
    return render(request, 'accounts/not_access_granted.html')
  if request.method == "POST":
    form  = ContactForm(request.POST)
    if form.is_valid() :
      to_email = form.cleaned_data.get('email')
      content = form.cleaned_data.get('content')
      who = form.cleaned_data.get('who')
      payload = "from =  {},  to = {},  content = {}".format(who, to_email, content)
      mail_subject = 'Energy Monitor Application' 
      to_email = form.cleaned_data.get('email')
      message = render_to_string('accounts/acc_content_message.html', {
        'user': to,
        'domain': "https://github.com/xdanielsb"
      })
      email = EmailMultiAlternatives(
        mail_subject,
        message, 
        to=[to_email]
      )
      email.content_subtype = "html"
      email.send()
      return redirect("house:confirm")
    return render( request, 'house/sent-email.html', {
        'form': form
    })
  return render( request, 'house/sent-email.html', {
    'form': ContactForm(initial={'email': to})
  })

