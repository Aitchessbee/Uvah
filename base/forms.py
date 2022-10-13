from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

        # def save(self, commit=True):
        #     user = super(UserForm, self).save(commit=False)
        #     user.email = self.cleaned_data["email"]
        #     if commit:
        #         user.save()
        #     return user
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"placeholder": "Enter Username"});
        self.fields['email'].widget.attrs.update({"placeholder": "Enter Email"});
        self.fields['password1'].widget.attrs.update({"placeholder": "Enter Password"});
        self.fields['password2'].widget.attrs.update({"placeholder": "Confirm Password"});

        