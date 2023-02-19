from django.contrib.auth.models import User, Group
from django.urls import reverse

from users.models import ObjectPermission
from utilities.querysets import RestrictedQuerySet

__all__ = [
    'NetBoxGroup',
    'NetBoxObjectPermission',
    'NetBoxUser',
]


class NetBoxGroup(Group):
    objects = RestrictedQuerySet.as_manager()

    class Meta:
        proxy = True
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def get_absolute_url(self):
        return reverse('plugins:netbox_users:netboxgroup', args=[self.pk])


class NetBoxObjectPermission(ObjectPermission):
    objects = RestrictedQuerySet.as_manager()

    class Meta:
        proxy = True
        verbose_name = 'Object Permission'
        verbose_name_plural = 'Object Permissions'

    def get_absolute_url(self):
        return reverse('plugins:netbox_users:netboxobjectpermission', args=[self.pk])


class NetBoxUser(User):
    objects = RestrictedQuerySet.as_manager()

    class Meta:
        proxy = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_absolute_url(self):
        return reverse('plugins:netbox_users:netboxuser', args=[self.pk])

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.

        This is a copy of the same method in django.contrib.auth.base_user.BaseUserManager
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    def clean(self):
        self.email = self.normalize_email(self.email)
