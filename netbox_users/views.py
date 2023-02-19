from netbox.views import generic
from utilities.views import register_model_view
from . import models, tables, forms


#
# Groups
#

class NetBoxGroupListView(generic.ObjectListView):
    queryset = models.NetBoxGroup.objects.all()
    table = tables.NetBoxGroupTable


@register_model_view(models.NetBoxGroup)
class NetBoxGroupView(generic.ObjectView):
    queryset = models.NetBoxGroup.objects.all()


@register_model_view(models.NetBoxGroup, 'edit')
class NetBoxGroupEditView(generic.ObjectEditView):
    queryset = models.NetBoxGroup.objects.all()
    form = forms.NetBoxGroupForm


@register_model_view(models.NetBoxGroup, 'delete')
class NetBoxGroupDeleteView(generic.ObjectDeleteView):
    queryset = models.NetBoxGroup.objects.all()


#
# Object Permissions
#

class NetBoxObjectPermissionListView(generic.ObjectListView):
    queryset = models.NetBoxObjectPermission.objects.all()
    table = tables.NetBoxObjectPermissionTable


@register_model_view(models.NetBoxObjectPermission)
class NetBoxObjectPermissionView(generic.ObjectView):
    queryset = models.NetBoxObjectPermission.objects.all()


@register_model_view(models.NetBoxObjectPermission, 'edit')
class NetBoxObjectPermissionEditView(generic.ObjectEditView):
    queryset = models.NetBoxObjectPermission.objects.all()
    form = forms.NetBoxObjectPermissionForm


@register_model_view(models.NetBoxObjectPermission, 'delete')
class NetBoxObjectPermissionDeleteView(generic.ObjectDeleteView):
    queryset = models.NetBoxObjectPermission.objects.all()


#
# Users
#

class NetBoxUserListView(generic.ObjectListView):
    queryset = models.NetBoxUser.objects.all()
    table = tables.NetBoxUserTable


@register_model_view(models.NetBoxUser)
class NetBoxUserView(generic.ObjectView):
    queryset = models.NetBoxUser.objects.all()


@register_model_view(models.NetBoxUser, 'edit')
class NetBoxUserEditView(generic.ObjectEditView):
    queryset = models.NetBoxUser.objects.all()
    form = forms.NetBoxUserForm


@register_model_view(models.NetBoxUser, 'delete')
class NetBoxUserDeleteView(generic.ObjectDeleteView):
    queryset = models.NetBoxUser.objects.all()
