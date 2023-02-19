from django.urls import path, include

from utilities.urls import get_model_urls
from . import views

app_name = 'netbox_users'

urlpatterns = [
    # Groups
    path('groups/', views.NetBoxGroupListView.as_view(), name='netboxgroup_list'),
    path('groups/add/', views.NetBoxGroupEditView.as_view(), name='netboxgroup_add'),
    path('groups/<int:pk>/', include(get_model_urls(app_name, 'netboxgroup'))),
    # Object Permissions
    path('object-permissions/', views.NetBoxObjectPermissionListView.as_view(), name='netboxobjectpermission_list'),
    path('object-permissions/add/', views.NetBoxObjectPermissionEditView.as_view(), name='netboxobjectpermission_add'),
    path('object-permissions/<int:pk>/', include(get_model_urls(app_name, 'netboxobjectpermission'))),
    # Users
    path('users/', views.NetBoxUserListView.as_view(), name='netboxuser_list'),
    path('users/add/', views.NetBoxUserEditView.as_view(), name='netboxuser_add'),
    path('users/<int:pk>/', include(get_model_urls(app_name, 'netboxuser'))),
]
