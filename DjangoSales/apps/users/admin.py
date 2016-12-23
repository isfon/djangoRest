
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """ A form for creating new users. Includes all the required fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        #Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        #Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="password",
                                         help_text="""Raw passwords are not stored, so there is no way to see this
                                         user's password, but you can change the password using <a href=\"password/\">
                                         this form</a>.""")

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name','tipo',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser',)}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)