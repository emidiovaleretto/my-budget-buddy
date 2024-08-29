from allauth.account.forms import LoginForm


class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        placeholders = {
            'login': 'Enter your username',
            'password': '••••••••',
            'remember': ''
        }

        self.fields['login'].widget.attrs['autofocus'] = True

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input-field'
            })

        self.fields['remember'].widget.attrs.update({
            'class': 'checkbox'
        })