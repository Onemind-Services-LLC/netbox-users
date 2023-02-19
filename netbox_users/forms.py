from django import forms
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from netbox.forms import NetBoxModelForm
from utilities.forms import DynamicModelMultipleChoiceField, APISelectMultiple, ContentTypeMultipleChoiceField
from .models import *

__all__ = [
    'NetBoxGroupForm',
    'NetBoxObjectPermissionForm',
    'NetBoxUserForm',
]


class NetBoxGroupForm(NetBoxModelForm):
    object_permissions = DynamicModelMultipleChoiceField(
        queryset=NetBoxObjectPermission.objects.all(),
        required=False,
        label='Permissions',
        help_text='Permissions assigned to this group',
        widget=APISelectMultiple(
            api_url='/api/users/permissions/',
        )
    )

    users = DynamicModelMultipleChoiceField(
        queryset=NetBoxUser.objects.all(),
        required=False,
        label='Users',
        help_text='Users assigned to this group',
        widget=APISelectMultiple(
            api_url='/api/users/users/',
        )
    )

    fieldsets = (
        ('Basic', ('name', 'object_permissions')),
        ('Users', ('users',)),
    )

    class Meta:
        model = NetBoxGroup
        fields = ['name', 'object_permissions', 'users']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set initial values for object_permissions and users
        if self.instance.pk:
            self.fields['object_permissions'].initial = self.instance.object_permissions.all()
            self.fields['users'].initial = self.instance.user_set.all()

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Update the group's permissions
        instance.object_permissions.set(self.cleaned_data['object_permissions'])
        # Update the group's users
        instance.user_set.set(self.cleaned_data['users'])

        if commit:
            instance.save()

        return instance


class NetBoxObjectPermissionForm(NetBoxModelForm):
    object_types = ContentTypeMultipleChoiceField(
        queryset=ContentType.objects.all(),
        label='Object types',
        help_text='The object types to which this permission applies',
    )

    groups = DynamicModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label='Groups',
        help_text='The groups to which this permission applies',
        widget=APISelectMultiple(
            api_url='/api/users/groups/',
        )
    )

    users = DynamicModelMultipleChoiceField(
        queryset=NetBoxUser.objects.all(),
        required=False,
        label='Users',
        help_text='The users to which this permission applies',
        widget=APISelectMultiple(
            api_url='/api/users/users/',
        )
    )

    can_add = forms.BooleanField(
        required=False,
        label='Add',
        help_text='Can create new objects of this type',
    )

    can_change = forms.BooleanField(
        required=False,
        label='Change',
        help_text='Can modify existing objects of this type',
    )

    can_delete = forms.BooleanField(
        required=False,
        label='Delete',
        help_text='Can delete existing objects of this type',
    )

    can_view = forms.BooleanField(
        required=False,
        label='View',
        help_text='Can view existing objects of this type',
    )

    fieldsets = (
        ('Basic', ('name', 'description', 'enabled', 'object_types')),
        ('Permissions', ('can_add', 'can_change', 'can_delete', 'can_view')),
        ('Assignments', ('groups', 'users')),
        ('Constraints', ('constraints',)),
    )

    class Meta:
        model = NetBoxObjectPermission
        fields = (
            'name', 'description', 'enabled', 'object_types', 'groups', 'users', 'constraints', 'can_add', 'can_change',
            'can_delete', 'can_view'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set initial values for object_types, groups, and users
        if self.instance.pk:
            self.fields['object_types'].initial = self.instance.object_types.all()
            self.fields['groups'].initial = self.instance.groups.all()
            self.fields['users'].initial = self.instance.users.all()

            # Set initial values for the CRUD checkboxes
            for action in ['add', 'change', 'delete', 'view']:
                if action in self.instance.actions:
                    self.fields[f'can_{action}'].initial = True
                    self.instance.actions.remove(action)

    def clean(self):
        super().clean()

        # Append any of the selected CRUD checkboxes to the actions list
        actions = []
        for action in ['add', 'change', 'delete', 'view']:
            if self.cleaned_data.get(f'can_{action}'):
                actions.append(action)

        # If no actions were selected, raise a validation error
        if not actions:
            self.add_error(None, 'At least one permission must be selected.')

        self.cleaned_data['actions'] = actions
        return self.cleaned_data


class NetBoxUserForm(NetBoxModelForm):
    groups = DynamicModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label='Groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        widget=APISelectMultiple(
            api_url='/api/users/groups/',
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False
    )

    password_confirm = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput,
        required=False
    )

    fieldsets = (
        ('Basic', ('username', 'first_name', 'last_name', 'email')),
        ('Groups', ('groups',)),
        ('Status', ('is_active', 'is_superuser', 'is_staff')),
        ('Password', ('password', 'password_confirm')),
    )

    class Meta:
        model = NetBoxUser
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_superuser', 'is_staff',
                  'password', 'password_confirm']

    def clean(self):
        super().clean()

        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        # If the user is being created, require a password
        if not self.instance.pk and not password:
            self.add_error('password', 'This field is required.')

        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match.')

        return self.cleaned_data

    def save(self, commit=True):

        instance = super().save(commit=False)

        password = self.cleaned_data.get('password')
        if password:
            instance.set_password(password)

        # Update the user's groups
        instance.groups.set(self.cleaned_data['groups'])

        # If the is_superuser flag is being set, is_staff must also be set
        if instance.is_superuser:
            instance.is_staff = True

        if commit:
            instance.save()

        return instance
