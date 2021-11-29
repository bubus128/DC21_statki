from django import forms


class MailForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=50)
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=500)
