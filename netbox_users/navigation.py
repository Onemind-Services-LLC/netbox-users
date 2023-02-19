from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_users:netboxuser_list',
        link_text='Users',
        permissions=['netbox_users.view_netboxuser'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_users:netboxuser_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_users.add_netboxuser'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_users:netboxgroup_list',
        link_text='Groups',
        permissions=['netbox_users.view_netboxgroup'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_users:netboxgroup_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_users.add_netboxusergroup'],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:netbox_users:netboxobjectpermission_list',
        link_text='Object Permissions',
        permissions=['netbox_users.view_netboxobjectpermission'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_users:netboxobjectpermission_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_users.add_netboxobjectpermission'],
            ),
        ),
    ),
)
