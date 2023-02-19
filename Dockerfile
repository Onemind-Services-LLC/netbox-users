ARG NETBOX_VARIANT=v3.4

FROM netboxcommunity/netbox:${NETBOX_VARIANT}

RUN mkdir -pv /plugins/netbox-users
COPY . /plugins/netbox-users

RUN /opt/netbox/venv/bin/python3 /plugins/netbox-users/setup.py develop
RUN cp -rf /plugins/netbox-users/netbox_users/ /opt/netbox/venv/lib/python3.10/site-packages/netbox_users
