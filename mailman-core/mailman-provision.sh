#!/bin/sh
if [ -n "$SERVER_HOSTNAME" ]; then
    printf '[mailman]\nsite_owner: mailman@%s\n' "$SERVER_HOSTNAME" >> /etc/mailman.cfg
fi
