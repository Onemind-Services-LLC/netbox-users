from netbox.tables import NetBoxTable, columns
from .models import *

__all__ = [
    'NetBoxGroupTable',
    'NetBoxObjectPermissionTable',
    'NetBoxUserTable',
]


class NetBoxGroupTable(NetBoxTable):
    object_permissions = columns.TemplateColumn(
        template_code=''' {% for perm in record.object_permissions.all %} {{ perm }} {% endfor %} ''',
        verbose_name='Object Permissions',
    )

    actions = columns.ActionsColumn(
        actions=('edit', 'delete',)
    )

    class Meta(NetBoxTable.Meta):
        model = NetBoxGroup
        fields = (
            'pk', 'id', 'name', 'object_permissions',
        )
        default_columns = (
            'id', 'name', 'object_permissions',
        )


class NetBoxObjectPermissionTable(NetBoxTable):
    actions = columns.ActionsColumn(
        actions=('edit', 'delete',)
    )

    class Meta(NetBoxTable.Meta):
        model = NetBoxObjectPermission
        fields = (
            'pk', 'id', 'name', 'groups', 'users',
        )
        default_columns = (
            'id', 'name', 'groups', 'users',
        )


class NetBoxUserTable(NetBoxTable):
    actions = columns.ActionsColumn(
        actions=('edit', 'delete',)
    )

    class Meta(NetBoxTable.Meta):
        model = NetBoxUser
        fields = (
            'pk', 'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
            'last_login', 'date_joined', 'groups', 'user_permissions',
        )
        default_columns = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
        )
