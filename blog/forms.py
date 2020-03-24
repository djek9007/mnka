from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, help_text='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Имя*'}))
    phone = forms.IntegerField(help_text='Ваш телефон',
                               widget=forms.TextInput(attrs={'placeholder': 'Телефон*'}))
    email = forms.EmailField(help_text='email',
                             widget=forms.TextInput(attrs={'placeholder': 'Email*'}))
    message = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={'placeholder': 'Ваш запрос', 'rows':'3', }))
