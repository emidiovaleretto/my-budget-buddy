from allauth.account.forms import LoginForm, SignupForm
from django import forms


class CustomLoginForm(LoginForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your username',
        })

        self.fields['login'].label = "Username"

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your password',
        })
        self.fields['password'].label = "Password"

        self.fields['remember'].widget = forms.CheckboxInput(attrs={
            'class': 'checkbox',
        })
        self.fields['remember'].label = "Remember me"

    def label_tag(self, name, label_suffix=None, attrs=None):
        label_attrs = {'class': 'label'}
        if attrs:
            label_attrs.update(attrs)
        return super(CustomLoginForm, self).label_tag(name, label_suffix, label_attrs)
    
    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your username',
        })

        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your email',
        })

        self.fields['email'].label = "Email (optional)"

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your password',
        })
        self.fields['password1'].label = "Password"

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Confirm your password',
        })
        self.fields['password2'].label = "Confirm password"

    def label_tag(self, name, label_suffix=None, attrs=None):
        label_attrs = {'class': 'label'}
        if attrs:
            label_attrs.update(attrs)
        return super(CustomSignUpForm, self).label_tag(name, label_suffix, label_attrs)
    
    def signup(self, *args, **kwargs):
        return super(CustomSignUpForm, self).signup(*args, **kwargs)