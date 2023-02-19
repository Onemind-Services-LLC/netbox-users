# NetBox Users

This is a companion plugin for [NetBox]() that provides a user management interface. It is intended to be used as a
replacement for the default Django user management interface.

## Installation

1. Install the plugin:

    ```shell
    pip install netbox-users
    ```
   
2. Add `netbox_users` to `PLUGINS` in `configuration.py`:

    ```python
    PLUGINS = ['netbox_users']
    ```
   
## Configuration

The plugin has no configuration options.

## Usage

The plugin provides a new top-level navigation menu item called "Users". This menu item is only visible to users with
the `is_staff` flag set to `True`. The menu item provides a list of all users, and a form for creating new users.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Credits

This plugin is created and maintained by [Onemind-Services-LLC](https://github.com/Onemind-Services-LLC).
