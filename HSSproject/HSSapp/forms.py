from django import forms

from HSSapp.models import User, Profile,Location


class newuserform(forms.ModelForm):
    class Meta():
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        # exclude=['field1','field2']
        # field=('field1','field2')
        fields = '__all__'

        def clean(self):
            cleaned_data = super().clean()
            Name = cleaned_data.get("username")
            if User.objects.filter(username=Name):
                print("user name already exists")
                msg = "user name already exists!"
                self.add_error('username', msg)


class login(forms.ModelForm):
    class Meta():
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        exclude = ('email', 'phone')

        def clean(self):
            cleaned_data = super().clean()
            # pwd = cleaned_data.get("pwd")
            # cpwd = cleaned_data.get("cpwd")
            Name = cleaned_data.get("username")
            PW = cleaned_data.get("password")
            if User.objects.filter(username=Name):
                print("valid user name")
            else:
                print("invalid username")
                msg1 = "invalid username"
                self.add_error('username', msg1)

            if User.objects.filter(password=PW):
                print("valid password")
            else:
                msg2 = "invalid password"
                self.add_error('password', msg2)


class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']


class locationform(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['name']
