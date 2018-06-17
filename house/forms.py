from django import forms

class ContactForm(forms.Form):
  who  = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  content = forms.CharField(
      required=True,
      widget=forms.Textarea
  )
  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['who'].label = "Support Staff Name"
    self.fields['email'].label = "To"
    self.fields['content'].label = "Write here the message"
