from importlib.metadata import metadata

from extras.plugins import PluginConfig

metadata = metadata('netbox_users')


class NetBoxUsersConfig(PluginConfig):
    name = metadata.get('Name').replace('-', '_')
    verbose_name = metadata.get('Summary')
    description = metadata.get('Description')
    version = metadata.get('Version')
    author = metadata.get('Author')
    author_email = metadata.get('Author-email')
    base_url = 'auth'
    min_version = '3.4.0'
    max_version = '3.4.99'


config = NetBoxUsersConfig
